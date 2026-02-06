import nmap
import argparse
import json
import os
import logging
from datetime import datetime

os.makedirs("scans", exist_ok=True)
os.makedirs("reports", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

scanner = nmap.PortScanner()

def generate_reports(results, target, arguments):
    scan_time = datetime.now()

    with open("reports/scan_report.txt", "w") as txt:
        txt.write("Local Network Enumeration Report\n")
        txt.write("=" * 45 + "\n")
        txt.write(f"Target      : {target}\n")
        txt.write(f"Arguments   : {arguments}\n")
        txt.write(f"Scan Time   : {scan_time}\n\n")

        for host in results["scan"]:
            txt.write(f"Host: {host}\n")
            txt.write(f"State: {results['scan'][host]['status']['state']}\n")

            if "tcp" in results["scan"][host]:
                for port, info in results["scan"][host]["tcp"].items():
                    txt.write(
                        f"  Port {port} | "
                        f"{info['state']} | "
                        f"{info.get('name','N/A')} | "
                        f"{info.get('version','N/A')}\n"
                    )
            txt.write("\n")

    with open("reports/scan_report.html", "w") as html:
        html.write("<html><head><title>Scan Report</title></head><body>")
        html.write("<h1>Local Network Enumeration Report</h1>")
        html.write(f"<p><b>Target:</b> {target}</p>")
        html.write(f"<p><b>Arguments:</b> {arguments}</p>")
        html.write(f"<p><b>Scan Time:</b> {scan_time}</p>")

        for host in results["scan"]:
            html.write(f"<h2>Host: {host}</h2>")
            html.write(f"<p>Status: {results['scan'][host]['status']['state']}</p>")

            if "tcp" in results["scan"][host]:
                html.write("<ul>")
                for port, info in results["scan"][host]["tcp"].items():
                    html.write(
                        f"<li>Port {port} | "
                        f"{info['state']} | "
                        f"{info.get('name','N/A')} | "
                        f"{info.get('version','N/A')}</li>"
                    )
                html.write("</ul>")

        html.write("</body></html>")

def save_json(results):
    with open("scans/scan_results.json", "w") as f:
        json.dump(results, f, indent=4)

def run_scan(target, arguments):
    logging.info(f"Scan started on {target} with arguments: {arguments}")
    print(f"[+] Scanning target: {target}")

    scanner.scan(target, arguments=arguments)
    results = scanner._scan_result

    save_json(results)
    generate_reports(results, target, arguments)

    logging.info("Scan completed successfully")
    print("[✓] Scan completed")
    print("[✓] Results saved")

def main():
    parser = argparse.ArgumentParser(description="Local Network Enumerator - Phase 2")

    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-p", "--port")
    parser.add_argument("-sV", "--service", action="store_true")
    parser.add_argument("-O", "--osdetect", action="store_true")
    parser.add_argument("-A", "--aggressive", action="store_true")
    parser.add_argument("-T", "--timing", default="3")

    args = parser.parse_args()

    scan_args = f"-T{args.timing}"

    if args.port:
        scan_args += f" -p {args.port}"
    if args.service:
        scan_args += " -sV"
    if args.osdetect:
        scan_args += " -O"
    if args.aggressive:
        scan_args += " -A"

    run_scan(args.target, scan_args)

if __name__ == "__main__":
    main()

