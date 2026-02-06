# Local Network Enumerator

A Python-based tool that performs local network enumeration using Nmap.  
The project discovers reachable hosts, scans for open TCP ports, identifies running services, detects operating systems, and saves the results as structured reports.

Built for learning network security fundamentals and ethical scanning.  
Tested in a Linux virtual environment to practice ethical network scanning and security fundamentals.

---

## Phase 1 – Basic Network Enumeration

### Features
- Host availability check
- TCP port scanning
- Service and version detection
- JSON report generation

---

## Phase 2 – Advanced Network Enumeration

### Features
- Specific port scanning (e.g., port 80)
- Service version detection using `-sV`
- Operating system detection using `-O`
- Aggressive scanning using `-A`
- Automated execution of multiple scan types
- Report generation in JSON, TXT, and HTML formats
- Organized output directories for scans, reports, and logs

---

## Requirements
- Linux (Kali / Ubuntu)
- Python 3
- Nmap

---

## Usage
```bash
python3 scanner.py
```

---

## Disclaimer
This project is intended strictly for educational purposes and must only be used on networks where proper authorization has been granted.

---

## Author
Shreesh Kallihal
