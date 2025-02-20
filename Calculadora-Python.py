#Calculadora by Leandro
import tkinter as tk
from tkinter import messagebox

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro"
    return a / b

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("⚠️ Erro", "🚫 Não é possível dividir por zero. Tente outra vez!")
        entrada.delete(0, tk.END)
    except Exception:
        messagebox.showerror("⚠️ Erro", "🤔 Expressão inválida. Verifique e tente novamente.")
        entrada.delete(0, tk.END)

def adicionar_valor(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

# Interface gráfica
janela = tk.Tk()
janela.title("🧮 Calculadora Interativa")

entrada = tk.Entry(janela, width=20, font=('Arial', 18), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, width=5, height=2, font=('Arial', 14), bg="#4CAF50", fg="white", command=calcular)
    else:
        botao = tk.Button(janela, text=texto, width=5, height=2, font=('Arial', 14), command=lambda t=texto: adicionar_valor(t))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

botao_limpar = tk.Button(janela, text="🗑️ C", width=5, height=2, font=('Arial', 14), bg="#f44336", fg="white", command=limpar)
botao_limpar.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# Mensagem de boas-vindas
messagebox.showinfo("👋 Olá!", "Bem-vindo à Calculadora Interativa! Divirta-se fazendo contas. 😉")

janela.mainloop()
