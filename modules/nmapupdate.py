import subprocess
import os
import platform
import shutil
from modules.exceptions import clear_screen

def updatenmap():
    while True:
        clear_screen()
        print("--- Nmap Installer/Updater ---")
        print("")
        choice = input("Would you like to install/update Nmap?(y/n): ")
        match choice:
            case "y":
                print("")
                print("Checking for Nmap updates")
                print("")
                distro = "unknown"
                if os.path.exists("/etc/os-release"):
                    with open("/etc/os-release") as f:
                        data = f.read().lower()
                        if "ubuntu" in data or "debian" in data:
                            distro = "debian"
                        elif "arch" in data:
                            distro = "arch"
                        elif "fedora" in data or "centos" in data or "rhel" in data:
                            distro = "fedora"
                elif platform.system() == "Windows":
                    distro = "Windows"
                elif platform.system() == "Darwin":
                    distro = "MacOS"

                try:
                    if distro == "debian":
                        subprocess.run(["sudo", "apt-get", "update"], check=True)
                        subprocess.run(["sudo", "apt-get", "install", "-y", "nmap"], check=True)
                    elif distro == "arch":
                        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "nmap"], check=True)
                    elif distro == "fedora":
                        if shutil.which("dnf"):
                            subprocess.run(["sudo", "dnf", "install", "-y", "nmap"], check=True)
                        elif shutil.which("yum"):
                            subprocess.run(["sudo", "yum", "install", "-y", "nmap"], check=True)
                    elif distro == "Windows":
                        if shutil.which("choco"):
                            if shutil.which("nmap"):
                                subprocess.run(["choco", "upgrade", "nmap", "-y"], check=True)
                            else:
                                subprocess.run(["choco", "install", "nmap"], check=True)
                        else:
                            print("Please install Chocolatey from https://chocolatey.org/install")
                    elif distro == "MacOS":
                        if shutil.which("brew"):
                            subprocess.run(["brew", "update"], check=True)
                            if shutil.which("nmap"):
                                subprocess.run(["brew", "upgrade", "nmap"], check=True)
                            else:
                                subprocess.run(["brew", "install", "nmap"], check=True)
                        else:
                            print("Please install Homebrew from https://brew.sh/")
                    else:
                        print("")
                        print("Could not detect package manager. Skipping update.")
                        return
                    print("")
                    subprocess.run(["nmap", "--version"], check=True)
                    print("")
                    print("Nmap is up to date")
                    print("")
                    print("Welcome to DummiesNmap")
                    input("Press enter to continue..")
                    return
                except Exception as e:
                    print(f"Failed to update Nmap: {e}")
            case "n":
                print("Skipping updates, going to main menu")
                print("")
                print("Welcome to DummiesNmap")
                input("Press enter to continue..")
                return
            case _:
                print("Please select a valid option.")
                print("")
