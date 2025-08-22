import os
from modules.ctx import ScanContext
from modules import scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Target Specifications ---")
        print("")

        target = input("Enter target IP/domain (enter n to leave empty): ")
        iL = input("[-iL] Enter targets to scan from a given file path (enter n to leave empty): ")
        iR = input("[-iR] Enter the amount of random hosts you want to target (enter 0 for endless targets and n to leave empty): ")
        excludetarget = input("[--exclude] Enter targets to exclude from search separated by commas (e.g: 192.168.0.1,192.168.0.2)(enter n to leave empty): ")
        excludefile = input("[--excludefile] Enter targets to exclude from a given file path (enter n to leave empty): ")

        if target != "n": 
            ctx.set_target(target)
        if iL != "n": 
            ctx.add_flag("-iL", iL)
        if iR != "n":
            if iR == "0":
                print("")
                print("Running -iR with 0 will run it infinitely until stopped with Ctrl + C")
            ctx.add_flag("-iR", iR)
        if excludetarget != "n": 
            ctx.add_flag("--exclude", excludetarget)
        if excludefile != "n": 
            ctx.add_flag("--excludefile", excludefile)

        while True:
            os.system("printf '\033[2J\033[3J\033[H'")
            print("Current command:", ctx.get_command())
            print("")
            print("-- What now? --")
            print("1. Run Nmap with current command")
            print("2. Add more flags")
            print("3. Back to main menu")
            choice = input("> ")
            print("")

            match choice:
                case "1":
                    ctx.run_and_save()
                    raise backtomain
                case "2":
                    while True:
                        print("-- Flag Categories --")
                        print("1. Scan Techniques")
                        print("2. Host Discovery")
                        print("3. Port Specification and Scan Order")
                        print("4. Service and Version Detection")
                        print("5. OS Detection")
                        print("6. Script Scanning (NSE)")
                        print("7. Timing and Performance")
                        print("8. Firewall and IDS Evasion")
                        print("9. Outputs")
                        print("10. Miscellaneous")
                        flagcat = input("> ")

                        match flagcat:
                            case "1":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                scantech.menu(ctx)
                            case "2":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                hostdiscovery.menu(ctx)
                            case "3":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                portspecandscanorder.menu(ctx)
                            case "4":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                serviceverdetect.menu(ctx)
                            case "5":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                osdetec.menu(ctx)
                            case "6":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                nse.menu(ctx)
                            case "7":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                timingandperf.menu(ctx)
                            case "8":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                firewallandidsevas.menu(ctx)
                            case "9":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                outputs.menu(ctx)
                            case "10":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                others.menu(ctx)
                            case _:
                                print("Please select a valid option.")
                                print("")
                case "3":
                    os.system("printf '\033[2J\033[3J\033[H'")
                    raise backtomain
                case _:
                    print("")
