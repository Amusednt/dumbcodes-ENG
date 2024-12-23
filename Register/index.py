import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# Nome do arquivo Excel
FILE_NAME = 'cadastro.xlsx'

# Função para calcular a idade
def calcular_idade(data_inicial, data_final):
    data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
    data_final = datetime.strptime(data_final, '%d/%m/%Y')
    idade = data_final.year - data_inicial.year - ((data_final.month, data_final.day) < (data_inicial.month, data_inicial.day))
    return idade

# Função para cadastrar um novo registro
def cadastrar():
    data_inicial = entry_data_inicial.get()
    data_final = entry_data_final.get()
    nome = entry_nome.get()
    nacionalidade = entry_nacionalidade.get()
    comentarios = entry_comentarios.get()

    # Calcular a idade
    try:
        idade = calcular_idade(data_inicial, data_final)
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido. Use DD/MM/AAAA.")
        return

    registro = {
        'Data Inicial': data_inicial,
        'Data Final': data_final,
        'Nome Completo': nome,
        'Nacionalidade': nacionalidade,
        'Comentários': comentarios,
        'Idade': idade
    }

    try:
        df = pd.read_excel(FILE_NAME)
        df = df.append(registro, ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([registro])

    df.to_excel(FILE_NAME, index=False)
    messagebox.showinfo("Sucesso", "Registro cadastrado com sucesso!")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Cadastro")

# Frame para Cadastro
frame_cadastro = ttk.LabelFrame(root, text="Cadastro")
frame_cadastro.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(frame_cadastro, text="Data Inicial (DD/MM/AAAA):").grid(column=0, row=0)
entry_data_inicial = ttk.Entry(frame_cadastro)
entry_data_inicial.grid(column=1, row=0)

ttk.Label(frame_cadastro, text="Data Final (DD/MM/AAAA):").grid(column=0, row=1)
entry_data_final = ttk.Entry(frame_cadastro)
entry_data_final.grid(column=1, row=1)

ttk.Label(frame_cadastro, text="Nome Completo:").grid(column=0, row=2)
entry_nome = ttk.Entry(frame_cadastro)
entry_nome.grid(column=1, row=2)

ttk.Label(frame_cadastro, text="Nacionalidade:").grid(column=0, row=3)
entry_nacionalidade = ttk.Entry(frame_cadastro)
entry_nacionalidade.grid(column=1, row=3)

ttk.Label(frame_cadastro, text="Comentários:").grid(column=0, row=4)
entry_comentarios = ttk.Entry(frame_cadastro)
entry_comentarios.grid(column=1, row=4)

ttk.Button(frame_cadastro, text="Cadastrar", command=cadastrar).grid(columnspan=2, row=5)

# Iniciar a interface
root.mainloop()