class FlightRecord:
    def __init__(self, client_id, airline_id, date, start_city, end_city):
        self.ClientID = client_id
        self.AirlineID = airline_id
        self.Date = date
        self.StartCity = start_city
        self.EndCity = end_city

    def to_dict(self):
        return {
                "Client_ID": self.ClientID,
                "Airline_ID": self.AirlineID,
                "Date": self.Date.isoformat(),
                "Start City": self.StartCity,
                "End City": self.EndCity
        }
