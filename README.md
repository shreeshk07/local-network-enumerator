# Local Network Enumerator

https://medium.com/@shreeshk08/building-a-local-network-enumerator-with-python-and-nmap-a3ca53708059

A Python-based tool that performs local network enumeration using Nmap.  
The project discovers reachable hosts, scans for open TCP ports, identifies running services, detects operating systems, and generates structured scan reports.

Built to strengthen practical understanding of network security fundamentals and ethical reconnaissance techniques.  
Developed and tested in a Linux virtual environment to safely practice real-world network scanning workflows.

---

## Phase 1 – Basic Network Enumeration

Phase 1 focuses on automating core network reconnaissance tasks using Python and Nmap.

### Features
- Host availability detection
- TCP port scanning
- Service and version detection
- JSON report generation
- Python-based automation of Nmap scans

---

## Phase 2 – Advanced Network Enumeration and Reporting

Phase 2 extends the project with deeper enumeration techniques and improved usability.

### Features
- Specific port scanning (e.g., port 80)
- Service version detection using `-sV`
- Operating system detection using `-O`
- Aggressive scanning using `-A`
- Automated execution of multiple scan types
- Report generation in JSON, TXT, and HTML formats
- Organized output structure for scans, reports, and logs

---

## Requirements
- Linux (Kali / Ubuntu)
- Python 3
- Nmap

Install Nmap if required:
```bash
sudo apt update
sudo apt install nmap -y
```

---

## Usage
```bash
python3 scanner.py
```

The script performs network scanning and automatically saves results in structured report files.

---

## Learning Outcomes
- Practical understanding of network reconnaissance techniques
- Hands-on experience with Nmap scan modes
- Automation of security tools using Python
- Ethical scanning practices in controlled environments
- Clear reporting and documentation of scan results

---

## Disclaimer
This project is intended strictly for educational purposes and must only be used on networks where explicit authorization has been granted.

---

## Author
Shreesh Kallihal  
MSc Cyber Security Student
