import json
import os

class RecordManager:
    def __init__(self, filename="05-records.json"):
        self.filename = filename
        self.records = {"clients": [], "flights": [], "airlines": []}
        self.load_records()


    def load_records(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.records = json.load(file)
                except json.JSONDecodeError:
                    print(f"Error: {self.filename} corrupt, initializing empty record")
                    self.records = {"clients": [], "flights": [], "airlines": []}
                    self.save_records()
        else:
            self.save_records()

    def save_records(self):
        with open(self.filename, "w") as file:
            json.dump(self.records, file, indent=4)

    
    # CRUD methods - CREATE - RECORD - UPDATE - DELETE

    def create_record(self, record_type, record):
        if record_type in self.records:
            # Check for duplicate record ID
            if any(r["ID"] == record["ID"] for r in self.records[record_type]):
                raise ValueError(f"Record with {record["ID"]} already exists")
            self.records[record_type].append(record)
            self.save_records()
        else:
            raise ValueError(f"Invalid record type: {record_type}")

    def read_records(self, record_type):
        if record_type in self.records:
            return self.records[record_type]
        else:
            raise ValueError(f"Invalid record type: {record_type}")

    def update_record(self, record_type, record_id, updated_record):
        if record_type in self.records:
            for i, record in enumerate(self.records[record_type]):
                if record["ID"] == record_id:
                    self.records[record_type][i] = updated_record
                    self.save_records()
                    return
                raise ValueError(f"Record with ID {record_id} not found")
            else:
                raise ValueError(f"Invalid record type: {record_type}")

    def delete_record(self, record_type, record_id):
        if record_type in self.records:
            new_records = [record for record in self.records[record_type] if record["ID"] != record_id]
            if len(new_records) == len(self.records[record_type]):
                raise ValueError(f"Record with ID {record_id} not found")
            self.records[record_type] = new_records
            self.save_records()
        else:
            raise ValueError(f"Invalid record type: {record_type}")


