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

        # Set window size:
        self.root.geometry("600x400")

        # Set window background colour
        self.root.config(bg="#2E4053")

        # Center content of window
        content_frame = tk.Frame(root, bg="#2E4053")
        content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Header Label
        self.label = tk.Label(root, text="TripMaster Record Management System", bg="#2E4053", fg="white", font=("Verdana", 20, "normal"))
        self.label.pack(pady=40)


        #Label
        self.label = tk.Label(root, text="Select Record Type to Manage", bg="#2E4053", fg="grey", font=("Arial", 12, "bold"))
        self.label.pack(pady=30)

        # Buttons for different records
        
        # Client with style customization
        self.client_btn = tk.Button(root, text="Client Records", command=self.open_client_records, bg="#1ABC9C", fg="black", font=("Arial", 12, "bold"))
        self.client_btn.pack(pady=10)

        # Flight with style customization
        self.flight_btn = tk.Button(root, text="Flight Records", command=self.open_flight_records, bg="#1ABC9C", fg="black", font=("Arial", 12, "bold"))
        self.flight_btn.pack(pady=10)

        # Airline with style customization
        self.airline_btn = tk.Button(root, text="Airline Records", command=self.open_airline_records, bg="#1ABC9C", fg="black", font=("Arial", 12, "bold"))
        self.airline_btn.pack(pady=10)

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
