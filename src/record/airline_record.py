class AirlineRecord:
    def __init__(self, airline_id, company_name):
        self.ID = airline_id
        self.Type = "Airline"
        self.CompanyName = company_name

    def to_dict(self):
        return {
                "ID": self.ID,
                "Type": self.Type,
                "Company Name": self.CompanyName
        }
