import socket
import datetime

# ==============================
# BANNER
# ==============================
print("""
=====================================
   🔐 CYBERSCAN LITE v1.0
   Network Security Scanner
=====================================
""")

# ==============================
# MENU
# ==============================
print("""
1. Escaneo rápido
2. Escaneo completo
3. Salir
""")

option = input("Selecciona una opción: ")

if option == "3":
    print("Saliendo...")
    exit()

target = input("\nIngresa IP o dominio: ")

# ==============================
# RESOLVER IP
# ==============================
try:
    ip = socket.gethostbyname(target)
    print(f"\n[+] IP resuelta: {ip}")
except socket.gaierror:
    print("[-] Error: no se pudo resolver el dominio")
    exit()

# ==============================
# PUERTOS
# ==============================
if option == "1":
    ports = [22, 80, 443]  # rápido
else:
    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3389]

print("\n🔍 Escaneando puertos...\n")

# ==============================
# ARCHIVO DE REPORTE
# ==============================
filename = "scan_report.txt"
with open(filename, "a") as f:
    f.write("\n=====================================\n")
    f.write(f"Escaneo: {target} ({ip})\n")
    f.write(f"Fecha: {datetime.datetime.now()}\n")
    f.write("=====================================\n")

    # ==============================
    # SCAN
    # ==============================
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((ip, port))

        if result == 0:
            status = f"[ABIERTO] Puerto {port}"

            # ==============================
            # RIESGOS
            # ==============================
            if port == 22:
                status += " ⚠ SSH expuesto (riesgo brute force)"
            elif port == 23:
                status += " ⚠ Telnet inseguro"
            elif port == 445:
                status += " ⚠ SMB vulnerable en redes internas"
            elif port == 3389:
                status += " ⚠ RDP expuesto"

            print(status)

        else:
            status = f"[CERRADO] Puerto {port}"
            print(status)

        f.write(status + "\n")
        s.close()

print("\n✔ Escaneo finalizado")
print(f"📄 Reporte guardado en {filename}")