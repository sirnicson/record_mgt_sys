from record.base_record import BaseRecord
from datetime import datetime

class FlightRecord(BaseRecord):
    def __init__(self, client_id, airline_id, date, start_city, end_city):
        super().__init__(client_id=client_id, airline_id=airline_id)
        self.Type = "Flight"
        self.Date = datetime.strptime(date, "%Y-%m-%d")
        self.StartCity = start_city
        self.EndCity = end_city

    def to_dict(self):
        flight_record = super().to_dict()
        flight_record.update({
            "Date":self.Date.isoformat(),
            "Start City": self.StartCity,
            "End City": self.EndCity
        })
        return flight_record
