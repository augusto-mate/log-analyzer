# Log Analyzer 🔍

[![CI/CD](https://github.com/augusto-mate/log-analyzer/actions/workflows/python-app.yml/badge.svg)](https://github.com/augusto-mate/log-analyzer/actions)
[![Coverage Status](https://img.shields.io/badge/coverage-90%25-brightgreen)](https://github.com/augusto-mate/log-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 

> Este repositório também está disponível em Português.  
> Consulte [README.md](README.md).

Python tool for analyzing server logs (SSH, Apache/Nginx) and detecting suspicious patterns, such as brute force attempts or invalid accesses. Exports reports in **JSON**, **HTML**, and **PNG graphs** for easy viewing.

---

## 🚀 Features 

- Containerization with **Docker**.
- Parser for **SSH**, **Apache**, and **Nginx**.
- Detection of **brute force attempts**.
- CI/CD pipeline with **GitHub Actions**.
- Identification of **suspicious HTTP requests**.
- Automated testing with **pytest** and coverage with **pytest-cov**.

## 📂 Structure

```code
src/                    # Main source code
tests/                  # Automated tests
sample_logs/            # Sample logs
```

## 🛠️ Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/augusto-mate/log-analyzer.git
cd log-analyzer
pip install -r requirements.txt
```

## 🧪 Usage

Run the tests:

```bash
python -m pytest -v
```

Run the analyzer:

```bash
python src/main.py
```

---

## 🛣️ Roadmap

- [x] SSH log parser + brute force detection
- [x] Apache log parser + HTTP errors
- [x] JSON/HTML/Graphics export
- [x] Automated testing with Pytest
- [x] CI/CD with GitHub Actions
- [x] Dockerfile for portability
- [ ] Advanced Nginx support
- [ ] Interactive web dashboard

---

## 👤 Author

[**Augusto Mate**](https://github.com/augusto-mate/)  
Cybersecurity and workflow automation projects.

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

### ✨ Inspiration

*“A prudent man foreseeth the evil, and hideth himself: but the simple pass on, and are punished.”*  
— Proverbs 22:3
