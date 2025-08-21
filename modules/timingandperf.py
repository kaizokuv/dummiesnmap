import os
from modules.ctx import ScanContext
from modules import targetspec, scantech, hostdiscovery, portspecandscanorder, serviceverdetect, osdetec, nse, firewallandidsevas, outputs, others
from modules.exceptions import backtomain

def menu(ctx: ScanContext):
    while True:
        print("Current command:", ctx.get_command())
        print("")
        print("--- Timing and Performance ---")
        print("")
        T = input("[-T] Enter a value of 0-5 to determine the speed of the scan, 0 for slowest 5 for fastest (enter n to leave empty): ")
        print("")
        print("-- Retry and timeout --")
        print("")
        maxretries = input("[--max-retries] Enter the maximum number of probe retransmissions (enter n to leave empty): ")
        minrtttimeout = input("[--min-rtt-timeout] Enter the minimum time for round-trip-time estimate (e.g: 5ms for 5 milliseconds, 1s for 1 second, 3m for 3 minutes, or 4h for 4 hours) (enter n to leave empty): ")
        maxrtttimeout = input("[--max-rtt-timeout] Enter the maximum time for round-trip-time estimate (e.g: 5ms for 5 milliseconds, 1s for 1 second, 3m for 3 minutes, or 4h for 4 hours) (enter n to leave empty): ")
        inirtttimeout = input("[--initial-rtt-timeout] Enter the starting time for round-trip-time estimate (e.g: 5ms for 5 milliseconds, 1s for 1 second, 3m for 3 minutes, or 4h for 4 hours) (enter n to leave empty): ")
        print("")
        print("-- Parallelism --")
        print("")
        minpar = input("[--min-parallelism] Enter minimum number of probes to run in parallel (enter n to leave empty): ")
        maxpar = input("[--max-parallelism] Enter maximum number of probes to run in parallel (enter n to leave empty): ")
        minhostgroup = input("[--min-hostgroup] Enter minimum amount of hosts to scan in parallel (enter n to leave empty): ")
        maxhostgroup = input("[--max-hostgroup] Enter maximum amount of hosts to scan in parallel (enter n to leave empty): ")
        print("")
        print("-- Rate control --")
        print("")
        minrate = input("[--min-rate] Send a set minimum amount of packets per second (enter n to leave empty): ")
        maxrate = input("[--max-rate] Send a set maximum amount of packets per second (enter n to leave empty): ")
        print("")
        print("-- Scan delays --")
        print("")
        scandelay = input("[--scan-delay] Enter amount of time to wait between probes to the host (e.g: 5ms for 5 milliseconds, 1s for 1 second, 3m for 3 minutes, or 4h for 4 hours) (enter n to leave empty): ")
        maxscandelay = input("[--max-scan-delay] Enter max amount of time to wait between probes to the host (e.g: 5ms for 5 milliseconds, 1s for 1 second, 3m for 3 minutes, or 4h for 4 hours) (enter n to leave empty): ")
        print("")
        print("-- Firewall and RST handling --")
        print("")
        defrstratelmt = input("[--defeat-rst-ratelimit] Bypass firewalls that rate-limit RST packets? (y/n): ")
        print("")
        print("-- Nsock Engines --")
        print("")
        print("epoll - Very efficient for large scans (Linux only)")
        print("iocp - Uses IO Completion Ports (Windows only)")
        print("kqueue - Event notification system for BSD and macOS")
        print("poll - More quicker version of 'select' (Unix systems only)")
        print("select - Basic, portable method (Works everywhere, but slow)")
        print("")
        nsock = input("[--nsock-engine] Choose Nsock engine (enter n to leave empty): ")
        
        if T != "n": ctx.add_flag("-T",T)
        if maxretries != "n": ctx.add_flag("--max-retries", maxretries)
        if minrtttimeout != "n": ctx.add_flag("--min-rtt-timeout", minrtttimeout)
        if maxrtttimeout != "n": ctx.add_flag("--max-rtt-timeout", maxrtttimeout)
        if inirtttimeout != "n": ctx.add_flag("--initial-rtt-timeout", inirtttimeout)
        if minpar != "n": ctx.add_flag("--min-parallelism", minpar)
        if maxpar != "n": ctx.add_flag("--max-parallelism", maxpar)
        if minhostgroup != "n": ctx.add_flag("--min-hostgroup", minhostgroup)
        if maxhostgroup != "n": ctx.add_flag("--max-hostgroup", maxhostgroup)
        if minrate != "n": ctx.add_flag("--min-rate", minrate)
        if maxrate != "n": ctx.add_flag("--max-rate", maxrate)
        if scandelay != "n": ctx.add_flag("--scan-delay", scandelay)
        if maxscandelay != "n": ctx.add_flag("--max-scan-delay", maxscandelay)
        if defrstratelmt == "y": ctx.add_flag("--defeat-rst-ratelimit")
        if nsock != "n": ctx.add_flag("--nsock-engine", nsock)

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
                    