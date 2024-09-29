import json

class RecordManager:
    def __init__(self):
        self.records = []

    def create_record(self, record):
        self.records.append(record)

    def update_record(self, record_id, updated_record):
        for record in self.records:
            if record["ID"] == record_id:
                record.update(updated_record)
                return True
        return False

    def delete_record(self,record_id):
        self.records = [rec for rec in self.records if rec["ID"] != record_id]

    def search_record(self, record_id):
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
