import requests
import os
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def carga():
    slow_print("[*] Iniciando herramienta...", 0.05)
    slow_print("[*] Cargando motor de rastreo...", 0.05)
    slow_print("[*] Estableciendo conexión segura...", 0.05)
    slow_print("[*] Listo.\n", 0.05)

def banner():
    print(Fore.RED + Style.BRIGHT + r"""
 ██▓ ██▓███                       ██▓     ▒█████   ▄████▄  ██ ▄█▀▓█████  ██▀███  
▓██▒▓██░  ██▒▓                   ▓██▒    ▒██▒  ██▒▒██▀ ▀█  ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒▒                  ▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒░ ▒██▒▒██▒░▒██▒   ▒██▒      ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
░██░▒██▒ ░  ░  ▒██▒▒██▒░▒██▒  ▒░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
        """)

    print(Fore.CYAN + "            IP-LOCKER")
    print(Fore.YELLOW + "            @anonymousCRI\n")
    print(Fore.WHITE + "-" * 70)
    print(Fore.GREEN + " Herramienta de geolocalización de direcciones IP")
    print(Fore.GREEN + " by: Rootr MortenTod | Uso educativo")
    print(Fore.WHITE + "-" * 70 + "\n")
    

def rastreo_ip(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,timezone,org,query"

    try:
        respuesta = requests.get(url, timeout=5).json()
    except:
        return None

    if respuesta.get("status") == "fail":
        return None

    return {
        "IP": respuesta["query"],
        "País": respuesta["country"],
        "Región": respuesta["regionName"],
        "Ciudad": respuesta["city"],
        "Zona Horaria": respuesta["timezone"],
        "Proveedor": respuesta["org"],
    }

def resultado(data):
    print(Fore.YELLOW + "\n[+] Información obtenida con éxito\n")
    print(Fore.WHITE + "=" * 40)
    for clave, valor in data.items():
        print(Fore.WHITE + f"{clave:<15}: {valor}")
        time.sleep(0.3)
    print(Fore.WHITE + "=" * 40 + "\n")

def main():
    limpiar()
    banner()
    carga()

    ip = input(Fore.YELLOW + "IP-Locker > Ingrese la dirección IP objetivo ➜  " + Fore.WHITE)
    print("          ")
    
    texto = Fore.WHITE + "[*] Rastreando IP"
    for i in range(9):
        puntos = "." * (i % 4)
        sys.stdout.write("\r" + texto + puntos + "   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

    data = rastreo_ip(ip)

    if data is None:
        print(Fore.RED + "\n[-] IP inválida o privada.\n")
    else:
        resultado(data)

if __name__ == "__main__":
    main()
