from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Login import Login
import time
from Formatacao import Formatacao
import pandas as pd

lerPlanilha = pd.read_excel(Formatacao().get_caminhoNotas(), Formatacao().get_sheetnameNotas())

lerPlanilha['Nome'] = lerPlanilha['Nome'].astype(str)
lerPlanilha['CNPJ'] = lerPlanilha['CNPJ'].astype(str)
lerPlanilha['Email'] = lerPlanilha['Email'].astype(str)
lerPlanilha['CEP'] = lerPlanilha['CEP'].astype(str)
lerPlanilha['Logradouro'] = lerPlanilha['Logradouro'].astype(str)
lerPlanilha['Bairro'] = lerPlanilha['Bairro'].astype(str)
lerPlanilha['N'] = lerPlanilha['N'].astype(str)
lerPlanilha['Valor Nota'] = lerPlanilha['Valor Nota'].astype(str)

login = Login()
cnpj = str(login.get_cnpj())
senha = str(login.get_senha())

def voltar_inicio(browser):
    browser.get('https://patospb.webiss.com.br/inicio')
    time.sleep(2)


def fazer_login(browser, cnpj, senha):
    entrar_login = browser.find_element(By.XPATH, '//*[@id="Login"]').send_keys(cnpj)
    entrar_senha = browser.find_element(By.XPATH, '//*[@id="Senha"]').send_keys(senha)
    entrar_button = browser.find_element(By.XPATH, '//*[@id="botao-logar"]').click()

def botao_proximo(browser):
    while True:
        try:
            proximo_button = browser.find_element(By.ID, 'btnProximo')
            proximo_button.click()
            break
        except:
            continue

def navegar_ate_nota(browser):
    while True:
        try:
            issqn = browser.find_element(By.XPATH, '//*[@id="recurso-issqn"]').click()
            time.sleep(1)
            nfe = browser.find_element(By.XPATH, '//*[@id="recurso-issqn-nfse"]').click()
            time.sleep(1)
            criar_button = browser.find_element(By.XPATH, '//*[@id="recurso-issqn-nfse-criar"]').click()
            time.sleep(1)
            botao_proximo(browser)
            break
        except:
            continue

def colocar_cnpj(browser, lerPlanilha, indice):
    while True:
        try:
            caixa_cpf_cnpj = browser.find_element(By.XPATH, '//*[@id="tomador-numero-documento"]')
            caixa_cpf_cnpj.send_keys(lerPlanilha['CNPJ'][indice])
            break
        except:
            continue

def colocar_razao_social(browser, lerPlanilha, indice):
    espere = WebDriverWait(browser, 30)
    nome_razao_social = espere.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tomador-razao-social"]')), 'Elemento [razao social] Não ficou visível')

    valor_atual = nome_razao_social.get_attribute("value")
    if valor_atual.strip():  # Se já tiver um valor, não altera nada e retorna
        return
    
    nome_razao_social.click()
    nome_razao_social.clear()
    nome_razao_social.send_keys(lerPlanilha['Nome'][indice])

def colocar_e_mail(browser, lerPlanilha, indice):
    espere = WebDriverWait(browser, 30)
    e_mail = espere.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tomador-email"]')))
    time.sleep(2)
    valor_atual = e_mail.get_attribute("value")
    if valor_atual.strip():  # Se já tiver um valor, não altera nada e retorna
        return

    e_mail.click()
    e_mail.clear()
    e_mail.send_keys(lerPlanilha['Email'][indice])

def colocar_telefone(browser, lerPlanilha, indice):
    espere = WebDriverWait(browser, 30)
    telefone = espere.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tomador-telefone"]')))

    valor_atual = telefone.get_attribute("value")
    if valor_atual.strip():  # Se já tiver um valor, não altera nada e retorna
        return  

    telefone.click()
    telefone.clear()
    telefone.send_keys('(00) 0 0000-0000')

def colocar_cep(browser, lerPlanilha, indice):
    espere = WebDriverWait(browser, 30)
    cep = espere.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cepDoEndereco"]')))

    valor_atual = cep.get_attribute("value")
    if valor_atual.strip():  # Se já tiver um valor, não altera nada e retorna
        return  

    cep.click()
    cep.clear()
    cep.send_keys(lerPlanilha['CEP'][indice])
    time.sleep(1.5)

def colocar_logradouro(browser, lerPlanilha, indice):
    while True:
        logradouro = browser.find_element(By.XPATH, '//*[@id="nomeLogradouroDoEndereco"]')
        atributo_read_only = logradouro.get_attribute('readonly')

        if atributo_read_only is not None:
            print('Não da pra clicar no logradouro, pulando pra proxima função')
            colocar_bairro(browser, lerPlanilha, indice)
            break
        else:
            logradouro.click()
            time.sleep(1)
            logradouro.clear()
            logradouro.send_keys(lerPlanilha['Logradouro'][indice])
            break

def colocar_bairro(browser, lerPlanilha, indice):

    while True:
        bairro = browser.find_element(By.XPATH, '//*[@id="nomeBairroDoEndereco"]')
        atributo_read_only = bairro.get_attribute('readonly')

        if atributo_read_only is not None:
            print('Não da pra clicar no Bairro, pulando pra proxima função')
            colocar_numero(browser, lerPlanilha, indice)
            break
        else:
            bairro.click()
            time.sleep(1)
            bairro.clear()
            bairro.send_keys(lerPlanilha['Bairro'][indice])
            break

def colocar_numero(browser, lerPlanilha, indice):
    espere = WebDriverWait(browser, 30)
    numero = espere.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="numeroDoEndereco"]')))

    valor_atual = numero.get_attribute("value")
    if valor_atual.strip():  # Se já tiver um valor, não altera nada e retorna
        return  

    numero.click()
    numero.clear()
    numero.send_keys(lerPlanilha['N'][indice])

def dados_cliente(browser, lerPlanilha, indice):
    espere = WebDriverWait(browser, 30)
    colocar_cnpj(browser, lerPlanilha, indice)
    colocar_razao_social(browser, lerPlanilha, indice)
    colocar_e_mail(browser, lerPlanilha, indice)
    colocar_telefone(browser, lerPlanilha, indice)
    colocar_cep(browser, lerPlanilha, indice)
    colocar_logradouro(browser, lerPlanilha, indice)
    colocar_bairro(browser, lerPlanilha, indice)
    colocar_numero(browser, lerPlanilha, indice)
    botao_proximo(browser)

def tipo_atividade(browser):
    while True:
        try:
            time.sleep(2)
            tipo_atividade = browser.find_element(By.XPATH, '//*[@id="s2id_lista-de-servicos-prestador"]/a/span')
            tipo_atividade.click()
            time.sleep(1)
            input_tipo_atividade = browser.find_element(By.CSS_SELECTOR, '#select2-drop > div > input')
            print('a')
            input_tipo_atividade.send_keys('1402 - Assistência técnica.')
            input_tipo_atividade.send_keys(Keys.ENTER)
            # seleciona_tipo_atividade = browser.find_element(By.CSS_SELECTOR, '#select2-drop > ul > li:nth-child(3)')
            # seleciona_tipo_atividade.click()
            break
        except:
            continue

def escolher_cnae(browser):
    while True:
        try:
            cnae = browser.find_element(By.CSS_SELECTOR, '#s2id_CnaeAtividade_Id > a')
            cnae.click()
            time.sleep(1)
            cnae.send_keys('9511800 - Reparação e manutenção de computadores e de equipamentos periféricos')
            cnae.send_keys(Keys.ENTER)
            # seleciona_cnae = browser.find_element(By.CSS_SELECTOR, '#select2-drop > ul > li.select2-results-dept-0.select2-result.select2-result-selectable.select2-highlighted')
            # seleciona_cnae.click()
            break
        except:
            continue

def descricao_servicos(browser):
    tipo_atividade(browser)
    escolher_cnae(browser)
    descricao_detalhada = browser.find_element(By.XPATH, '//*[@id="discriminacao"]').send_keys('Referente a compra do TEF.')
    botao_proximo(browser)


def colocar_valor(browser, indice):
    espere = WebDriverWait(browser, 30)
    valor = str(lerPlanilha['Valor Nota'][indice])
    #valor += '0'
    campo_valor = espere.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="valores-servico"]')))
    campo_valor.click()
    campo_valor.clear()
    campo_valor.send_keys(valor)

def validar_valor(browser, indice):
    while True:
        try:
            alicota = browser.find_element(By.XPATH, '//*[@id="valores-documento-fiscal-aliquota"]')
            alicota.click()

            base_de_calculo = browser.find_element(By.XPATH, '//*[@id="valores-documento-fiscal-valor-base-calculo"]')

            a = base_de_calculo.text
            
            if a == '120,00':
                print(f'Valor correto! {a}')
                break
            else:
                print('Valor errado, realizando ajuste')
                colocar_valor(browser, indice)
        except:
            continue

def valor_servico(browser, indice):
    colocar_valor(browser, indice)
    validar_valor(browser, indice)

    
def salvar_rascunho(browser):
    salvar = browser.find_element(By.XPATH, '//*[@id="wizard-nota-fiscal"]/div/div[2]/div[2]/div/div/a[3]').click()
    
def emitir(browser):
    emissao = browser.find_element(By.XPATH, '//*[@id="botao-emitir-nota-fiscal"]').click()

def cliente_emitido(lerPlanilha,indice):
    
    print(f"{indice} - Nota fiscal emitida para o cliente {lerPlanilha['Nome'][indice]}")
    