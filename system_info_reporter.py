import platform
import socket
import psutil
from datetime import datetime

def get_system_info():
    info = {}

    info["Hostname"] = socket.gethostname()
    info["IP Address"] = socket.gethostbyname(info["Hostname"])
    info["OS"] = platform.system()
    info["OS Version"] = platform.version()
    info["Architecture"] = platform.machine()
    info["Processor"] = platform.processor()
    info["CPU Cores"] = psutil.cpu_count(logical=True)
    info["RAM (GB)"] = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    info["Disk Total (GB)"] = round(psutil.disk_usage('/').total / (1024 ** 3), 2)
    info["Disk Free (GB)"] = round(psutil.disk_usage('/').free / (1024 ** 3), 2)

    return info

def display_info(info):
    print("\n🖥️ SYSTEM INFORMATION REPORT\n" + "-"*35)
    for key, value in info.items():
        print(f"{key}: {value}")
    print("-"*35)

def save_to_file(info):
    filename = f"system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as f:
        f.write("SYSTEM INFORMATION REPORT\n")
        f.write("-" * 35 + "\n")
        for key, value in info.items():
            f.write(f"{key}: {value}\n")
        f.write("-" * 35 + "\n")
    print(f"\n📁 Report saved as: {filename}")

# Run the script
info = get_system_info()
display_info(info)

save_choice = input("\n💾 Do you want to save this report to a file? (y/n): ").lower()
if save_choice == 'y':
    save_to_file(info)
else:
    print("Report not saved.")
