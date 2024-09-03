from banco import criar_conta, remover_conta, atualizar_conta, consultar_conta, deposito, saque, transferencia
from dados import carregar_dados, salvar_dados

def main():
    carregar_dados()

    while True:
        print("\nBanco Digital Zen")
        print("1. Criar Conta")
        print("2. Remover Conta")
        print("3. Atualizar Conta")
        print("4. Consultar Conta")
        print("5. Depósito")
        print("6. Saque")
        print("7. Transferência")
        print("8. Salvar e Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            numero = input("Número da conta: ")
            nome = input("Nome do titular: ")
            saldo = float(input("Saldo inicial: "))
            criar_conta(numero, nome, saldo)
            print(f"Conta {numero} criada com sucesso!")

        elif opcao == '2':
            numero = input("Número da conta a ser removida: ")
            remover_conta(numero)
            print(f"Conta {numero} removida com sucesso!")

        elif opcao == '3':
            numero = input("Número da conta a ser atualizada: ")
            nome = input("Novo nome (deixe em branco para não alterar): ")
            saldo = input("Novo saldo (deixe em branco para não alterar): ")
            saldo = float(saldo) if saldo else None
            atualizar_conta(numero, nome, saldo)
            print(f"Conta {numero} atualizada com sucesso!")

        elif opcao == '4':
            numero = input("Número da conta a ser consultada: ")
            conta = consultar_conta(numero)
            if conta:
                print(f"Conta {numero}: {conta}")
            else:
                print("Conta não encontrada.")

        elif opcao == '5':
            numero = input("Número da conta para depósito: ")
            valor = float(input("Valor do depósito: "))
            deposito(numero, valor)
            print(f"Depósito de R${valor} realizado com sucesso na conta {numero}!")

        elif opcao == '6':
            numero = input("Número da conta para saque: ")
            valor = float(input("Valor do saque: "))
            saque(numero, valor)
            print(f"Saque de R${valor} realizado com sucesso na conta {numero}!")

        elif opcao == '7':
            numero_origem = input("Número da conta de origem: ")
            numero_destino = input("Número da conta de destino: ")
            valor = float(input("Valor da transferência: "))
            transferencia(numero_origem, numero_destino, valor)
            print(f"Transferência de R${valor} da conta {numero_origem} para a conta {numero_destino} realizada com sucesso!")

        elif opcao == '8':
            salvar_dados()
            print("Dados salvos com sucesso. Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
