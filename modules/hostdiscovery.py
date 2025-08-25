from modules.ctx import ScanContext
from modules import targetspec, scantech, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain
from modules.exceptions import clear_screen

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Host Discovery ---")
        print("")
        disarpping = input("[--disable-arp-ping] Skip ARP ping on local net? (y/n): ")
        PA = input("[-PA] List ports for TCP ACK ping separated by commas (e.g: 22,80) or in a range (e.g: 20-25) (enter n to leave empty): ")
        PE = input("[-PE] Send standard ICMP ping? (y/n): ")
        PM = input("[-PM] Send ICMP timestamp request? (y/n): ")
        Pn = input("[-Pn] Skip host discovery (This assumes the host is up)? (y/n): ")
        PO = input("[-PO] IP protocol ping? (y/n): ")
        PS = input("[-PS] List ports for TCP SYN ping separated by commas or range (enter n to leave empty): ")
        PU = input("[-PU] List ports for UDP ping separated by commas or range (enter n to leave empty): ")
        sn = input("[-sn] Ping scan (WILL NOT WORK WITH ANY SCAN TECHNIQUE FLAGS)? (y/n): ")

        if disarpping.lower() == "y":
            ctx.add_flag("--disable-arp-ping")
        if PA.lower() != "n":
            ctx.add_flag(f"-PA{PA}")
        if PE.lower() == "y":
            ctx.add_flag("-PE")
        if PM.lower() == "y":
            ctx.add_flag("-PM")
        if Pn.lower() == "y":
            ctx.add_flag("-Pn")
        if PO.lower() == "y":
            ctx.add_flag("-PO")
        if PS.lower() != "n":
            ctx.add_flag(f"-PS{PS}")
        if PU.lower() != "n":
            ctx.add_flag(f"-PU{PU}")
        if sn.lower() == "y":
            ctx.add_flag("-sn")

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
                                clear_screen()
                                targetspec.menu(ctx)
                            case "2":
                                clear_screen()
                                scantech.menu(ctx)
                            case "3":
                                clear_screen()
                                portspecandscanorder.menu(ctx)
                            case "4":
                                clear_screen()
                                serviceverdetect.menu(ctx)
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
                    print("Please select a valid option.")
                    print("")
