import json

# Estrutura inicial para armazenar contas
contas = {}

def salvar_dados():
    with open('contas.json', 'w') as f:
        json.dump(contas, f)

def carregar_dados():
    global contas
    try:
        with open('contas.json', 'r') as f:
            contas = json.load(f)
    except FileNotFoundError:
        contas = {}