import tkinter as tk
from tkinter import messagebox
from dados import*


def criar_conta(numero, nome_titular, saldo, tipo):
    contas[numero] = {'saldo': saldo, 'tipo': tipo}
    users[numero] = {'nome': nome_titular}
    salvar_dados()
    salvar_usuarios()

def remover_conta(numero):
    if numero in contas:
        del contas[numero]
        del users[numero]

def atualizar_conta(numero, nome=None, saldo=None, tipo=None):
    if numero in contas:
        if nome:
            users[numero]['nome'] = nome
        if saldo is not None:
            contas[numero]['saldo'] = saldo
        if tipo:
            contas[numero]['tipo'] = tipo

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