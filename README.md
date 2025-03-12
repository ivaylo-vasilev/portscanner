# PortScanner
Scan a device from the network for open ports.
---

**PortScanner** is a Python based CLI program intended to scan a device from the network for open ports. By default the program will scan a predifined selection of 100 ports, but you can specify a list of ports, or even a single port, to be scanned by using the optional argument `-p, --ports` and type a list of port numbers separated by spaces. **PortScanner** will show the currently scanned ports in terminal using colors to indicate open (green color) and closed (red color) ports. After the scan is complete you will be able to see a summary of all the open ports found on the scanned device. The program has also an option to save the result in a text file. To do that add `-O, --output` as an optional argument in the command. ***Do not*** type a name for the text file, as it will be given automatically and will contain the IP of the device and the date and time of the performed scan.

*Example usage:*

`$python3 portscan.py [ip]` -> scan the device using 100 common ports

`$python3 portscan.py [ip] -O` -> scan the device using 100 common ports, save the result in text file

`$python3 portscan.py [ip] -p <ports ...>` -> scan the specified list of ports on the device


*For additional usage and help:*

`$python3 portscan.py --help`

---

![portscan](https://github.com/user-attachments/assets/710dfd97-7786-40ac-8268-a65b1d9d5f3f)
