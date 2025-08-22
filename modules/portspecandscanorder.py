import os
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Port Specification and Scan Order ---")
        print("")
        F = input("[-F] Use Fast mode (top 100 common ports)? (y/n): ")
        print("")
        print("-- If not using -F --")
        print("")
        p = input("[-p] List ports to scan by commas (e.g: 22,80) or in a range (e.g: 20-25) (enter n to leave empty): ")
        portratio = input("[--port-ratio] Ratio of ports required to consider host up (0.0 - 1.0, enter n to leave empty): ")
        r = input("[-r] Scan ports in order? (y/n): ")
        topports = input("[--top-ports] Scan N most common ports (enter n to leave empty): ")

        if F == "y": ctx.add_flag("-F")
        if p != "n": ctx.add_flag("-p", p)
        if portratio != "n": ctx.add_flag("--port-ratio", portratio)
        if r == "y": ctx.add_flag("-r")
        if topports != "n": ctx.add_flag("--top-ports", topports)

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
                        print("1. Target Specifications")
                        print("2. Scan Techniques")
                        print("3. Host Discovery")
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
                                targetspec.menu(ctx)
                            case "2":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                scantech.menu(ctx)
                            case "3":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                hostdiscovery.menu(ctx)
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
