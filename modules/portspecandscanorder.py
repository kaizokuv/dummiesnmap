from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("")
        print("Current command:", ctx.get_command())
        print("")
        print("--- Port Specification and Scan Order ---")
        print("")
        F = input("[-F] Use Fast mode (top 100 common ports)? (y/n): ")
        p = input("[-p] List ports to scan by commas or ranges (enter n to leave empty): ")
        portratio = input("[--port-ratio] Ratio of ports required to consider host up (0.0 - 1.0, enter n to leave empty): ")
        r = input("[-r] Scan ports in order? (y/n): ")
        topports = input("[--top-ports] Scan N most common ports (enter n to leave empty): ")

        if F == "y": ctx.add_flag("-F")
        if p != "n": ctx.add_flag("-p", p)
        if portratio != "n": ctx.add_flag("--port-ratio", portratio)
        if r == "y": ctx.add_flag("-r")
        if topports != "n": ctx.add_flag("--top-ports", topports)

        print("")
        print("Current command:", ctx.get_command())
        print("")
        while True:
            print("-- What now? --")
            print("1. Run Nmap with current command")
            print("2. Save command")
            print("3. Add more flags")
            choice = input("> ")
            print("")

            match choice:
                case "1":
                    ctx.run_and_save()
                    raise backtomain
                case "2":
                    ctx.save_only()
                    raise backtomain
                case "3":
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
                                targetspec.menu(ctx)
                            case "2":
                                scantech.menu(ctx)
                            case "3":
                                hostdiscovery.menu(ctx)
                            case "4":
                                serviceverdetect.menu(ctx)
                            case "5":
                                osdetec.menu(ctx)
                            case "6":
                                nse.menu(ctx)
                            case "7":
                                timingandperf.menu(ctx)
                            case "8":
                                firewallandidsevas.menu(ctx)
                            case "9":
                                outputs.menu(ctx)
                            case "10":
                                others.menu(ctx)
                            case _:
                                print("Please select a valid option.")
                                print("")
                case _:
                    print("Please select a valid option.")
                    print("")
