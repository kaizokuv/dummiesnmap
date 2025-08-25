from modules.exceptions import clear_screen
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")        
        print("--- Script Scanning (NSE) ---")
        print("")
        sC = input("[-sC] Run Nmap's default script set? (y/n): ")
        print("")
        print("-- Script Categories --")
        print("")
        print("all - Every script installed in your system (varies user to user if you installed custom scripts)")
        print("auth - Authentication (checks for logins, credentials, bypasses etc)")
        print("broadcast - Discovering hosts on the current network")
        print("brute - Brute force attacks")
        print("default - Jack of all trades script")
        print("discovery - Find services, hosts and details")
        print("dos - Denial of service checks")
        print("exploit - Extremely intrusive active exploitation")
        print("external - Queries for outside services/APIs")
        print("fuzzer - Protocol fuzzing")
        print("intrusive - Aggressive, noisy and disruptive scripts")
        print("malware - Checks for any known malware or backdoors")
        print("safe - Safe scripts that you could run in production")
        print("version - Extended version detection")
        print("vuln - Vulnerability checks such as CVEs and misconfigs")
        print("")
        choosescript = input("[--script] Choose the scripts you would like to run (e.g: default,safe) (enter n to leave empty): ")
        scriptargs = input("[--script-args] Enter arguements for chosen NSE scripts (enter n to leave empty): ")
        scriptargsfile =  input("[--script-args-file] Load arguements for chosen NSE scripts from given file path (enter n to leave empty): ")
        scripttrace = input("[--script-trace] Trace traffic for chosen NSE scripts and arguements? (y/n): ")

        if sC == "y": ctx.add_flag("-sC")
        if choosescript != "n": ctx.add_flag(f"--script={choosescript}")
        if scriptargs != "n": ctx.add_flag(f"--script-args={scriptargs}")
        if scriptargsfile != "n": ctx.add_flag(f"--script-args-file={scriptargsfile}")
        if scripttrace == "y": ctx.add_flag("--script-trace")

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
                        print("5. Service and Version Detection")
                        print("6. OS Detection")
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
                                serviceverdetect.menu(ctx)
                            case "6":
                                clear_screen()
                                osdetec.menu(ctx)
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
