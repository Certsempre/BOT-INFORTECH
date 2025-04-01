import sys
import pandas as pd
from Login import Login
from navegacao import *
from Formatacao import Formatacao
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Pegando os argumentos da interface
caminho_planilha = sys.argv[1]
pagina_planilha = sys.argv[2]
quantidade_notas = int(sys.argv[3])

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
browser = webdriver.Chrome(options=chrome_options)

browser.maximize_window()

login = Login()
cnpj = str(login.get_cnpj())
senha = str(login.get_senha())

lerPlanilha = pd.read_excel(caminho_planilha, pagina_planilha)

browser.get('https://patospb.webiss.com.br/')

fazer_login(browser, cnpj, senha)

for indice in range(min(quantidade_notas, len(lerPlanilha))):  
    voltar_inicio(browser)
    navegar_ate_nota(browser)
    dados_cliente(browser, lerPlanilha, indice)
    descricao_servicos(browser)
    valor_servico(browser, indice)
    salvar_rascunho(browser)
    emitir(browser)
    cliente_emitido(lerPlanilha, indice)
