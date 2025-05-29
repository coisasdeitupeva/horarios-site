import requests
from bs4 import BeautifulSoup

url = "https://viaitupeva.com.br/horarios"
resposta = requests.get(url)

# Força o encoding correto
resposta.encoding = 'utf-8'

resposta.raise_for_status()

soup = BeautifulSoup(resposta.text, "html.parser")

tabelas = soup.find_all("table")

if tabelas:
    html_tabelas = "".join(str(tabela) for tabela in tabelas)

    html_completo = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8" />
        <title>Horários de Ônibus</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background: #fff;
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 30px;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: center;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Horários de Ônibus - Todas as Tabelas</h1>
        {html_tabelas}
    </body>
    </html>
    """

    with open("horarios_todas_tabelas.html", "w", encoding="utf-8") as f:
        f.write(html_completo)

    print("✅ Arquivo horarios_todas_tabelas.html gerado com sucesso!")
else:
    print("❌ Não foram encontradas tabelas na página.")

    with open("../index.html", "w", encoding="utf-8") as f:
        f.write(html_formatado)

