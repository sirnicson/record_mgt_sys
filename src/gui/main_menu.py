import tkinter as tk
from tkinter import messagebox

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.client_record_gui import ClientRecordGUI

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("TripMaster - Main Menu")

        #Label
        self.label = tk.Label(root, text="Select Record Type to Manage")
        self.label.pack(pady=5)

        # Buttons for different records
        
        # Client
        self.client_btn = tk.Button(root, text="Client Records", command=self.open_client_records)
        self.client_btn.pack(pady=5)

        # Flight
        self.flight_btn = tk.Button(root, text="Flight Records", command=self.open_flight_records)
        self.flight_btn.pack(pady=5)

        # Airline 
        self.airline_btn = tk.Button(root, text="Airline Records", command=self.open_airline_records)
        self.airline_btn.pack(pady=5)

    def open_client_records(self):
        # Open the Client Record GUI
        new_window = tk.Toplevel(self.root)
        ClientRecordGUI(new_window)

    def open_flight_records(self):
        # Open the Flight Record GUI
        new_window = tk.Toplevel(self.root)
        FlightRecordGUI(new_window)

    def open_airline_records(self):
        # Open the Airline Record GUI
        new_window = tk.Toplevel(self.root)
        AirlineRecordGUI(new_window)
