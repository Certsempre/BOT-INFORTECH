import customtkinter as ctk
import subprocess
import sys

import pandas as pd

# Função para executar a RPA
def executar_rpa():
    caminho_planilha = input_caminho_planilha.get()
    pagina_planilha = input_pagina_planilha.get()
    qtd_notas = input_qtd_notas_planilha.get()

    if not caminho_planilha or not pagina_planilha or not qtd_notas.isdigit():
        print("Por favor, preencha todos os campos corretamente.")
        return

    # Chamando a função que inicia a RPA
    iniciar_rpa(caminho_planilha, pagina_planilha, int(qtd_notas))

# Função para iniciar o script principal da RPA
def iniciar_rpa(caminho, pagina, quantidade):
    subprocess.run([sys.executable, "main.py", caminho, pagina, str(quantidade)])

#_________Configuração da Interface_________
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("Bot - Emissão de NFSe da Infortech")
app.geometry('500x500')

# Mensagem de boas-vindas
bem_vindo = ctk.CTkLabel(app, text='Bem-Vindo')
bem_vindo.pack(pady=40)

#_________________Caminho Planilha____________________________
label_caminho_planilha = ctk.CTkLabel(app, text='Caminho da Planilha')
label_caminho_planilha.pack(pady=10)

input_caminho_planilha = ctk.CTkEntry(app, placeholder_text="Digite o caminho da planilha")
input_caminho_planilha.pack(pady=1)

#________________Página Planilha_______________________________
label_pagina_planilha = ctk.CTkLabel(app, text='Página da Planilha')
label_pagina_planilha.pack(pady=10)

input_pagina_planilha = ctk.CTkEntry(app, placeholder_text="Digite a página da planilha")
input_pagina_planilha.pack(pady=1)

#________________QTD de Notas que Deseja Emitir________________
label_qtd_notas_planilha = ctk.CTkLabel(app, text='Quantidade de Notas')
label_qtd_notas_planilha.pack(pady=10)

input_qtd_notas_planilha = ctk.CTkEntry(app, placeholder_text="Digite a quantidade de notas que deseja emitir")
input_qtd_notas_planilha.pack(pady=1)

#________________Botão Enviar__________________________________
botao_executar = ctk.CTkButton(app, text='Enviar', command=executar_rpa)
botao_executar.pack(pady=30)

# Executa o loop da interface
app.mainloop()
