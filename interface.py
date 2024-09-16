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



# Criação da janela
root = tk.Tk()

# Definir título da janela
root.title("Banco Digital Zen")

# Label título centralizado
label_titulo = tk.Label(root, text="Banco Digital Zen", font=("Helvetica", 30, "bold"))
label_titulo.pack(pady=20)  # Centraliza 
# Label subtítulo
label_titulo = tk.Label(root, text="Cadastro de Clientes", font=("Helvetica", 24, "bold"),
                        bg="black", fg="white", borderwidth=2, relief="solid")
label_titulo.pack(pady=(10, 5))

#  tela cheia
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")


# Layout
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Número da Conta:", font=("Helvetica", 12)).grid(row=0, column=0, padx=20, pady=10)
entry_numero = tk.Entry(frame, width=30)
entry_numero.grid(row=0, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Nome do Titular:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame, width=30)
entry_nome.grid(row=1, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Saldo:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5)
entry_saldo = tk.Entry(frame, width=30)
entry_saldo.grid(row=2, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Número da Conta Destino:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5)
entry_destino = tk.Entry(frame, width=30)
entry_destino.grid(row=3, column=1, padx=10, pady=5, ipady=5)

# Botões
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Criar Conta", command=criar_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='light green').grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Remover Conta", command=remover_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='salmon').grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Atualizar Conta", command=atualizar_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='yellow').grid(row=0, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Consultar Conta", command=consultar_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='yellow').grid(row=0, column=3, padx=10, pady=5)

tk.Button(button_frame, text="Depósito", command=deposito_gui, width=20, font=('Helvetica', 12, 'bold'), bg='light blue').grid(row=1, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Saque", command=saque_gui, width=20,font=('Helvetica', 12, 'bold'), bg="light blue").grid(row=1, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Transferência", command=transferencia_gui, width=20, font=('Helvetica', 12, 'bold'), bg='yellow').grid(row=1, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Salvar e Sair", command=salvar_sair, width=20, font=('Helvetica', 12, 'bold'), bg="light blue").grid(row=1, column=3, padx=10, pady=5)

root.mainloop()
