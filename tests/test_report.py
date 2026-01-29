# tests/test_report.py

import pytest
import os
from src.report import export_json, export_html, export_graph

def test_export_json(tmp_path):
    data = {"192.168.1.10": 5}
    filename = tmp_path / "report.json"
    export_json(data, filename=str(filename))
    assert filename.exists()
    assert '"192.168.1.10": 5' in filename.read_text()

def test_export_html(tmp_path):
    data = {"203.0.113.8": 3}
    filename = tmp_path / "report.html"
    export_html(data, filename=str(filename), context="Apache")
    assert filename.exists()
    assert "<h1>Relatório Apache</h1>" in filename.read_text()

def test_export_graph(tmp_path):
    data = {"192.168.1.10": 5}
    filename = tmp_path / "report.png"
    export_graph(data, filename=str(filename), context="SSH")
    assert filename.exists()
    assert os.path.getsize(filename) > 0
