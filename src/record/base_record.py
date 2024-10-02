class  BaseRecord:
    def __init__(self, client_id=None, airline_id=None):
        self.client_id = client_id
        self.airline_id = airline_id

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "airline_id": self.airline_id
        }
