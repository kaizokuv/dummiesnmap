import os
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, timingandperf, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Firewall and IDS Evasion ---")
        print("")
        print("-- Packet fragmentation --")
        print("")
        f = input("[-f] Fragment probe packets? (y/n): ")
        mtu = input("[--mtu] Set custom fragment value in multiples of 8 (enter n to leave empty): ")
        print("")
        print("-- IP masking --")
        print("")
        D = input("[-D] Enter fake IPs as decoys to mask your real IP, use ME to mark your actual IP (e.g: 192.168.0.5,10.25.0.13,ME,206.0.115.13) (enter n to leave empty): ")
        S = input("[-S] Input IP address to spoof source address (enter n to leave empty): ")
        spoofmac = input("[--spoof-mac] Enter a full MAC, prefix or vendor name to fake your network card's MAC address (enter n to leave empty): ")
        print("")
        print("-- Connection routing --")
        print("")
        e = input("[-e] Enter a specified network interface to scan (e.g: wlan0, eth1) (enter n to leave empty): ")
        g = input("[-g] Set a source port to send packets from (e.g: 80) (enter n to leave empty): ")
        proxies = input("[--proxies] Specify proxies to send your connection through (e.g: http://proxy1:8080,socks4://proxy2:1080) (enter n to leave empty): ")
        ttl = input("[--ttl] Set how many hops a packet can take (enter n to leave empty): ")
        print("")
        print("-- Payloads and padding --")
        print("")
        datahex = input("[--data] Enter hex string as custom payload (enter n to leave empty): ")
        datastring = input("[--data-string] Enter ASCII string  as custom payload (enter n to leave empty): ")
        datalength = input("[--data-length] Enter a number of random bytes to pad the packet (enter n to leave empty): ")
        badsum = input("[--badsum] Send bad checksums? (y/n): ")
        print("")
        print("-- IP Options --")
        print("")
        print("Hex bytes - Directly supply hex bytes (e.g: 0101080A)")
        print("L - Specify a list of IPs your packet will follow, but it can choose paths between the given IP (e.g: 192.168.1.1 10.0.0.1)")
        print("R - Let's you see the actual path your packet takes")
        print("S - Specify a list of IPs your packet will follow (e.g: 192.168.1.1 10.0.0.1)")
        print("T - Records when a hop forwards the packet")
        print("U - Tells routers to take a closer look at the packet")
        print("")
        ipoptions = input("[--ip-options] Set IP options separated by spaces (e.g: 0101080A R) (enter n to leave empty): ")

        if f == "y": ctx.add_flag("-f")
        if mtu != "n": ctx.add_flag("--mtu", mtu)
        if D != "n": ctx.add_flag("-D", D)
        if S != "n": ctx.add_flag("-S", S)
        if spoofmac != "n": ctx.add_flag("--spoof-mac", spoofmac)
        if e != "n": ctx.add_flag("-e", e)
        if g != "n": ctx.add_flag("-g", g)
        if proxies != "n": ctx.add_flag("--proxies", proxies)
        if ttl != "n": ctx.add_flag("--ttl", ttl)
        if datahex != "n": ctx.add_flag("--data", datahex)
        if datastring != "n": ctx.add_flag("--data-string", datastring)
        if datalength != "n": ctx.add_flag("--data-length", datalength)
        if badsum == "y": ctx.add_flag("--badsum")
        if ipoptions != "n": ctx.add_flag("--ip-options", ipoptions)

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
                        print("2. Scan Techniques")
                        print("3. Host Discovery")
                        print("4. Port Specification and Scan Order")
                        print("5. Service and Version Detection")
                        print("6. OS Detection")
                        print("7. Script Scanning (NSE)")
                        print("8. Timing and Performance")
                        print("9. Outputs")
                        print("10. Miscellaneous")
                        flagcat = input("> ")

                        match flagcat:
                            case "1":
                                os.system("printf '\033c'")
                                targetspec.menu(ctx)
                            case "2":
                                os.system("printf '\033c'")
                                scantech.menu(ctx)
                            case "3":
                                os.system("printf '\033c'")
                                hostdiscovery.menu(ctx)
                            case "4":
                                os.system("printf '\033c'")
                                portspecandscanorder.menu(ctx)
                            case "5":
                                os.system("printf '\033c'")
                                serviceverdetect.menu(ctx)
                            case "6":
                                os.system("printf '\033c'")
                                osdetec.menu(ctx)
                            case "7":
                                os.system("printf '\033c'")
                                nse.menu(ctx)
                            case "8":
                                os.system("printf '\033c'")
                                timingandperf.menu(ctx)
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
                    