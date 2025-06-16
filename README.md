# 🧰 IT Support Toolkit

Scripts for automating common IT support tasks. Great for entry-level IT support, helpdesk, and general system diagnostics.

---

## 📡 Script: Network Checker (`network_checker.py`)

### 🔍 What It Does
This script checks for an active internet connection by:
- Resolving the IP address of www.google.com
- Pinging it using your operating system's native ping tool
- Reporting whether the internet connection is working or not

### 🖥️ Works On
- ✅ macOS
- ✅ Windows
- ✅ Linux

The script automatically detects your operating system and uses the correct ping command.

### ⚙️ How to Use

1. Make sure Python 3 is installed:
   - On macOS: run `python3 --version` in Terminal  
   - On Windows: run `python --version` in Command Prompt or PowerShell

2. Open Terminal or Command Prompt.

3. Navigate to the folder where the script is saved:
   ```bash
   cd path/to/your/IT-Support-Toolkit
python3 network_checker.py    # or `python` on Windows

🖥️ Script: System Info Reporter (system_info_reporter.py)
🔍 What It Does
This script gathers key system information such as:

Hostname and IP address

Operating system and version

CPU, RAM, and disk usage

It displays this info in a clean format and optionally saves it to a timestamped .txt report.

🖥️ Works On
✅ macOS

✅ Windows

✅ Linux

⚙️ How to Use
Install the required library:

pip install psutil
Run the script:

python system_info_reporter.py   # or `python3` on macOS
You’ll be prompted to save the output as a report file if desired.

# `ip_dns_troubleshooter.py`

# 📡 IP & DNS Troubleshooter

A simple, cross-platform Python script to perform basic network diagnostics in one go.

---

## 🔍 What It Does

- **Local IP Address**  
  Retrieves the machine’s LAN IP (e.g. `192.168.x.x`).

- **Public IP Address**  
  Looks up your public Internet IP via `api.ipify.org`.  
  If the `requests` library isn’t installed, the script will skip this step and note it in the output.

- **DNS Resolution**  
  Resolves a domain name (default: `www.google.com`) to its IP address.

- **Default Gateway**  
  Detects your network’s default gateway on Windows, macOS (Darwin) or Linux.

---

## 🖥️ Supported Platforms

- ✅ Windows  
- ✅ macOS (Darwin)  
- ✅ Linux  

---

## ⚙️ Requirements

- **Python 3**  
- *(Optional)* `requests` library (for public IP).  
  Install with:
  ```bash
  pip install requests
python ip_dns_troubleshooter.py    # or `python3` on macOS/Linux


👤 Author
Created by Nahom Ejigu-Abegaz

