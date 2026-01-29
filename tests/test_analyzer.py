# tests/test_analyzer.py

import pytest
from src.analyzer import detect_brute_force, detect_suspicious_http

def test_detect_brute_force():
    events = [
        {"event": "failed_login", "ip": "192.168.1.10"},
        {"event": "failed_login", "ip": "192.168.1.10"},
        {"event": "failed_login", "ip": "192.168.1.10"},
        {"event": "failed_login", "ip": "192.168.1.10"},
        {"event": "failed_login", "ip": "192.168.1.10"},
    ]
    result = detect_brute_force(events, threshold=5)
    assert "192.168.1.10" in result
    assert result["192.168.1.10"] == 5

def test_detect_suspicious_http():
    events = [
        {"event": "http_request", "ip": "203.0.113.8", "status": 404},
        {"event": "http_request", "ip": "203.0.113.8", "status": 404},
        {"event": "http_request", "ip": "203.0.113.8", "status": 404},
    ]
    result = detect_suspicious_http(events, threshold=3)
    assert "203.0.113.8" in result
    assert result["203.0.113.8"] == 3
