import pandas as pd
from Login import Login
from navegacao import *
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
browser = webdriver.Chrome(options=chrome_options)

browser.maximize_window()

login = Login()
cnpj = str(login.get_cnpj())
senha = str(login.get_senha())

lerPlanilha = pd.read_excel(Formatacao().get_caminhoNotas(), Formatacao().get_sheetnameNotas())

browser.get('https://patospb.webiss.com.br/')

fazer_login(browser, cnpj, senha)

for indice in range(min(94, len(lerPlanilha))):  
    voltar_inicio(browser)
    navegar_ate_nota(browser)
    dados_cliente(browser, lerPlanilha, indice)
    descricao_servicos(browser)
    valor_servico(browser, indice)
    salvar_rascunho(browser)
    emitir(browser)
    cliente_emitido(lerPlanilha, indice)





