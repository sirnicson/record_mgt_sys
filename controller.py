from a_model import RecordManager

class Controller:
    def __init__(self):
        self.record_manager = RecordManager()


    # This method would create record for all record types
    def create_record(self, record_type, record):
        try:
            self.record_manager.create_record(record_type, record)
        except ValueError as e:
            print(f"Error creating record: {e}")

    # This method would get record for all record types
    def get_records(self, record_type):
        try:
            return self.record_manager.read_records(record_type)
        except ValueError as e:
            print(f"Error reading records: {e}")

    # This method would update record for all record types
    def update_record(self, record_type, record_id, updated_record):
        try:
            self.record_manager.update_record(record_type, record_id, updated_record)
        except ValueError as e:
            print (f"Error updating record: {e}")
    
    # This method would delete record for all record types
    def delete_record(self, record_type, record_id):
        try:
            self.record_manager.delete_record(record_type, record_id)
        except ValueError as e:
            print(f"Error deleting record: {e}")
