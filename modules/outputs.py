import os
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Outputs ---")
        print("")
        print("-- Saving results --")
        print("")
        oN = input("[-oN] Save results in given file path in standard format (e.g: /home/user/nmapdata/data.txt) (enter n to leave empty): ")
        oX = input("[-oX] Save results in given file path in xml format (e.g: /home/user/nmapdata/dataxml.txt) (enter n to leave empty): ")
        oG = input("[-oG] Save results in given file path in grepable format for ease with grep (e.g: /home/user/nmapdata/datagrep.txt) (enter n to leave empty): ")
        oA = input("[-oA] Save results in given file path in all three format (e.g: /home/user/nmapdata/dataall.txt) (enter n to leave empty): ")
        print("")
        print("-- Details --")
        print('')
        v = input("[-v] Add more details? (enter n for empty, 1 for standard, 2 for extra and 3 for most): ")
        d = input("[-d] Enter value to get debugging info (0-9) (enter n to leave empty): ")
        reason = input("[--reason] Get reason for why a port is marked open or closed? (y/n): ")
        openports = input("[--open] Only list open ports? (y/n): ")
        packettrace = input("[--packet-trace] Trace all sent and recieved packets? (y/n): ")
        iflist = input("[--iflist] Show system interfaces and routes? (y/n): ")
        print("")
        print("-- XML-only options --")
        print("")
        defaultstyle = input("[--webxml] Use Nmap's default XML style? (y/n): ")
        customstyle = input("[--stylesheet] Enter file path to add custom stylesheet for XML output (enter n to leave empty): ")
        nostyle = input("[--no-stylesheet] Display raw XML? (y/n): ")
        print("")
        print("-- Others --")
        print("")
        appendoutput = input("[--append-output] Add new scan results to given file path (relates to the file path provided for saving results)? (y/n): ")
        resume = input("[--resume] Enter file path to continue scan from (enter n to leave empty): ")
        nonint = input("[--noninteractive] Run scan without inputs from user? (y/n): ")

        if oA != "n": ctx.add_flag("-oA", oA)
        if oG != "n": ctx.add_flag("-oG", oG)
        if oN != "n": ctx.add_flag("-oN", oN)
        if oX != "n": ctx.add_flag("-oX", oX)

        if v != "n": 
            if v == '1': ctx.add_flag("-v")
            elif v == '2': ctx.add_flag("-vv")
            elif v == '3': ctx.add_flag("-vvv")

        if d != "n":
            try:
                level = int(d)
                if level < 0: level = 0
                if level > 9: level = 9
                ctx.add_flag("-" + "d" * level)
            except ValueError:
                ctx.add_flag("-d")

        if reason == "y": ctx.add_flag("--reason")
        if openports == "y": ctx.add_flag("--open")
        if packettrace == "y": ctx.add_flag("--packet-trace")
        if iflist == "y": ctx.add_flag("--iflist")
        if defaultstyle == "y": ctx.add_flag("--webxml")
        if customstyle != "n": ctx.add_flag("--stylesheet", customstyle)
        if nostyle == "y": ctx.add_flag("--no-stylesheet")
        if appendoutput == "y": ctx.add_flag("--append-output")
        if resume != "n": ctx.add_flag("--resume", resume)
        if nonint == "y": ctx.add_flag("--noninteractive")

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
                        print("6. OS Detection")
                        print("7. Script Scanning (NSE)")
                        print("8. Timing and Performance")
                        print("9. Firewall and IDS Evasion")
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
                                osdetec.menu(ctx)
                            case "7":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                nse.menu(ctx)
                            case "8":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                timingandperf.menu(ctx)
                            case "9":
                                os.system("printf '\033[2J\033[3J\033[H'")
                                firewallandidsevas.menu(ctx)
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
                    