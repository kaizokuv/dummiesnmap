from modules.ctx import ScanContext
from modules import scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("")
        print("Current command:", ctx.get_command())
        print("")
        print("--- Target Specifications ---")
        print("")

        target = input("Enter target IP/domain (enter n to leave empty): ")
        iL = input("Enter targets to scan from a given file path (enter n to leave empty): ")
        iR = input("Enter the amount of random hosts you want to target (enter 0 for endless targets and n to leave empty): ")
        excludetarget = input("Enter targets to exclude from search separated by commas (e.g: 192.168.0.1,192.168.0.2)(enter n to leave empty): ")
        excludefile = input("Enter targets to exclude from a given file path (enter n to leave empty): ")

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

        print("")
        print("Current command:", ctx.get_command())
        print("")
        while True:
            print("-- What now? --")
            print("1. Run Nmap with current command")
            print("2. Save command")
            print("3. Add more flags")
            print("4. Back to main menu")
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
                                scantech.menu(ctx)
                            case "2":
                                hostdiscovery.menu(ctx)
                            case "3":
                                portspecandscanorder.menu(ctx)
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
                case "4":
                    raise backtomain
                case _:
                    print("Please select a valid option.")
                    print("")
