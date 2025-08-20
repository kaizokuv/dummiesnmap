import subprocess
from modules import saves

class ScanContext:
    def __init__(self):
        self.base_cmd = ["sudo", "nmap"]
        self.flags = []
        self.target = ""

    def add_flag(self, flag, value=None):
        if value:
            self.flags.append(f"{flag} {value}")
        else:
            self.flags.append(flag)

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
        print("Running:", " ".join(final_command), "\n")
        try:
            result = subprocess.run(final_command, capture_output=True, text=True, bufsize=1)
            output = result.stdout + result.stderr
            print(output)
            saves.add_history(self.target, " ".join(self.flags), " ".join(final_command), output)
            print("Scan complete and saved")
            print("Going back to main menu")
        except Exception as e:
            print(f"[!] Error running Nmap: {e}")
            print("")

    def save_only(self):
        final_command = self.get_command_list()
        print("Saving command for:", " ".join(final_command))
        print("")
        saves.add_history(self.target, " ".join(self.flags), " ".join(final_command), output=None)
        print("Command saved")
        print("Going back to main menu")


