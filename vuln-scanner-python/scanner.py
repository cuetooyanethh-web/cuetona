import socket

print("🔍 Simple Vulnerability Scanner")
print("-" * 40)

target = input("Ingresa IP o dominio: ")

try:
    ip = socket.gethostbyname(target)
    print(f"\n[+] IP resuelta: {ip}")
except socket.gaierror:
    print("[-] No se pudo resolver el dominio")
    exit()

print("\nEscaneando puertos comunes...\n")

ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"[ABIERTO] Puerto {port}")
    else:
        print(f"[CERRADO] Puerto {port}")

    s.close()

print("\n✔ Escaneo finalizado")