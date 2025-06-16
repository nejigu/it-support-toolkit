# it-support-toolkit
Scripts for automating common IT support tasks
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

---

## ⚙️ How to Use

1. Make sure Python 3 is installed:
    - On macOS: run ‘python3 --version’ in Terminal
    - On Windows: run ‘python --version’ in Command Prompt or PowerShell

2. Open Terminal or Command Prompt.

3. Navigate to the folder where the script is saved:
```bash
cd path/to/your/IT-Support-Toolkit

---

## 🖥️ Script: System Info Reporter (`system_info_reporter.py`)

### 🔍 What It Does
This script gathers key system information such as:
- Hostname and IP address
- Operating system and version
- CPU, RAM, and disk usage

It displays this info in a clean format and optionally saves it to a timestamped `.txt` report.

### 🖥️ Works On
- ✅ macOS
- ✅ Windows
- ✅ Linux

### ⚙️ How to Use

1. Install the required library:
```bash
pip install psutil

python system_info_reporter.py or python3 on macOS

## 👤 Author

Created by **Nahom Ejigu-Abegaz**  
[Connect with me on LinkedIn](https://www.linkedin.com/in/nejigu-abegaz)
