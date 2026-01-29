# src/parsers/ssh_parser.py

import re

def parse_ssh_log(file_path):
    events = []
    with open(file_path, "r") as f:
        for line in f:
            match = re.search(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                events.append({"event": "failed_login", "ip": match.group(1)})
    return events
