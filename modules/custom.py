import os
import subprocess
from modules.ctx import ScanContext
from modules import saves
from modules.exceptions import backtomain

def menu():
    while True:
        print("-- Custom Commands --")
        print("")
        custom_command = input(
            "Input custom command to run and save (e.g: 192.168.20.5 -sA): "
        ).strip()
        if not custom_command:
            print("No command entered, returning to main menu")
            print("")
            raise backtomain
        parts = custom_command.split()
        target = parts[0]
        flags = parts[1:]
        ctx = ScanContext()
        ctx.set_target(target)
        for flag in flags:
            ctx.add_flag(flag)
        full_cmd_list = ctx.get_command_list()
        print("")
        print("Running:", " ".join(full_cmd_list))
        print("")
        try:
            result = subprocess.run(full_cmd_list, capture_output=True, text=True)
            output = result.stdout + result.stderr
            print(output)
        except Exception as e:
            print(f"Error running command: {e}")
            output = f"Error: {e}"
        saves.add_history(target, " ".join(flags), " ".join(full_cmd_list), output)
        print("Scan complete and saved")
        os.system("printf '\033[2J\033[3J\033[H'")
        tryagainmenu()

def tryagainmenu():
    while True:
        print("-- What now? --")
        print("1. Run/save another command")
        print("2. History")
        print("3. Back to main menu")
        print("4. Exit")
        customcase = input("> ")
        print("")

        match customcase:
            case "1":
                os.system("printf '\033[2J\033[3J\033[H'")
                menu()
            case "2":
                os.system("printf '\033[2J\033[3J\033[H'")
                saves.menu()
            case "3":
                os.system("printf '\033[2J\033[3J\033[H'")
                raise backtomain
            case "4":
                print("Thank you, please come again")
                print("Any ideas for future updates are welcome, hmu on Github :D")
                print("")
                exit()
            case _:
                print("Please select a valid option.")
                print("")
