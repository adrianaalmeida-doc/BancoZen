import tkinter as tk
from tkinter import messagebox
from banco import*
from dados import*



# Funções da interface gráfica
def criar_conta_gui():
    numero = entry_numero.get()
    nome_titular = entry_nome.get()
    saldo = entry_saldo.get()
    tipo = entry_tipo.get()


    if not numero.isdigit() or numero in contas:
        messagebox.showerror("Erro", "Número da conta inválido ou já existe.")
        return

    try:
        saldo = float(saldo)
        if saldo <= 0:
            messagebox.showerror("Erro", "O saldo deve ser positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Saldo inválido. Deve ser um número.")
        return

    criar_conta(numero, nome_titular, saldo, tipo)
    salvar_dados()
    salvar_usuarios()
    messagebox.showinfo("Sucesso", f"Conta {numero} para {nome_titular} criada com sucesso!")

def remover_conta_gui():
    numero = entry_numero.get()
    
    if not numero.isdigit() or numero not in contas:
        messagebox.showerror("Erro", "Conta não encontrada.")
        return
    
    remover_conta(numero)
    salvar_dados()
    salvar_usuarios()
    messagebox.showinfo("Sucesso", f"Conta {numero} removida com sucesso!")

def atualizar_conta_gui():
    numero = entry_numero.get()
    nome_titular = entry_nome.get()
    saldo = entry_saldo.get()

    if not numero.isdigit() or numero not in contas:
        messagebox.showerror("Erro", "Conta não encontrada.")
        return

    saldo = saldo if saldo == "" else float(saldo)
    
    if saldo != "" and saldo <= 0:
        messagebox.showerror("Erro", "O saldo deve ser positivo.")
        return
    
    atualizar_conta(numero, nome_titular, saldo)
    salvar_dados()
    salvar_usuarios()
    messagebox.showinfo("Sucesso", f"Conta {numero} atualizada com sucesso!")

def consultar_conta_gui():
    numero = entry_numero.get()

    if not numero.isdigit():
        messagebox.showerror("Erro", "O número da conta deve conter apenas dígitos.")
        return

    conta = consultar_conta(numero)
    if conta:
        messagebox.showinfo("Informação", f"Conta {numero}: Nome: {conta['nome']}, Saldo: R${conta['saldo']}, Tipo: {conta['tipo']}")
    else:
        messagebox.showerror("Erro", "Conta não encontrada.")

def deposito_gui():
    numero = entry_numero.get()
    valor = entry_saldo.get()

    if not numero.isdigit() or numero not in contas:
        messagebox.showerror("Erro", "Conta não encontrada.")
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
    salvar_dados()
    messagebox.showinfo("Sucesso", f"Depósito de R${valor} realizado com sucesso na conta {numero}!")

def saque_gui():
    numero = entry_numero.get()
    valor = entry_saldo.get()

    if not numero.isdigit() or numero not in contas:
        messagebox.showerror("Erro", "Conta não encontrada.")
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
        salvar_dados()
        messagebox.showinfo("Sucesso", f"Saque de R${valor} realizado com sucesso na conta {numero}!")
    else:
        messagebox.showerror("Erro", "Saldo insuficiente.")

def transferencia_gui():
    numero_origem = entry_numero.get()
    numero_destino = entry_destino.get()
    valor = entry_saldo.get()

    if not numero_origem.isdigit() or not numero_destino.isdigit() or numero_origem not in contas or numero_destino not in contas:
        messagebox.showerror("Erro", "Uma ou ambas as contas não foram encontradas.")
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
    if conta_origem and conta_origem['saldo'] >= valor:
        transferencia(numero_origem, numero_destino, valor)
        salvar_dados()
        messagebox.showinfo("Sucesso", f"Transferência de R${valor} da conta {numero_origem} para a conta {numero_destino} realizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Saldo insuficiente.")

def listar_relatorio_gui():
    
    carregar_dados()  
    carregar_usuarios()  

    text_area.config(state=tk.NORMAL) 
    text_area.delete(1.0, tk.END)  

    # Formatar a saída
    relatorio = "Relatório de Contas e Usuários\n\n"
    
    if users:
        for usuario, dados in users.items():
            relatorio += f"Usuário: {dados['nome']}\n"
            contas_usuario = [numero for numero in contas if numero == usuario]
            if contas_usuario:
                for numero in contas_usuario:
                    relatorio += f"  - Conta: {numero}, Saldo: R${contas[numero]['saldo']}, Tipo: {contas[numero]['tipo']}\n"
            else:
                relatorio += "  - Nenhuma conta cadastrada.\n"
    else:
        relatorio += "Nenhum usuário cadastrado.\n"

    text_area.insert(tk.END, relatorio)  
    text_area.config(state=tk.DISABLED) 

def salvar_sair():
    salvar_dados()
    salvar_usuarios()

    root.destroy()

# Criação da janela
root = tk.Tk()
root.title("Banco Digital Zen")


# Layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Entradas de Dados
tk.Label(frame, text="Número da Conta:", font=("Helvetica", 12)).grid(row=0, column=0, padx=20, pady=10)
entry_numero = tk.Entry(frame, width=30)
entry_numero.grid(row=0, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Nome do Titular:", font=("Helvetica", 12)).grid(row=1, column=0, padx=20, pady=10)
entry_nome = tk.Entry(frame, width=30)
entry_nome.grid(row=1, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Saldo:", font=("Helvetica", 12)).grid(row=2, column=0, padx=20, pady=10)
entry_saldo = tk.Entry(frame, width=30)
entry_saldo.grid(row=2, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Tipo de Conta:", font=("Helvetica", 12)).grid(row=3, column=0, padx=20, pady=10)
entry_tipo = tk.Entry(frame, width=30)
entry_tipo.grid(row=3, column=1, padx=10, pady=5, ipady=5)

tk.Label(frame, text="Número da Conta Destino:", font=("Helvetica", 12)).grid(row=4, column=0, padx=20, pady=10)
entry_destino = tk.Entry(frame, width=30)
entry_destino.grid(row=4, column=1, padx=10, pady=5, ipady=5)

# Botões
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Criar Conta", command=criar_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='light green').grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Remover Conta", command=remover_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='salmon').grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Atualizar Conta", command=atualizar_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='yellow').grid(row=0, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Consultar Conta", command=consultar_conta_gui, width=20, font=('Helvetica', 12, 'bold'), bg='yellow').grid(row=0, column=3, padx=10, pady=5)

tk.Button(button_frame, text="Depósito", command=deposito_gui, width=20, font=('Helvetica', 12, 'bold'), bg='light blue').grid(row=1, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Saque", command=saque_gui, width=20, font=('Helvetica', 12, 'bold'), bg="light blue").grid(row=1, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Transferência", command=transferencia_gui, width=20, font=('Helvetica', 12, 'bold'), bg='yellow').grid(row=1, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Salvar e Sair", command=salvar_sair, width=20, font=('Helvetica', 12, 'bold'), bg="light blue").grid(row=1, column=3, padx=10, pady=5)

# Botão para listar relatório
tk.Button(button_frame, text="Listar Relatório", command=listar_relatorio_gui, width=20, font=('Helvetica', 12, 'bold'), bg='light blue').grid(row=2, column=0, padx=10, pady=5, columnspan=4)

text_area = tk.Text(root, height=10, width=80, font=("Helvetica", 12))
text_area.pack(pady=20)
text_area.config(state=tk.DISABLED)  
root.mainloop()