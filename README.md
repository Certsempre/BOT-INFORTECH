# Scraping para Emissão de Nota Fiscal de Serviço

Este projeto realiza o scraping do site da prefeitura de Patos-PB para emissão de notas fiscais de serviço. As informações necessárias para emissão são extraídas de uma planilha XLSX e enviadas ao site de forma automatizada.

---

## 🚀 Funcionalidades

- Carregamento de dados a partir de uma planilha XLSX.
- Automação do preenchimento dos formulários no site da prefeitura.
- Emissão de nota fiscal de serviço para cada entrada válida da planilha.

---

## 📋 Requisitos

- Python 3.8 ou superior.
- Bibliotecas Python:
  - `pandas`
  - `openpyxl`
  - `selenium`
  - `webdriver-manager`
- Navegador Google Chrome (ou outro compatível com Selenium).
- Driver do Selenium compatível com o navegador (pode ser configurado com o `webdriver-manager`).
