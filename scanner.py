import socket
import os

print("""
========================================
   SYSTEM SECURITY SCANNER
   Author: Shaheer Hussain
========================================
""")

def show_menu():
    print("\n\n === Shaheer System Security Scanner ===")
    print("1. Scan Open Ports (Localhost)")
    print("2. View Running Processes")
    print("3. Password Strength Checker")
    print("4. Exit")




#------------------------------------------
# Port Scanner
#------------------------------------------

def scan_ports():
    print("\n [+] Scanning localhost ports...\n")
    target= "127.0.0.1"

    common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3",
    139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB"
}

    for port in range (20,1025):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.3)

        Result=  s.connect_ex((target, port))
        if Result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[OPEN] Port {port} ({service})")
        s.close()

    print("\n[✔]Scan Complete\n")




#-------------------------------------------
# Process Checker
#-------------------------------------------

def check_processes():
    print("\n [+] Listing running processes...\n")

    try:
        if os.name == "nt":   #Windows 
            os.system("tasklist | more")
        else: #Linux or Mac
            os.system ("pe aux")
    except Exception as e:
        print (" Error", e)

#-------------------------------------------
# Password Strength Checker
#-------------------------------------------

def check_password():
    password = input("\nEnter password to check: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in "!@#$%^&*()" for char in password):
        score += 1

    print("\n[+] Password Analysis:")

    if score <= 2:
        print("Weak Password ❌")
    elif score == 3 or score == 4:
        print("Moderate Password ⚠️")
    else:
        print("Strong Password ✅")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            scan_ports()
        elif choice == "2":
            check_processes()
        elif choice == "3":
            check_password()
        elif choice == "4" :
            print("\n[✔] Exiting Scanner...\n")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
