# Log Analyzer 🔍

[![CI/CD](https://github.com/augusto-mate/log-analyzer/actions/workflows/python-app.yml/badge.svg)](https://github.com/augusto-mate/log-analyzer/actions)
[![Coverage Status](https://img.shields.io/badge/coverage-90%25-brightgreen)](https://github.com/augusto-mate/log-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 

> This repository is also available in English.  
> See [README-en.md](README-en.md).

Ferramenta em Python para analisar logs de servidores (SSH, Apache/Nginx) e detectar padrões suspeitos, como tentativas de brute force ou acessos inválidos. Exporta relatórios em **JSON**, **HTML** e **gráficos PNG** para facilitar a visualização.

---

## 🚀 Funcionalidades 

- Containerização com **Docker**.
- Parser para **SSH**, **Apache** e **Nginx**.
- Detecção de **tentativas de brute force**.
- Pipeline de CI/CD com **GitHub Actions**.
- Identificação de **requisições HTTP suspeitas**.
- Testes automatizados com **pytest** e cobertura com **pytest-cov**.

## 📂 Estrutura

```code
src/                    # Código-fonte principal
tests/                  # Testes automatizados
sample_logs/            # Logs de exemplo
```

## 🛠️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/augusto-mate/log-analyzer.git
cd log-analyzer
pip install -r requirements.txt
```

## 🧪 Uso

Rode os testes:

```bash
python -m pytest -v
```

Execute o analisador:

```bash
python src/main.py
```

---

## 🛣️ Roadmap

- [x] SSH log parser + brute force detection
- [x] Apache log parser + erros HTTP
- [x] Exportação JSON/HTML/Gráficos
- [x] Testes automatizados com Pytest
- [x] CI/CD com GitHub Actions
- [x] Dockerfile para portabilidade
- [ ] Suporte avançado a Nginx
- [ ] Dashboard web interativo

---

## 👤 Autor

[**Augusto Mate**](https://github.com/augusto-mate/)  
Projetos de cibersegurança e automação de workflows.

## 📜 Licença

Este projeto está licenciado sob a **MIT License**.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### ✨ Inspiração

*"O prudente vê o perigo e busca refúgio, mas o inexperiente segue adiante e sofre as consequências."*  
— Provérbios 22:3
