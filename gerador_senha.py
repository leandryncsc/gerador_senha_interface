import tkinter as tk
from tkinter import messagebox
import string
import random

def gerar_senha():
    comprimento = int(entry_comprimento.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)

def copiar_para_area_de_transferencia():
    senha = entry_senha.get()
    janela.clipboard_clear()
    janela.clipboard_append(senha)
    messagebox.showinfo("Copiar", "Senha copiada para a área de transferência!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Gerador de Senha")

# Label e Entry para o comprimento da senha
label_comprimento = tk.Label(janela, text="Comprimento da senha:")
label_comprimento.pack(pady=5)

entry_comprimento = tk.Entry(janela)
entry_comprimento.pack(pady=5)

# Botão para gerar a senha
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack(pady=10)

# Entry para exibir a senha gerada
entry_senha = tk.Entry(janela, width=50)
entry_senha.pack(pady=5)

# Botão para copiar a senha para a área de transferência
botao_copiar = tk.Button(janela, text="Copiar Senha", command=copiar_para_area_de_transferencia)
botao_copiar.pack(pady=10)

# Iniciando o loop da interface gráfica
janela.mainloop()
