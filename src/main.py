import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_menu import MainMenu
from tkinter import Tk

def main():
    root = Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()

