import socket
from concurrent.futures import ThreadPoolExecutor
from core.utils import print_status

def grab_banner(target_ip, port):
    """Attempt to grab the banner/service name from an open port."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((target_ip, port))
        
        # Send a generic request to trigger a response banner
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        
        # Clean multi-line banners to single line
        if banner:
            first_line = banner.split('\n')[0]
            return first_line[:50]
        return "No banner responded"
    except Exception:
        return "Unknown Service"

def scan_port(target_ip, port):
    """Scan a single port using TCP socket connection."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5) # Fast timeout for efficiency
        
        result = s.connect_ex((target_ip, port))
        s.close()
        
        if result == 0:
            banner = grab_banner(target_ip, port)
            print_status(f"Port {port:<5} | OPEN | Service: {banner}", level="success")
            return port, banner
    except Exception as e:
        pass
    return None

def start_scan(target_host, start_port=1, end_port=1024, max_threads=50):
    """Orchestrate the multi-threaded port scan."""
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print_status(f"Could not resolve hostname '{target_host}'", level="error")
        return

    print_status(f"Target: {target_host} ({target_ip})", level="info")
    print_status(f"Scanning ports {start_port} to {end_port} using {max_threads} threads...", level="info")
    print("-" * 60)

    open_ports = []
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            executor.submit(scan_port, target_ip, port) 
            for port in range(start_port, end_port + 1)
        ]
        for future in futures:
            res = future.result()
            if res:
                open_ports.append(res)

    print("-" * 60)
    print_status(f"Scan Complete. Found {len(open_ports)} open port(s).", level="info")