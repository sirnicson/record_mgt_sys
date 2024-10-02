from record.base_record import BaseRecord

class ClientRecord(BaseRecord):
    def __init__(self, client_id, name, address_line1, address_line2, address_line3, city, state, zip_code, country, phone):
        super().__init__(client_id=client_id)
        self.Type = "Client"
        self.Name = name
        self.AddressLine1 = address_line1
        self.AddressLine2 = address_line2
        self.AddressLine3 = address_line3
        self.City = city
        self.State = state
        self.ZipCode = zip_code
        self.Country = country
        self.Phone = phone

    def to_dict(self):
        client_record = super().to_dict()
        client_record.update({
            "ID": self.client_id,
            "Type": self.Type,
            "Name": self.Name,
            "Address Line 1": self.AddressLine1,
            "Address Line 2": self.AddressLine2,
            "Address Line 3": self.AddressLine3,
            "City": self.City,
            "State": self.State,
            "Zip Code": self.ZipCode,
            "Country": self.Country,
            "Phone Number": self.Phone
        })
        return client_record
