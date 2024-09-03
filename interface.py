import tkinter as tk
from tkinter import messagebox
from banco import criar_conta, remover_conta, atualizar_conta, consultar_conta, deposito, saque, transferencia
from dados import carregar_dados, salvar_dados

# Funções para a interface gráfica
def criar_conta_gui():
    numero = entry_numero.get()
    nome = entry_nome.get()
    saldo = entry_saldo.get()
    
    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return
    
    try:
        saldo = float(saldo)
        if saldo <= 0:
            messagebox.showerror("Erro", "O saldo deve ser positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Saldo inválido. Deve ser um número.")
        return
    
    criar_conta(numero, nome, saldo)
    messagebox.showinfo("Sucesso", f"Conta {numero} criada com sucesso!")

def remover_conta_gui():
    numero = entry_numero.get()
    
    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return
    
    if consultar_conta(numero):
        remover_conta(numero)
        messagebox.showinfo("Sucesso", f"Conta {numero} removida com sucesso!")
    else:
        messagebox.showerror("Erro", "Conta não encontrada.")

def atualizar_conta_gui():
    numero = entry_numero.get()
    nome = entry_nome.get()
    saldo = entry_saldo.get()
    
    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return
    
    saldo = saldo if saldo == "" else float(saldo)
    
    if saldo != "" and saldo <= 0:
        messagebox.showerror("Erro", "O saldo deve ser positivo.")
        return
    
    atualizar_conta(numero, nome, saldo)
    messagebox.showinfo("Sucesso", f"Conta {numero} atualizada com sucesso!")

def consultar_conta_gui():
    numero = entry_numero.get()
    
    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return
    
    conta = consultar_conta(numero)
    if conta:
        messagebox.showinfo("Informação", f"Conta {numero}: {conta}")
    else:
        messagebox.showerror("Erro", "Conta não encontrada.")

def deposito_gui():
    numero = entry_numero.get()
    valor = entry_saldo.get()
    
    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return
    
    try:
        valor = float(valor)
        if valor <= 0:
            messagebox.showerror("Erro", "O valor do depósito deve ser positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido. Deve ser um número.")
        return
    
    deposito(numero, valor)
    messagebox.showinfo("Sucesso", f"Depósito de R${valor} realizado com sucesso na conta {numero}!")

def saque_gui():
    numero = entry_numero.get()
    valor = entry_saldo.get()
    
    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return
    
    try:
        valor = float(valor)
        if valor <= 0:
            messagebox.showerror("Erro", "O valor do saque deve ser positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido. Deve ser um número.")
        return
    
    conta = consultar_conta(numero)
    if conta and conta['saldo'] >= valor:
        saque(numero, valor)
        messagebox.showinfo("Sucesso", f"Saque de R${valor} realizado com sucesso na conta {numero}!")
    else:
        messagebox.showerror("Erro", "Saldo insuficiente ou conta não encontrada.")

def transferencia_gui():
    numero_origem = entry_numero.get()
    numero_destino = entry_destino.get()
    valor = entry_saldo.get()
    
    if not numero_origem.isdigit() or not numero_destino.isdigit():
        messagebox.showerror("Erro", "Os números das contas devem conter apenas dígitos.")
        return
    
    try:
        valor = float(valor)
        if valor <= 0:
            messagebox.showerror("Erro", "O valor da transferência deve ser positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido. Deve ser um número.")
        return
    
    conta_origem = consultar_conta(numero_origem)
    if conta_origem and conta_origem['saldo'] >= valor and consultar_conta(numero_destino):
        transferencia(numero_origem, numero_destino, valor)
        messagebox.showinfo("Sucesso", f"Transferência de R${valor} da conta {numero_origem} para a conta {numero_destino} realizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Saldo insuficiente ou conta(s) não encontrada(s).")

def salvar_sair():
    salvar_dados()
    root.destroy()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Banco Digital Zen")

# Layout
tk.Label(root, text="Número da Conta:").grid(row=0, column=0)
entry_numero = tk.Entry(root)
entry_numero.grid(row=0, column=1)

tk.Label(root, text="Nome do Titular:").grid(row=1, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=1, column=1)

tk.Label(root, text="Saldo:").grid(row=2, column=0)
entry_saldo = tk.Entry(root)
entry_saldo.grid(row=2, column=1)

tk.Label(root, text="Número da Conta Destino:").grid(row=3, column=0)
entry_destino = tk.Entry(root)
entry_destino.grid(row=3, column=1)

tk.Button(root, text="Criar Conta", command=criar_conta_gui).grid(row=4, column=0, pady=5)
tk.Button(root, text="Remover Conta", command=remover_conta_gui).grid(row=4, column=1, pady=5)
tk.Button(root, text="Atualizar Conta", command=atualizar_conta_gui).grid(row=4, column=2, pady=5)
tk.Button(root, text="Consultar Conta", command=consultar_conta_gui).grid(row=4, column=3, pady=5)
tk.Button(root, text="Depósito", command=deposito_gui).grid(row=5, column=0, pady=5)
tk.Button(root, text="Saque", command=saque_gui).grid(row=5, column=1, pady=5)
tk.Button(root, text="Transferência", command=transferencia_gui).grid(row=5, column=2, pady=5)
tk.Button(root, text="Salvar e Sair", command=salvar_sair).grid(row=5, column=3, pady=5)

root.mainloop()
