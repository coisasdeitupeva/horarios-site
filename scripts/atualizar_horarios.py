import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

url = "https://viaitupeva.com.br/horarios"
resposta = requests.get(url)

# Força o encoding correto
resposta.encoding = 'utf-8'

resposta.raise_for_status()

soup = BeautifulSoup(resposta.text, "html.parser")

tabelas = soup.find_all("table")

if tabelas:
    html_tabelas = "".join(str(tabela) for tabela in tabelas)

    # Ajusta o horário para o fuso de São Paulo (UTC-3)
    fuso_sp = pytz.timezone("America/Sao_Paulo")
    agora = datetime.now(fuso_sp).strftime("%d/%m/%Y às %H:%M")

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
            .atualizacao {{
                font-size: 14px;
                color: #777;
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Quadro de Horários Via Itupeva</h1>
        <p class="atualizacao">Última atualização: {agora}</p>
        {html_tabelas}
    </body>
    </html>
    """

    with open("horarios_todas_tabelas.html", "w", encoding="utf-8") as f:
        f.write(html_completo)

    print("✅ Arquivo horarios_todas_tabelas.html gerado com sucesso!")
else:
    print("❌ Não foram encontradas tabelas na página.")
