import os
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- OS Detection ---")
        print("")
        O = input("[-O] Detect target OS? (y/n): ")
        print("")
        print("-- If OS Detection Is On --")
        print("")
        osguess = input("[--osscan-guess] Guess a host's OS when exact match is not found? (y/n): ")
        oslimit = input("[--osscan-limit] Limit OS detection to promising targets? (y/n): ")

        if O == "y": ctx.add_flag("-O")
        if osguess == "y": ctx.add_flag("--osscan-guess")
        if oslimit == "y": ctx.add_flag("--osscan-limit")

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
                        print("4. Port Specification and Scan Order")
                        print("5. Service and Version Detection")
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
                                portspecandscanorder.menu(ctx)
                            case "5":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                serviceverdetect.menu(ctx)
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
                    print("Please select a valid option.")
                    print("")
