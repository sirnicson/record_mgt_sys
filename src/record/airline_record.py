from record.base_record import BaseRecord

class AirlineRecord(BaseRecord):
    def __init__(self, airline_id, company_name):
        super().__init__(airline_id=airline_id)
        self.Type = "Airline"
        self.CompanyName = company_name

    def to_dict(self):
        airline_record = super().to_dict()
        airline_record.update({
            "ID": self.airline_id,
            "Type": self.Type,
            "Company Name": self.CompanyName
        })
        return airline_record
