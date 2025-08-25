import subprocess
from modules import saves
from modules.exceptions import clear_screen

class ScanContext:
    def __init__(self):
        self.base_cmd = ["sudo", "nmap"]
        self.flags = []
        self.target = ""

    def add_flag(self, flag, value=None):
        if value is None:
            self.flags.append(flag)
        else:
            self.flags.extend([flag, str(value)])

    def set_target(self, target):
        self.target = target
        if target in self.base_cmd:
            self.base_cmd.remove(target)
        if target:
            self.base_cmd.append(target)

    def get_command_list(self):
        return self.base_cmd + self.flags

    def get_command(self):
        return " ".join(self.get_command_list())

    def run_and_save(self):
        final_command = self.get_command_list()
        if final_command == ["sudo", "nmap"]:
            print("Please provide a target/flag before running")
            print("")
            input("Press enter to continue")
            self.base_cmd = ["sudo", "nmap"]
            self.flags = []
            self.target = ""
            print("Going back to main menu")
            clear_screen()
        else:
            print("Running:", " ".join(final_command))
            print("")
            try:
                result = subprocess.run(final_command, capture_output=True, text=True, bufsize=1)
                output = result.stdout + result.stderr
                print(output)
                saves.add_history(self.target, " ".join(self.flags), " ".join(final_command), output)
                print("Scan complete and saved")
            except Exception as e:
                print(f"Error running command: {e}")
                output = f"Error: {e}"
                print("")
            input("Press enter to continue")
            self.base_cmd = ["sudo", "nmap"]
            self.flags = []
            self.target = ""
            print("Going back to main menu")
            clear_screen()