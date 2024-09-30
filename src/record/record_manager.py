import json

class RecordManager:
    def __init__(self):
        self.records = []
        self.load_records()  # Load existing records upon initialization

    def create_record(self, record):
        record['ID'] = self.get_next_id()  # Assign a unique ID to the new record
        self.records.append(record)

    def get_next_id(self):
        if not self.records:  # If there are no records, start from 1
            return 1
        else:
            # Find the highest ID in the current records
            max_id = max(record['ID'] for record in self.records)
            return max_id + 1  # Return the next available ID

    def update_record(self, record_id, updated_record):
        for record in self.records:
            if record["ID"] == record_id:
                for key, value in updated_record.items():
                    if value:  # Update only if the field is not empty
                        record[key] = value
                return True
        return False

    def delete_record(self, record_id):
        self.records = [rec for rec in self.records if rec["ID"] != record_id]

    def get_record(self, record_id):
        for record in self.records:
            if record["ID"] == record_id:
                return record
        return None

    def save_records(self, filename="data/records.json"):
        with open(filename, "w") as file:
            json.dump(self.records, file)

    def load_records(self, filename="data/records.json"):
        try:
            with open(filename, "r") as file:
                self.records = json.load(file)
        except FileNotFoundError:
            self.records = []
