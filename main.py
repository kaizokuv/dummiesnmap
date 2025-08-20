from modules.ctx import ScanContext
from modules import saves
from modules import custom
from modules import exceptions
from modules.exceptions import backtomain
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others

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

def main():

    ctx = ScanContext()

    while True:
        try:
            print("")
            print("--- Main Menu ---")
            print("1. Build new command")
            print("2. Clear current command")
            print("3. Run and save inputted command")
            print("4. History")
            print("5. Exit")
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
                            targetspec.menu(ctx)
                        case "2":
                            scantech.menu(ctx)
                        case "3":
                            hostdiscovery.menu(ctx)
                        case "4":
                            portspecandscanorder.menu(ctx)
                        case "5":
                            serviceverdetect.menu(ctx)
                        case "6":
                            osdetec.menu(ctx)
                        case "7":
                            nse.menu(ctx)
                        case "8":
                            timingandperf.menu(ctx)
                        case "9":
                            firewallandidsevas.menu(ctx)
                        case "10":
                            outputs.menu(ctx)
                        case "11":
                            others.menu(ctx)
                        case "12":
                            raise backtomain
                        case _:
                            print("Please select a valid option.")
                            print("")
                case "2":
                    ctx = ScanContext()
                    print("Current command cleared")
                    print("")
                case "3":
                    custom.menu()
                case "4":
                    saves.menu()
                case "5":
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
