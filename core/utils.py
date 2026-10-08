import sys
import datetime

# Terminal ANSI Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_banner():
    banner = f"""{CYAN}
    ==================================================
              PORT SCANNER & BANNER GRABBER           
                   [ Security Script ]                
    =================================================={RESET}
    """
    print(banner)

def print_status(message, level="info"):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    if level == "info":
        print(f"[{timestamp}] {CYAN}[INFO]{RESET} {message}")
    elif level == "success":
        print(f"[{timestamp}] {GREEN}[FOUND]{RESET} {message}")
    elif level == "error":
        print(f"[{timestamp}] {RED}[ERROR]{RESET} {message}")
    elif level == "warning":
        print(f"[{timestamp}] {YELLOW}[WARN]{RESET} {message}")