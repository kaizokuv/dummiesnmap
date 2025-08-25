from modules.exceptions import clear_screen
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Service and Version Detection ---")
        print("")
        sV = input("[-sV] Detect service versions? (y/n): ")
        print("")
        print("-- If Service Version Detection Is On --")
        print("")
        verall = input("[--version-all] Check all probes for services? (y/n): ")
        verint = input("[--version-intensity] Select a version scan intensity (0-9) (enter n to leave empty): ")
        verlight = input("[--version-light] Lighter service detection? (y/n): ")

        if sV == "y": ctx.add_flag("-sV")
        if verall == "y": ctx.add_flag("--version-all")
        if verint != "n": ctx.add_flag("--version-intensity", verint)
        if verlight == "y": ctx.add_flag("--version-light")

        while True:
            clear_screen()
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
                        print("4. Port Specification and Scan Order")
                        print("5. OS Detection")
                        print("6. Script Scanning (NSE)")
                        print("7. Timing and Performance")
                        print("8. Firewall and IDS Evasion")
                        print("9. Outputs")
                        print("10. Miscellaneous")
                        flagcat = input("> ")

                        match flagcat:
                            case "1":
                                clear_screen()
                                targetspec.menu(ctx)
                            case "2":
                                clear_screen()
                                scantech.menu(ctx)
                            case "3":
                                clear_screen()
                                hostdiscovery.menu(ctx)
                            case "4":
                                clear_screen()
                                portspecandscanorder.menu(ctx)
                            case "5":
                                clear_screen()
                                osdetec.menu(ctx)
                            case "6":
                                clear_screen()
                                nse.menu(ctx)
                            case "7":
                                clear_screen()
                                timingandperf.menu(ctx)
                            case "8":
                                clear_screen()
                                firewallandidsevas.menu(ctx)
                            case "9":
                                clear_screen()
                                outputs.menu(ctx)
                            case "10":
                                clear_screen()
                                others.menu(ctx)
                            case _:
                                print("Please select a valid option.")
                                print("")
                case "3":
                    clear_screen()
                    raise backtomain
                case _:
                    print("")
