import json
from dados import contas

def criar_conta(numero, nome, saldo):
    contas[numero] = {'nome': nome, 'saldo': saldo}

def remover_conta(numero):
    if numero in contas:
        del contas[numero]

def atualizar_conta(numero, nome=None, saldo=None):
    if numero in contas:
        if nome:
            contas[numero]['nome'] = nome
        if saldo is not None:
            contas[numero]['saldo'] = saldo

def consultar_conta(numero):
    return contas.get(numero, None)

def deposito(numero, valor):
    if numero in contas:
        contas[numero]['saldo'] += valor

def saque(numero, valor):
    if numero in contas and contas[numero]['saldo'] >= valor:
        contas[numero]['saldo'] -= valor

def transferencia(numero_origem, numero_destino, valor):
    if numero_origem in contas and numero_destino in contas and contas[numero_origem]['saldo'] >= valor:
        contas[numero_origem]['saldo'] -= valor
        contas[numero_destino]['saldo'] += valor