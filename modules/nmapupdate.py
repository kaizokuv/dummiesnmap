import subprocess
import os
from modules.exceptions import backtomain

def updatenmap():
    os.system("printf '\033[2J\033[3J\033[H'")
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

    try:
        if distro == "debian":
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "--only-upgrade", "-y", "nmap"], check=True)
        elif distro == "arch":
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "nmap"], check=True)
        elif distro == "fedora":
            subprocess.run(["sudo", "dnf", "upgrade", "-y", "nmap"], check=True)
        else:
            print("")
            print("Could not detect package manager. Skipping update.")
            raise backtomain
        print("")
        print("Nmap is up to date")
        print("")
        print("Welcome to DummiesNmap")
        input("> ")
    except Exception as e:
        print(f"Failed to update Nmap: {e}")
