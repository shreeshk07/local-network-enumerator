import nmap
import json
from datetime import datetime
import os

def scan_host(target):
    scanner = nmap.PortScanner()

    print(f"[*] Scanning target: {target}")
    scanner.scan(hosts=target, arguments="-sS -sV")

    results = {}

    if target in scanner.all_hosts():
        results["host"] = target
        results["state"] = scanner[target].state()
        results["protocols"] = {}

        for proto in scanner[target].all_protocols():
            results["protocols"][proto] = {}
            ports = scanner[target][proto].keys()

            for port in ports:
                service = scanner[target][proto][port]
                results["protocols"][proto][port] = {
                    "state": service["state"],
                    "service": service.get("name"),
                    "product": service.get("product"),
                    "version": service.get("version")
                }

    return results

def save_results(data):
    if not os.path.exists("output"):
        os.makedirs("output")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output/scan_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] Results saved to {filename}")

def main():
    print("=== Local Network Enumerator using Nmap ===")
    target = input("Enter target IP (example: 127.0.0.1): ")

    results = scan_host(target)

    if results:
        print(f"[+] Host is up: {results['host']}")
        for proto, ports in results["protocols"].items():
            print(f"Protocol: {proto}")
            for port, info in ports.items():
                print(f"  Port {port}: {info['state']} ({info['service']})")
        save_results(results)
    else:
        print("[-] Host seems down or unreachable")

if __name__ == "__main__":
    main()

