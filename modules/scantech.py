import os
from modules.ctx import ScanContext
from modules import targetspec, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Scan Techniques ---")
        print("")
        print("-- TCP Scan Types --")
        print("(Only one per scan)")
        print("DO NOT SELECT IF YOU WANT TO USE CUSTOM TCP FLAGS")
        print("Can be used with UDP scans ONLY (No SCTP)")
        print("")
        sA = input("[-sA] ACK scan, detects firewall/ACL? (y/n): ")
        sF = input("[-sF] TCP FIN scan, stealth scan to detect open ports without full connection? (y/n): ")
        sM = input("[-sM] Maimon scan, sends a TCP packet with FIN and ACK flags? (y/n): ")
        sN = input("[-sN] TCP Null scan, sends a TCP packet with no set flags? (y/n): ")
        sS = input("[-sS] Stealth scan, send SYN packets to check if ports are open? (y/n): ")
        sT = input("[-sT] TCP connect scan, full TCP connection scan? (y/n): ")
        sW = input("[-sW] Window scan, sends ACK packets that checks using window size? (y/n): ")
        sX = input("[-sX] Xmas scan, stealth scan with FIN, PSH and URG flags? (y/n): ")
        print("")
        print("-- UDP Scan --")
        print("(Can be used with TCP, Custom TCP Flags and STCP scans)")
        print("")
        sU = input("[-sU] UDP scan, sends UDP packets? (y/n): ")
        print("")
        print("-- SCTP Scan Types --")
        print("(Only one per scan)")
        print("Can be used with UDP scan ONLY (No TCP)")
        print("")
        sY = input("[-sY] SCTP INIT scan, sends INIT message to see if ports reply? (y/n): ")
        sZ = input("[-sZ] SCTP COOKIE-ECHO scan, send COOKIE-ECHO after INIT? (y/n): ")
        print("")
        print("-- TCP Flags --")
        print("(Replaces TCP Scan Types)")
        print("Can be used with UDP scans ONLY (No SCTP)")
        print("")
        print("ACK - Acknowledge and confirm recieved packets")
        print("CWR - Congestion Window Reduced, used for congestion control")
        print("ECE - ECN Echo, also for congestion control")
        print("FIN - Finish, marks the end of the data")
        print("NS - Nonce Sum, used for ECN experiments")
        print("PSH - Tells receiver to push data to the app now")
        print("RST - Reset the connection")
        print("SYN - Start a connection")
        print("URG - Data to be processed now")
        print("")
        scanflags = input("[--scanflags] Set custom TCP flags separated by commas (e.g: SYN,FIN) (enter n to leave empty): ")

        if sA == "y": ctx.add_flag("-sA")
        if sF == "y": ctx.add_flag("-sF")
        if sM == "y": ctx.add_flag("-sM")
        if sN == "y": ctx.add_flag("-sN")
        if sS == "y": ctx.add_flag("-sS")
        if sT == "y": ctx.add_flag("-sT")
        if sU == "y": ctx.add_flag("-sU")
        if sW == "y": ctx.add_flag("-sW")
        if sX == "y": ctx.add_flag("-sX")
        if sY == "y": ctx.add_flag("-sY")
        if sZ == "y": ctx.add_flag("-sZ")
        if scanflags != "n": ctx.add_flag("--scanflags", scanflags)

        os.system("printf '\033c'")
        print("Current command:", ctx.get_command())
        print("")
        while True:
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
                                os.system("printf '\033c'")
                                targetspec.menu(ctx)
                            case "2":
                                os.system("printf '\033c'")
                                hostdiscovery.menu(ctx)
                            case "3":
                                os.system("printf '\033c'")
                                portspecandscanorder.menu(ctx)
                            case "4":
                                os.system("printf '\033c'")
                                serviceverdetect.menu(ctx)
                            case "5":
                                os.system("printf '\033c'")
                                osdetec.menu(ctx)
                            case "6":
                                os.system("printf '\033c'")
                                nse.menu(ctx)
                            case "7":
                                os.system("printf '\033c'")
                                timingandperf.menu(ctx)
                            case "8":
                                os.system("printf '\033c'")
                                firewallandidsevas.menu(ctx)
                            case "9":
                                os.system("printf '\033c'")
                                outputs.menu(ctx)
                            case "10":
                                os.system("printf '\033c'")
                                others.menu(ctx)
                            case _:
                                print("Please select a valid option.")
                                print("")
                case "3":
                    os.system("printf '\033c'")
                    raise backtomain
                case _:
                    print("Please select a valid option.")
                    print("")
