# src/main.py

from parsers.ssh_parser import parse_ssh_log
from parsers.apache_parser import parse_apache_log
from parsers.nginx_parser import parse_nginx_log
from analyzer import detect_brute_force, detect_suspicious_http
from report import generate_report, export_json, export_html, export_graph

def main():
    # SSH
    ssh_events = parse_ssh_log("sample_logs/ssh.log")
    suspicious_ssh = detect_brute_force(ssh_events)
    generate_report(suspicious_ssh, context="SSH")
    export_json(suspicious_ssh, filename="ssh_report.json")
    export_graph(suspicious_ssh, filename="ssh_graph.png", context="SSH")

    # Apache
    apache_events = parse_apache_log("sample_logs/apache.log")
    suspicious_apache = detect_suspicious_http(apache_events)
    generate_report(suspicious_apache, context="Apache")
    export_html(suspicious_apache, filename="apache_report.html", context="Apache")
    export_graph(suspicious_apache, filename="apache_graph.png", context="Apache")

    # Nginx
    nginx_events = parse_nginx_log("sample_logs/nginx.log")
    suspicious_nginx = detect_suspicious_http(nginx_events)
    generate_report(suspicious_nginx, context="Nginx")
    export_html(suspicious_nginx, filename="nginx_report.html", context="Nginx")
    export_graph(suspicious_nginx, filename="nginx_graph.png", context="Nginx")

if __name__ == "__main__":
    main()
