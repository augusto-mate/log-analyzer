# src/analyzer.py

from collections import Counter

# --- SSH ---
def detect_brute_force(events, threshold=5):
    """
    Detecta IPs com tentativas de login falhas acima do limite (threshold).
    """
    ips = [e["ip"] for e in events if e["event"] == "failed_login"]
    counter = Counter(ips)
    return {ip: count for ip, count in counter.items() if count >= threshold}


# --- Apache/Nginx ---
def detect_suspicious_http(events, threshold=3):
    """
    Detecta IPs com muitos erros HTTP (401, 403, 404, 500).
    """
    suspicious = {}
    for e in events:
        if e["event"] == "http_request" and e["status"] in [401, 403, 404, 500]:
            ip = e["ip"]
            suspicious[ip] = suspicious.get(ip, 0) + 1
    return {ip: count for ip, count in suspicious.items() if count >= threshold}
