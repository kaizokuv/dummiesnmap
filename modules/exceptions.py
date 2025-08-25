import os

class backtomain(Exception):
    pass

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")