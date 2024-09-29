import tkinter as tk
from tkinter import messagebox

class RecordGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TripMaster Record Management System")

        # Labels and entries for a simple form
        self.label = tk.Label(root, text="Name")
        self.label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        
        # Add buttons
        self.create_button = tk.Button(root, text="Create Record", command=self.create_record)
        self.create_button.pack()

    def create_record(self):
        name = self.name_entry.get()
        if name:
            messagebox.showinfo("Info", f"Record for {name} created!")
        else:
            messagebox.showwarning("Warning", "Name cannot be empty!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = RecordGUI(root)
    root.mainloop()
