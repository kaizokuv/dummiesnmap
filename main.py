import os
from modules.ctx import ScanContext
from modules import saves
from modules import custom
from modules import exceptions
from modules.exceptions import backtomain
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others



def main():
    os.system("printf '\033c'")
    ctx = ScanContext()
    while True:
        try:
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
                            os.system("printf '\033c'")
                            targetspec.menu(ctx)
                        case "2":
                            os.system("printf '\033c'")
                            scantech.menu(ctx)
                        case "3":
                            os.system("printf '\033c'")
                            hostdiscovery.menu(ctx)
                        case "4":
                            os.system("printf '\033c'")
                            portspecandscanorder.menu(ctx)
                        case "5":
                            os.system("printf '\033c'")
                            serviceverdetect.menu(ctx)
                        case "6":
                            os.system("printf '\033c'")
                            osdetec.menu(ctx)
                        case "7":
                            os.system("printf '\033c'")
                            nse.menu(ctx)
                        case "8":
                            os.system("printf '\033c'")
                            timingandperf.menu(ctx)
                        case "9":
                            os.system("printf '\033c'")
                            firewallandidsevas.menu(ctx)
                        case "10":
                            os.system("printf '\033c'")
                            outputs.menu(ctx)
                        case "11":
                            os.system("printf '\033c'")
                            others.menu(ctx)
                        case "12":
                            os.system("printf '\033c'")
                            raise backtomain
                        case _:
                            print("Please select a valid option.")
                            print("")
                case "2":
                    ctx.run_and_save()
                    raise backtomain
                case "3":
                    ctx = ScanContext()
                    os.system("printf '\033c'")
                case "4":
                    os.system("printf '\033c'")
                    custom.menu()
                case "5":
                    os.system("printf '\033c'")
                    saves.menu()
                case "6":
                    print("Thank you, please come again")
                    print("Any ideas for future updates are welcome, hmu on Github :D")
                    print("")
                    exit()
                case _:
                    print("Please select a valid option.")
                    print("")
        except exceptions.backtomain:
            continue

if __name__ == "__main__":
    main()
