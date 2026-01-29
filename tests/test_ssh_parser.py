# tests/test_ssh_parser.py

import pytest
from src.parsers.ssh_parser import parse_ssh_log

def test_parse_ssh_log(tmp_path):
    # Criar log temporário
    log_file = tmp_path / "ssh.log"
    log_file.write_text(
        "Jan 28 10:15:32 server sshd[12345]: Failed password for root from 192.168.1.10 port 54321 ssh2\n"
        "Jan 28 10:15:35 server sshd[12345]: Failed password for root from 192.168.1.10 port 54321 ssh2\n"
    )
    events = parse_ssh_log(str(log_file))
    assert len(events) == 2
    assert events[0]["event"] == "failed_login"
    assert events[0]["ip"] == "192.168.1.10"
