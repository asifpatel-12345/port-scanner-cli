import argparse
from core.utils import print_banner, print_status
from core.scanner import start_scan

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Multi-Threaded CLI Port Scanner & Banner Grabber")
    parser.add_argument("-t", "--target", required=True, help="Target IP address or domain (e.g., scanme.nmap.org)")
    parser.add_argument("-sp", "--start-port", type=int, default=1, help="Start port range (Default: 1)")
    parser.add_argument("-ep", "--end-port", type=int, default=1024, help="End port range (Default: 1024)")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Number of concurrent threads (Default: 50)")

    args = parser.parse_args()

    try:
        start_scan(
            target_host=args.target,
            start_port=args.start_port,
            end_port=args.end_port,
            max_threads=args.workers
        )
    except KeyboardInterrupt:
        print("\n")
        print_status("Scan aborted by user.", level="warning")

if __name__ == "__main__":
    main()