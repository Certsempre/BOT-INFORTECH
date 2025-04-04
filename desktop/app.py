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

ctk.set_default_color_theme('blue')  # Tema azul

app = ctk.CTk()
app.title("Bot - Emissão de NFSe da Infortech")
app.geometry('500x450')
app.resizable(False, False) # Usuario não poderá alterar o tamanho da janela do app 

# Criando um frame para organizar os elementos
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

# Mensagem de boas-vindas
bem_vindo = ctk.CTkLabel(frame, text='Bem-Vindo', font=("Arial", 18, "bold"))
bem_vindo.pack(pady=10)

#_________________Caminho Planilha____________________________
label_caminho_planilha = ctk.CTkLabel(frame, text='Caminho da Planilha', font=("Arial", 14))
label_caminho_planilha.pack(pady=(5, 2))

input_caminho_planilha = ctk.CTkEntry(frame, placeholder_text="Digite o caminho da planilha",  width=300, height=35, corner_radius=8)
input_caminho_planilha.pack(pady=5)

#________________Página Planilha_______________________________
label_pagina_planilha = ctk.CTkLabel(frame, text='Página da Planilha', font=("Arial", 14))
label_pagina_planilha.pack(pady=(5, 2))

input_pagina_planilha = ctk.CTkEntry(frame, placeholder_text="Digite a página da planilha", width=300, height=35, corner_radius=8)
input_pagina_planilha.pack(pady=5)

#________________QTD de Notas que Deseja Emitir________________
label_qtd_notas_planilha = ctk.CTkLabel(frame, text='Quantidade de Notas', font=("Arial", 14))
label_qtd_notas_planilha.pack(pady=(5, 2))

input_qtd_notas_planilha = ctk.CTkEntry(frame, placeholder_text="Digite a quantidade de notas que deseja emitir", width=300, height=35, corner_radius=8)
input_qtd_notas_planilha.pack(pady=5)

#________________Botão Enviar__________________________________
botao_executar = ctk.CTkButton(frame, text='Enviar', command=executar_rpa, width=200, height=40, font=("Arial", 14, "bold"))
botao_executar.pack(pady=20)

# Executa o loop da interface
app.mainloop()
