import json
import os
from datetime import datetime
from modules.exceptions import backtomain
from modules.exceptions import clear_screen

HISTORY_FILE = "scan_history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def add_history(target, flags, final_command, output):
    history = load_history()
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target": target,
        "flags": flags if isinstance(flags, list) else flags.split(),
        "command": final_command,
        "output": output
    }
    history.append(entry)
    save_history(history)

def show_history():
    history = load_history()
    if not history:
        print("No scan history yet.")
        print("")
        return
    clear_screen()
    print("--- Scan History ---")
    for i, entry in enumerate(history, 1):
        print(f"{i}.")
        print(f"[{entry['timestamp']}]")
        print(f"Target: {entry['target']}")
        print(f"Command: {entry['command']}")
        print("")

def historymenu():
    while True:
        print("--- History Menu ---")
        print("1. Show all history")
        print("2. View details of a scan")
        print("3. Clear history")
        print("4. Back to main menu")
        menuchoice = input("> ")
        print("")

        match menuchoice:
            case "1":
                show_history()
                input("Press enter to continue")    
                clear_screen()
            case "2":
                history = load_history()
                if not history:
                    print("No history to view.")
                    print("")
                    input("Press enter to continue")    
                    clear_screen()
                else:
                    while True:
                        show_history()
                        idx = input("Enter scan number to view details (enter n to exit): ")
                        if idx.isdigit() and 1 <= int(idx) <= len(history):
                            entry = history[int(idx)-1]
                            clear_screen()  
                            print("-- Scan Details --")
                            print(f"Timestamp: {entry['timestamp']}")
                            print(f"Target: {entry['target']}")
                            print(f"Flags: {entry['flags']}")
                            print(f"Command: {entry['command']}")
                            print("")
                            print(f"--- Output ---")
                            print(entry['output'])
                            print("")
                            input("Press enter to continue")    
                            clear_screen()
                            historymenu()
                        elif idx == "n":
                            clear_screen()
                            historymenu()
                        else:
                            print("Please select a valid option.")
                            print("")
                            input("Press enter to continue")
                            clear_screen()
            case "3":
                confirm = input("Are you sure you want to clear all history? (y/n): ")
                print("")
                if confirm.lower() == "y":
                    save_history([])
                    print("History cleared.")
                    print("")
                input("Press enter to continue")    
                clear_screen()
            case"4":
                clear_screen()
                raise backtomain
            case _:
                print("")
