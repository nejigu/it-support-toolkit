import subprocess
import platform
import socket

def check_connection():
    print("Checking internet connection...\n")
    try:
        host = socket.gethostbyname("www.google.com")
        
        # Detect OS
        param = "-n" if platform.system().lower() == "windows" else "-c"

        # Ping the host
        result = subprocess.run(
            ["ping", param, "4", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode == 0:
            print("\n✅ Internet connection is working.")
        else:
            print("\n❌ Internet connection seems to be down.")

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

check_connection()


