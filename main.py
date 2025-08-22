import os
from modules import nmapupdate
from modules.ctx import ScanContext
from modules import saves
from modules import custom
from modules import exceptions
from modules.exceptions import backtomain
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others

def main():
    nmapupdate.updatenmap()
    ctx = ScanContext()
    while True:
        try:
            os.system("printf '\033[2J\033[3J\033[H'")
            print("")
            print("██████╗ ██╗   ██╗███╗   ███╗███╗   ███╗██╗███████╗███████╗███╗   ██╗███╗   ███╗ █████╗ ██████╗")
            print("██╔══██╗██║   ██║████╗ ████║████╗ ████║██║██╔════╝██╔════╝████╗  ██║████╗ ████║██╔══██╗██╔══██╗")
            print("██║  ██║██║   ██║██╔████╔██║██╔████╔██║██║█████╗  ███████╗██╔██╗ ██║██╔████╔██║███████║██████╔╝")
            print("██║  ██║██║   ██║██║╚██╔╝██║██║╚██╔╝██║██║██╔══╝  ╚════██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝")
            print("██████╔╝╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║███████╗███████║██║ ╚████║██║ ╚═╝ ██║██║  ██║██║")
            print("╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝")
            print("")
            print("By Kaizokuv")
            print("Github: https://github.com/kaizokuv")
            print("")
            print("--- Main Menu ---")
            print("1. Build new command")
            print("2. Run Nmap with current command")
            print("3. Clear current command")
            print("4. Run and save inputted command")
            print("5. History")
            print("6. Exit")
            print("Current command:", ctx.get_command())
            menuchoice = input("> ")
            print("")

            match menuchoice:
                case "1":
                    print("-- Flag Categories --")
                    print("1. Target Specifications")
                    print("2. Scan Techniques")
                    print("3. Host Discovery")
                    print("4. Port Specification and Scan Order")
                    print("5. Service and Version Detection")
                    print("6. OS Detection")
                    print("7. Script Scanning (NSE)")
                    print("8. Timing and Performance")
                    print("9. Firewall and IDS Evasion")
                    print("10. Outputs")
                    print("11. Miscellaneous")
                    print("12. Back to main menu")
                    flagcat = input("> ")

                    match flagcat:
                        case "1":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            targetspec.menu(ctx)
                        case "2":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            scantech.menu(ctx)
                        case "3":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            hostdiscovery.menu(ctx)
                        case "4":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            portspecandscanorder.menu(ctx)
                        case "5":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            serviceverdetect.menu(ctx)
                        case "6":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            osdetec.menu(ctx)
                        case "7":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            nse.menu(ctx)
                        case "8":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            timingandperf.menu(ctx)
                        case "9":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            firewallandidsevas.menu(ctx)
                        case "10":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            outputs.menu(ctx)
                        case "11":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            others.menu(ctx)
                        case "12":
                            os.system("printf '\033[2J\033[3J\033[H'")
                            raise backtomain
                        case _:
                            print("Please select a valid option.")
                            print("")
                case "2":
                    ctx.run_and_save()
                    raise backtomain
                case "3":
                    ctx = ScanContext()
                    os.system("printf '\033[2J\033[3J\033[H'")
                case "4":
                    os.system("printf '\033[2J\033[3J\033[H'")
                    custom.menu()
                case "5":
                    os.system("printf '\033[2J\033[3J\033[H'")
                    saves.historymenu()
                case "6":
                    print("Thank you, please come again")
                    print("Any ideas for future updates are welcome, hmu on Github :D")
                    print("")
                    exit()
                case _:
                    print("")
        except exceptions.backtomain:
            continue

if __name__ == "__main__":
    main()
