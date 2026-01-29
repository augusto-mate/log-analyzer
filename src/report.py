# src/report.py

import json
import matplotlib.pyplot as plt

def generate_report(suspicious_ips, context="SSH"):
    print(f"=== Relatório {context} ===")
    if not suspicious_ips:
        print("Nenhum padrão suspeito detectado.")
    else:
        for ip, count in suspicious_ips.items():
            print(f"IP: {ip} - Ocorrências suspeitas: {count}")


def export_json(suspicious_ips, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(suspicious_ips, f, indent=4)
    print(f"[+] Relatório JSON exportado para {filename}")


def export_html(suspicious_ips, filename="report.html", context="SSH"):
    with open(filename, "w") as f:
        f.write("<html><head><title>Relatório de Segurança</title></head><body>")
        f.write(f"<h1>Relatório {context}</h1>")
        if not suspicious_ips:
            f.write("<p>Nenhum padrão suspeito detectado.</p>")
        else:
            f.write("<ul>")
            for ip, count in suspicious_ips.items():
                f.write(f"<li>IP: {ip} - Ocorrências suspeitas: {count}</li>")
            f.write("</ul>")
        f.write("</body></html>")
    print(f"[+] Relatório HTML exportado para {filename}")


def export_graph(suspicious_ips, filename="report.png", context="SSH"):
    if not suspicious_ips:
        print("Nenhum dado para gerar gráfico.")
        return
    ips = list(suspicious_ips.keys())
    counts = list(suspicious_ips.values())
    plt.figure(figsize=(8, 5))
    plt.bar(ips, counts, color="red")
    plt.title(f"Tentativas suspeitas - {context}")
    plt.xlabel("IP")
    plt.ylabel("Ocorrências")
    plt.savefig(filename)
    plt.close()
    print(f"[+] Gráfico exportado para {filename}")
