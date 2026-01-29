# src/parsers/nginx_parser.py

import re

def parse_nginx_log(file_path):
    events = []
    with open(file_path, "r") as f:
        for line in f:
            match = re.search(r'(\d+\.\d+\.\d+\.\d+).*"(\w+) (.*?) HTTP.*" (\d+)', line)
            if match:
                ip = match.group(1)
                method = match.group(2)
                endpoint = match.group(3)
                status = int(match.group(4))
                events.append({
                    "event": "http_request",
                    "ip": ip,
                    "method": method,
                    "endpoint": endpoint,
                    "status": status
                })
    return events
