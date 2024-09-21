import json

# Estruturas iniciais
contas = {}
users = {}

def salvar_dados():
    with open('contas.json', 'a') as f: 
        json.dump(contas, f, indent=4)
print(f"Dados de contas salvos: {contas}")  


def carregar_dados():
    global contas
    try:
        with open('contas.json', 'r') as f:
            contas = json.load(f)
    except FileNotFoundError:
        contas = {}
    except json.JSONDecodeError:
        contas = {}  

def salvar_usuarios():
    with open('usuarios.json', 'a') as f: 
        json.dump(users, f, indent=4)

def carregar_usuarios():
    global users
    try:
        with open('usuarios.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    except json.JSONDecodeError:
        users = {} 
