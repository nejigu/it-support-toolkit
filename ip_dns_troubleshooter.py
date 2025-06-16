import socket
import platform
import subprocess

# Try to import requests, but allow the script to continue if not present
try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    HAVE_REQUESTS = False

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        return f"[!] Error getting local IP: {e}"
    finally:
        try:
            s.close()
        except:
            pass

def get_public_ip():
    if not HAVE_REQUESTS:
        return "[i] requests library not installed, skipping public IP"
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except Exception as e:
        return f"[!] Error getting public IP: {e}"

def resolve_dns(domain="www.google.com"):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        return f"[!] Error resolving DNS: {e}"

def get_default_gateway():
    try:
        system = platform.system()
        if system == "Windows":
            output = subprocess.check_output("ipconfig", shell=True).decode()
            for line in output.splitlines():
                if "Default Gateway" in line and ":" in line:
                    gw = line.split(":")[-1].strip()
                    if gw:
                        return gw
        elif system in ("Linux", "Darwin"):
            output = subprocess.check_output("netstat -rn", shell=True).decode()
            for line in output.splitlines():
                if line.startswith("default") or line.startswith("0.0.0.0"):
                    return line.split()[1]
        return "[!] Gateway not found"
    except Exception as e:
        return f"[!] Error getting gateway: {e}"

def main():
    print("📡 IP & DNS Troubleshooter")
    print("-" * 40)
    print(f"Local IP Address          : {get_local_ip()}")
    print(f"Public IP Address         : {get_public_ip()}")
    print(f"DNS Resolution (google.com): {resolve_dns()}")
    print(f"Default Gateway           : {get_default_gateway()}")

if __name__ == "__main__":
    main()

