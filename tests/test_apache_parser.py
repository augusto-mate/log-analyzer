# tests/test_apache_parser.py

import pytest
from src.parsers.apache_parser import parse_apache_log

def test_parse_apache_log(tmp_path):
    log_file = tmp_path / "apache.log"
    log_file.write_text(
        '192.168.1.20 - - [28/Jan/2026:10:15:32 +0000] "GET /login.php HTTP/1.1" 200 1234\n'
        '203.0.113.8 - - [28/Jan/2026:10:16:01 +0000] "GET /admin HTTP/1.1" 404 210\n'
    )
    events = parse_apache_log(str(log_file))
    assert len(events) == 2
    assert events[1]["status"] == 404
    assert events[1]["ip"] == "203.0.113.8"
