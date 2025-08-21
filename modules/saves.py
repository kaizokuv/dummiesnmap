import json
import os
from datetime import datetime
from modules.exceptions import backtomain

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
        "flags": flags,
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
    os.system("printf '\033c'")
    print("--- Scan History ---")
    for i, entry in enumerate(history, 1):
        print(f"{i}.")
        print(f"[{entry['timestamp']}]")
        print(f"Target: {entry['target']}")
        print(f"Command: {entry['command']}")
        print("")

def menu():
    while True:
        print("--- History Menu ---")
        print("1. Show all history")
        print("2. View details of a scan")
        print("3. Rerun old command with new target")
        print("4. Clear history")
        print("5. Back to main menu")
        menuchoice = input("> ")
        print("")

        match menuchoice:
            case "1":
                show_history()
                input("Press enter to continue")    
                os.system("printf '\033c'")
            case "2":
                history = load_history()
                if not history:
                    print("No history to view.")
                    print("")
                    input("Press enter to continue")    
                    os.system("printf '\033c'")
                else:
                    while True:
                        show_history()
                        idx = input("Enter scan number to view details: ")
                        if idx.isdigit() and 1 <= int(idx) <= len(history):
                            entry = history[int(idx)-1]
                            print("")
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
                            os.system("printf '\033c'")
                            menu()
                        else:
                            print("Please select a valid option.")
                            print("")
                            input("Press enter to continue")
                            os.system("printf '\033c'")
            case "3":
                history = load_history()
                if not history:
                    print("No history to view.")
                    print("")
                    input("Press enter to continue")    
                    os.system("printf '\033c'")
                else:
                    while True:
                        os.system("printf '\033c'")
                        show_history()
                        idx = input("Enter scan number to view and use details: ")
                        if idx.isdigit() and 1 <= int(idx) <= len(history):
                            entry = history[int(idx)-1]
                            print("")
                            print("-- Scan Details --")
                            print(f"Timestamp: {entry['timestamp']}")
                            print(f"Target: {entry['target']}")
                            print(f"Flags: {entry['flags']}")
                            print(f"Command: {entry['command']}")
                            print("")
                            while True:
                                replace = input("Do you want to reuse this scan with a new target? (y/n):" )
                                if replace == "y":
                                    print("")
                                    newtarget = input("Enter new target: ")
                                    if not newtarget:
                                        print("")
                                        print("Invalid target")
                                        print("")
                                        input("Press enter to continue")
                                        os.system("printf '\033c'")
                                    from modules.ctx import ScanContext
                                    ctx = ScanContext()
                                    for flag in entry["flags"].split():
                                        if flag.startswith("-"):
                                            ctx.add_flag(flag)
                                    ctx.set_target(newtarget)
                                    ctx.run_and_save()
                                else:
                                    os.system("printf '\033c'")  
                                    menu() 
                        else:
                            print("Please select a valid option.")
                            print("")
                            input("Press enter to continue")
                            os.system("printf '\033c'")
            case "4":
                confirm = input("Are you sure you want to clear all history? (y/n): ")
                print("")
                if confirm.lower() == "y":
                    save_history([])
                    print("History cleared.")
                    print("")
                input("Press enter to continue")    
                os.system("printf '\033c'")
            case"5":
                os.system("printf '\033c'")
                raise backtomain
            case _:
                print("Please select a valid option.")
                print("")
