import tkinter as tk
from tkinter import messagebox
from record.client_record import ClientRecord
from record.record_manager import RecordManager

class ClientRecordGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Client Records")
        
        # Set window size:
        self.root.geometry("400x800")

        # Set window background colour
        self.root.config(bg="#2E4053")

        # Center content of window
        content_frame = tk.Frame(root, bg="#2E4053")
        content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        content_frame.pack(pady=40)

        
        self.manager = RecordManager()
        self.manager.load_records()

        # Create buttons for different actions
        self.create_btn = tk.Button(root, text="Create Record", bg="#1ABC9C", fg="black", font=("Arial", 12, "normal"), command=self.show_create_fields)
        self.create_btn.pack(pady=5)

        self.delete_btn = tk.Button(root, text="Delete Record", bg="#1ABC9C", fg="black", font=("Arial", 12, "normal"), command=self.show_delete_fields)
        self.delete_btn.pack(pady=5)

        self.update_btn = tk.Button(root, text="Update Record", bg="#1ABC9C", fg="black", font=("Arial", 12, "normal"), command=self.show_update_fields)
        self.update_btn.pack(pady=5)

        self.display_btn = tk.Button(root, text="Display Record", bg="#1ABC9C", fg="black", font=("Arial", 12, "normal"), command=self.show_display_fields)
        self.display_btn.pack(pady=5)

        # Placeholder for dynamic fields
        self.dynamic_frame = tk.Frame(root)
        self.dynamic_frame.pack(pady=10)

    def clear_dynamic_frame(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

    def show_create_fields(self):
        self.clear_dynamic_frame()
        tk.Label(self.dynamic_frame, text="Enter Client Details:", font=("bold"), width=40).pack()

        tk.Label(self.dynamic_frame, text="Name:", width=40).pack()
        self.entry_name = tk.Entry(self.dynamic_frame)
        self.entry_name.pack()

        tk.Label(self.dynamic_frame, text="Address Line 1:", width=40).pack()
        self.entry_address1 = tk.Entry(self.dynamic_frame)
        self.entry_address1.pack()

        tk.Label(self.dynamic_frame, text="Address Line 2:", width=40).pack()
        self.entry_address2 = tk.Entry(self.dynamic_frame)
        self.entry_address2.pack(),

        tk.Label(self.dynamic_frame, text="Address Line 3:", width=40).pack()
        self.entry_address3 = tk.Entry(self.dynamic_frame)
        self.entry_address3.pack()

        tk.Label(self.dynamic_frame, text="City:", width=40).pack()
        self.entry_city = tk.Entry(self.dynamic_frame)
        self.entry_city.pack()

        tk.Label(self.dynamic_frame, text="State:", width=40).pack()
        self.entry_state = tk.Entry(self.dynamic_frame)
        self.entry_state.pack()

        tk.Label(self.dynamic_frame, text="Zip Code:", width=40).pack()
        self.entry_zip = tk.Entry(self.dynamic_frame)
        self.entry_zip.pack()

        tk.Label(self.dynamic_frame, text="Country:", width=40).pack()
        self.entry_country = tk.Entry(self.dynamic_frame)
        self.entry_country.pack()

        tk.Label(self.dynamic_frame, text="Phone Number:", width=40).pack()
        self.entry_phone = tk.Entry(self.dynamic_frame)
        self.entry_phone.pack()

        create_record_btn = tk.Button(self.dynamic_frame, text="Create Record", bg="#e6c695", fg="black", command=self.create_record)
        create_record_btn.pack(pady=5)

    def create_record(self):
        name = self.entry_name.get()
        address1 = self.entry_address1.get()
        address2 = self.entry_address2.get()
        address3 = self.entry_address3.get()
        city = self.entry_city.get()
        state = self.entry_state.get()
        zip_code = self.entry_zip.get()
        country = self.entry_country.get()
        phone = self.entry_phone.get()

        if all([name, address1, city, state, zip_code, country, phone]):
            # Generate a unique ID
            record_id = self.manager.get_next_id()

            new_record = {
                "ID": record_id,
                "Type": "Client",
                "Name": name,
                "Address Line 1": address1,
                "Address Line 2": address2,
                "Address Line 3": address3,
                "City": city,
                "State": state,
                "Zip Code": zip_code,
                "Country": country,
                "Phone Number": phone,
            }
            self.manager.create_record(new_record)
            self.manager.save_records()  # Save to file after creation
            messagebox.showinfo("Info", f"Record for {name} created!")
            self.clear_dynamic_frame()
        else:
            messagebox.showwarning("Warning", "All fields except Address Line 2 and 3 must be filled!")

    def show_delete_fields(self):
        self.clear_dynamic_frame()
        tk.Label(self.dynamic_frame, text="Enter ID of Record to Delete:").pack()

        self.entry_delete_id = tk.Entry(self.dynamic_frame)
        self.entry_delete_id.pack()

        delete_record_btn = tk.Button(self.dynamic_frame, text="Delete Record", command=self.delete_record)
        delete_record_btn.pack(pady=5)

    def delete_record(self):
        record_id = self.entry_delete_id.get()

        if record_id.isdigit():
            record_id = int(record_id)
            if self.manager.get_record(record_id):
                self.manager.delete_record(record_id)
                self.manager.save_records()
                messagebox.showinfo("Success", f"Record with ID {record_id} deleted!")
                self.clear_dynamic_frame()
            else:
                messagebox.showerror("Error", f"No record found for ID {record_id}!")
        else:
            messagebox.showwarning("Input Error", "ID must be a number!")

    def show_update_fields(self):
        self.clear_dynamic_frame()
        tk.Label(self.dynamic_frame, text="Enter ID of Record to Update:").pack()

        self.entry_update_id = tk.Entry(self.dynamic_frame)
        self.entry_update_id.pack()

        update_record_btn = tk.Button(self.dynamic_frame, text="Find Record", command=self.load_update_fields)
        update_record_btn.pack(pady=5)

    def load_update_fields(self):
        record_id = self.entry_update_id.get()

        if record_id.isdigit():
            self.record_id = int(record_id)  # Store record ID in an instance variable
            record = self.manager.get_record(self.record_id)
            if record:
                self.clear_dynamic_frame()

                tk.Label(self.dynamic_frame, text="Update Client Details:").pack()

                tk.Label(self.dynamic_frame, text="Name:", width=40).pack()
                self.entry_name = tk.Entry(self.dynamic_frame)
                self.entry_name.insert(0, record["Name"])
                self.entry_name.pack()

                tk.Label(self.dynamic_frame, text="Address Line 1:", width=40).pack()
                self.entry_address1 = tk.Entry(self.dynamic_frame)
                self.entry_address1.insert(0, record["Address Line 1"])
                self.entry_address1.pack()

                tk.Label(self.dynamic_frame, text="Address Line 2:", width=40).pack()
                self.entry_address2 = tk.Entry(self.dynamic_frame)
                self.entry_address2.insert(0, record["Address Line 2"])
                self.entry_address2.pack()

                tk.Label(self.dynamic_frame, text="Address Line 3:", width=40).pack()
                self.entry_address3 = tk.Entry(self.dynamic_frame)
                self.entry_address3.insert(0, record["Address Line 3"])
                self.entry_address3.pack()

                tk.Label(self.dynamic_frame, text="City:", width=40).pack()
                self.entry_city = tk.Entry(self.dynamic_frame)
                self.entry_city.insert(0, record["City"])
                self.entry_city.pack()

                tk.Label(self.dynamic_frame, text="State:", width=40).pack()
                self.entry_state = tk.Entry(self.dynamic_frame)
                self.entry_state.insert(0, record["State"])
                self.entry_state.pack()

                tk.Label(self.dynamic_frame, text="Zip Code:", width=40).pack()
                self.entry_zip = tk.Entry(self.dynamic_frame)
                self.entry_zip.insert(0, record["Zip Code"])
                self.entry_zip.pack()

                tk.Label(self.dynamic_frame, text="Country:", width=40).pack()
                self.entry_country = tk.Entry(self.dynamic_frame)
                self.entry_country.insert(0, record["Country"])
                self.entry_country.pack()

                tk.Label(self.dynamic_frame, text="Phone Number:", width=40).pack()
                self.entry_phone = tk.Entry(self.dynamic_frame)
                self.entry_phone.insert(0, record["Phone Number"])
                self.entry_phone.pack()

                update_button = tk.Button(self.dynamic_frame, text="Update Record", command=self.update_record)
                update_button.pack(pady=5)
            else:
                messagebox.showerror("Error", f"No record found for ID {record_id}!")
        else:
            messagebox.showwarning("Input Error", "ID must be a number!")

    def update_record(self):
        if not hasattr(self, 'record_id'):
            messagebox.showerror("Error", "No record selected for update.")
            return

        updated_record = {
                "ID": self.record_id,
                "Type": "Client",
                "Name": self.entry_name.get(),
                "Address Line 1": self.entry_address1.get(),
                "Address Line 2": self.entry_address2.get(),
                "Address Line 3": self.entry_address3.get(),
                "City": self.entry_city.get(),
                "State": self.entry_state.get(),
                "Zip Code": self.entry_zip.get(),
                "Country": self.entry_country.get(),
                "Phone Number": self.entry_phone.get()
        }

        self.manager.update_record(self.record_id, updated_record)
        self.manager.save_records()
        messagebox.showinfo("Success", f"Record with ID {self.record_id} updated!")
        self.clear_dynamic_frame()


    def select_record(self, record_id):

        # Load the record details into the form
        record = self.manager.get_record(record_id)

        # Populate the entry fields with the record data
        self.entry_name.insert(0, record['Name'])
        self.entry_address1.insert(0, record['Address Line 1'])
        self.entry_address2.insert(0, record['Address Line 2'])
        self.entry_address3.insert(0, record['Address Line 3'])
        self.entry_city.insert(0, record['City'])
        self.entry_state.insert(0, record['State'])
        self.entry_zip.insert(0, record['Zip Code'])
        self.entry_country.insert(0, record['Country'])
        self.entry_phone.insert(0, record['Phone Number'])

        self.record_id = record_id # Set the record_id for later use



    def show_display_fields(self):
        self.clear_dynamic_frame()
        tk.Label(self.dynamic_frame, text="Enter ID of Record to Display:", width=40).pack()

        self.entry_display_id = tk.Entry(self.dynamic_frame)
        self.entry_display_id.pack()

        display_record_btn = tk.Button(self.dynamic_frame, text="Display Record", command=self.display_record)
        display_record_btn.pack(pady=5)

    def display_record(self):
        record_id = self.entry_display_id.get()
        if record_id.isdigit():
            record_id = int(record_id)
            record = self.manager.get_record(record_id)
            if record:
                self.clear_dynamic_frame()
                tk.Label(self.dynamic_frame, text=f"Client Record {record_id}:").pack()
                for key, value in record.items():
                    tk.Label(self.dynamic_frame, text=f"{key}: {value}").pack()
            else:
                messagebox.showerror("Error", f"No record found for ID {record_id}!")
        else:
            messagebox.showwarning("Input Error", "ID must be a number!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientRecordGUI(root)
    root.mainloop()
