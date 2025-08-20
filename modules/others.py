from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, firewallandidsevas, outputs
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("")
        print("Current command:", ctx.get_command())
        print("")
        print("--- Miscellaneous ---")
        print("")
        ipv6 = input("[-6] Use IPv6 instead of IPv4? (y/n): ")
        A = input("[-A] Turn on OS detection, Service version detection, default script scanning and aggresive scanning? (y/n): ")
        datadir = input("[--datadir] Have Nmap use data files from given file path instead of system defaults (e.g: /home/user/custom-nmap-data) (enter n to leave empty): ")
        sendeth = input("[--send-eth] Send packets over Ethernet? (y/n): ")
        sendip = input("[--send-ip] Send packets as raw IP packets (not usable with sending over Ethernet)? (y/n): ")
        priv = input("[--privileged] Get Nmap to assume you're root? (y/n): ")
        unpriv = input("[--unprivileged] Get Nmap to assume you're a normal user (not usable with getting Nmap to assume you're root)? (y/n): ")
        
        if ipv6 == "y": ctx.add_flag("-6")
        if A == "y": ctx.add_flag("-A")
        if datadir != "n": ctx.add_flag("--datadir", datadir)
        if sendeth == "y": ctx.add_flag("--send-eth")
        if sendip == "y": ctx.add_flag("--send-ip")
        if priv == "y": ctx.add_flag("--privileged")
        if unpriv == "y": ctx.add_flag("--unprivileged")

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
                        print("4. Port Specification and Scan Order")
                        print("5. Service and Version Detection")
                        print("6. OS Detection")
                        print("7. Script Scanning (NSE)")
                        print("8. Timing and Performance")
                        print("9. Firewall and IDS Evasion")
                        print("10. Outputs")
                        flagcat = input("> ")

                        match flagcat:
                            case "1":
                                targetspec.menu(ctx)
                            case "2":
                                scantech.menu(ctx)
                            case "3":
                                hostdiscovery.menu(ctx)
                            case "4":
                                portspecandscanorder.menu(ctx)
                            case "5":
                                serviceverdetect.menu(ctx)
                            case "6":
                                osdetec.menu(ctx)
                            case "7":
                                nse.menu(ctx)
                            case "8":
                                timingandperf.menu(ctx)
                            case "9":
                                firewallandidsevas.menu(ctx)
                            case "10":
                                outputs.menu(ctx)
                            case _:
                                print("Please select a valid option.")
                                print("")
                case _:
                    print("Please select a valid option.")
                    print("")
                    