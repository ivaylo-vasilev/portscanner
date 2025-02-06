#!/usr/bin/python3

import argparse
import socket
import time
import sys
from colorama import init, Fore

init(autoreset=True)

common_ports = [18, 20, 21, 22, 23, 25, 42, 43, 49, 53, 67, 68, 69, 70, 79, 80, 101, 102, 105, 107,
                108, 109, 110, 111, 113, 115, 117, 118, 119, 123, 135, 137, 138, 139, 143, 153, 156,
                158, 161, 162, 170, 179, 194, 199, 213, 218, 220, 280, 401, 427, 434, 443, 445, 465,
                587, 631, 636, 691, 706, 853, 989, 990, 992, 993, 995, 1080, 1194, 1293, 1433, 1434,
                1755, 1863, 2775, 3306, 3389, 5432, 5985, 5986, 6665, 6666, 6667, 6668, 6669, 6670,
                6881, 6882, 6883, 6884, 6885, 6886, 6887, 6888, 6889, 6890, 6969, 8000, 8008, 8080,
                9389, 11371]

parser = argparse.ArgumentParser(prog="portscan", description="PortScanner", epilog="(c) Ivaylo Vasilev")
parser.add_argument("host", nargs="?", help="IP address")
parser.add_argument("-p", "--ports", nargs="+", type=int, default=common_ports, help="ports (separated by space)")
parser.add_argument("-O", "--output", action="store_true", help="save scan result in file")
parser.add_argument("--version", action="version", version="%(prog)s 2025.0", help="show program version")
args = parser.parse_args()

counter = 0
open_ports = []


def main():
    print("PortScanner 2025.0 | (c) Ivaylo Vasilev")
    print("=======================================")

    target_host = args.host
    ports = args.ports

    print(f"\n *  Scanning {target_host} for {len(ports)} open ports ...\n")
    
    port_scanner(target_host, ports)
    
    print(f"\n *  Scanning completed for {target_host}\n")
    print("----- SCAN RESULTS -----")
    
    if counter > 0:
        print(f"[ OPEN PORTS DETECTED: {counter} ]")
        print("")
        for port in open_ports:
            print(f"[+] Port: {port}")
    else:
        print("[ NO OPEN PORTS DETECTED ]")
    
    if args.output:
        print("")
        scan_result(target_host)


def port_scanner(host, ports):
    global counter

    try:
        socket.gethostbyaddr(host)
    except socket.gaierror as e:
        print(f"error: {e}")
        sys.exit(1)
    except socket.herror as e:
        print(f"error: {e}")
        sys.exit(2)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    for port in ports:
        try:
            if sock.connect_ex((host, port)):
                print(f"{Fore.LIGHTRED_EX}[-] Port {port}: CLOSED{Fore.RESET}")
            else:
                open_ports.append(port)
                counter += 1
                print(f"{Fore.LIGHTGREEN_EX}[+] Port {port}: OPEN{Fore.RESET}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"error: {e}")
            sys.exit(3)


def scan_result(host):
    header = """
            **************************
            *       PortScanner      *
            * ---------------------- *
            *   (c) Ivaylo Vasilev   *
            **************************
            **************************

            ------ SCAN RESULTS ------

        """
    
    hostname = host.replace(".", "-")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"ps-{hostname}_{timestamp}.txt"
    
    with open(filename, "a") as file:
        file.write(header)
        if counter > 0:
            file.write(f"[ OPEN PORTS DETECTED: {counter} ]\n")
            for port in open_ports:
                file.write(f"[+] Port: {port}\n")
        else:
            file.write("[ NO OPEN PORTS DETECTED ]\n")
    
    print(f"[*] Scan results saved in: {Fore.LIGHTBLUE_EX}{filename}{Fore.RESET}")


if __name__ == "__main__":
    main()
