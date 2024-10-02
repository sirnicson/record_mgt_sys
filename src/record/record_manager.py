import json
import os

from record.client_record import ClientRecord
from record.flight_record import FlightRecord
from record.airline_record import AirlineRecord

class RecordManager:
    def __init__(self):
        # Separate lists for each type of record
        self.client_record = []
        self.flight_record = []
        self.airline_record = []
        self.load_records()  # Load existing records when initialized

    def create_record(self, record):
        record_dict = record.to_dict()
        record_dict['ID'] = self.get_next_id(record.__class__.__name__)  # Assigns unique ID to new record
        if isinstance(record, ClientRecord):
            self.client_record.append(record_dict)
        elif isinstance(record, FlightRecord):
            self.flight_record.append(record_dict)
        elif isinstance(record, AirlineRecord):
            self.airline_record.append(record_dict)

    def get_next_id(self, record_type):
        records = self.get_records_by_type(record_type)
        if not records:
            return 1
        return max(record['ID'] for record in records) + 1  # Returns the next available ID

    def get_records_by_type(self, record_type):
        if record_type == 'Client':
            return self.client_record
        elif record_type == 'Flight':
            return self.flight_record
        elif record_type == 'Airline':
            return self.airline_record
        return []

    def get_record(self, record_type, **kwargs):
        if record_type == "Client":
            record_id = kwargs.get("client_id")  # Get client_id from kwargs
            if record_id is None:
                raise ValueError("Client ID must be provided.")
            return self.get_client_record(record_id)

        elif record_type == "Flight":
            client_id = kwargs.get("client_id")
            airline_id = kwargs.get("airline_id")
            if client_id is None or airline_id is None:
                raise ValueError("Both Client ID and Airline ID must be provided.")
            return self.get_flight_record(client_id, airline_id)

        elif record_type == "Airline":
            record_id = kwargs.get("airline_id")  # Get airline_id from kwargs
            if record_id is None:
                raise ValueError("Airline ID must be provided.")
            return self.get_airline_record(record_id)

        else:
            raise ValueError(f"Unknown record type: {record_type}")

    def get_client_record(self, client_id):
        for record in self.client_record:
            if record["ID"] == client_id:
                return record
        return None

    def get_flight_record(self, client_id, airline_id):
        for flight in self.flight_record:
            if flight.get("client_id") == client_id and flight.get("airline_id") == airline_id:
                return flight
        return None

    def get_airline_record(self, airline_id):
        for record in self.airline_record:
            if record["ID"] == airline_id:
                return record
        return None

    def update_record(self, record_id, updated_fields, record_type):
        # Get the record based on record_id and record_type
        record = self.get_record(record_id, record_type)

        if not record:
            return False
        
        if record_type == "Client":
            self.update_client_record(record, updated_fields)
        elif record_type == "Flight":
            self.update_flight_record(record, updated_fields)
        elif record_type == "Airline":
            self.update_airline_record(record, updated_fields)
        else:
            return False  # Unsupported record type
        
        return True

    def update_client_record(self, record, updated_fields):
        allowed_fields = ['Name', 'Address Line 1', 'Address Line 2', 'Address Line 3', 
                          'City', 'State', 'Zip Code', 'Country', 'Phone Number']
        for key, value in updated_fields.items():
            if key in allowed_fields and value:  # Update only allowed fields
                record[key] = value

    def update_flight_record(self, record, updated_fields):
        allowed_fields = ['Date', 'Start City', 'End City']
        for key, value in updated_fields.items():
            if key in allowed_fields and value:  # Update only allowed fields
                record[key] = value

    def update_airline_record(self, record, updated_fields):
        allowed_fields = ['Company Name']
        for key, value in updated_fields.items():
            if key in allowed_fields and value:  # Update only allowed fields
                record[key] = value

    def delete_record(self, record_type, **kwargs):
        if record_type == "Client":
            client_id = kwargs.get("client_id")
            # Check if client_id is provided
            if client_id is None:
                print("Client ID must be provided.")
                return
            # Find and delete the client record
            for record in self.client_record:
                if record.get("ID") == client_id:
                    self.client_record.remove(record)
                    print(f"Client ID {client_id} successfully deleted.")
                    return
            print(f"Client ID {client_id} not found.")

            
        elif record_type == "Flight":
            client_id = kwargs.get("client_id")
            airline_id = kwargs.get("airline_id")
            
            # Check if both client_id and airline_id are provided
            if client_id is None or airline_id is None:
                print("Both Client ID and Airline ID must be provided.")
                return

            # Find and delete the flight record
            for flight in self.flight_record:
                if flight.get("client_id") == client_id and flight.get("airline_id") == airline_id:
                    self.flight_record.remove(flight)
                    print(f"Flight for Client ID {client_id} and Airline ID {airline_id} successfully deleted.")
                    return
            print(f"No flight found for Client ID {client_id} and Airline ID {airline_id}.")


        elif record_type == "Airline":
            airline_id = kwargs.get("airline_id")
            if airline_id is None:
                print("Airline ID must be provided.")
                return

            # Find and delete the airline record
            for record in self.airline_record:
                if record.get("ID") == airline_id:
                    self.airline_record.remove(record)
                    print(f"Airline ID {airline_id} successfully deleted.")
                    return
            print(f"Airline ID {airline_id} not found.")
        else:
            raise ValueError(f"Unknown record type: {record_type}")

    def save_records(self):
        self.save_records_to_file("data/client_data.json", self.client_record)
        self.save_records_to_file("data/flight_data.json", self.flight_record)
        self.save_records_to_file("data/airline_data.json", self.airline_record)

    def save_records_to_file(self, filename, records):
        try:
            with open(filename, "w") as file:
                json.dump(records, file)
                print(f"Records successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving records to {filename}: {e}")
       

    def load_records(self):
        self.client_record = self.load_records_from_file("data/client_data.json")
        self.flight_record = self.load_records_from_file("data/flight_data.json")
        self.airline_record = self.load_records_from_file("data/airline_data.json")

    def load_records_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def search_record(self, client_id, airline_id):
        # Checks that both client_id and airline_id are provided
        if client_id is None or airline_id is None:
            raise ValueError("Both Client ID and Airline ID must be provided.")

        # Filter flight records based on provided IDs
        matching_records = [
            flight for flight in self.flight_record
            if flight["client_id"] == client_id and flight["airline_id"] == airline_id
        ]

        return matching_records
