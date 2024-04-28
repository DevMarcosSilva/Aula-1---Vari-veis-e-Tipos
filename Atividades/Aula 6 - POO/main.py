from classes import *
import time

def main():
    print("Bem-vindo ao sistema bancário!")

    # Coletar informações do cliente
    nome = input("Informe o seu nome: ")
    sobrenome = input("Informe o seu sobrenome: ")
    cpf = input("Informe o seu CPF: ")

    cliente = Cliente(nome, sobrenome, cpf)

    print("\nEscolha o tipo de conta:")
    print("1. Conta Poupança")
    print("2. Conta Corrente")
    tipo_conta = input("Informe o tipo de conta (1 ou 2): ")

    if tipo_conta == "1":
        numero_agencia = input("Informe o número da agência: ")
        saldo_inicial = float(input("Informe o saldo inicial: "))
        limite = float(input("Informe o limite: "))
        aniversario_conta = input("Informe a data de aniversário da conta (DD/MM): ")

        conta = ContaPoupanca(numero_agencia, "Poupança", saldo_inicial, limite, aniversario_conta)
    elif tipo_conta == "2":
        numero_agencia = input("Informe o número da agência: ")
        saldo_inicial = float(input("Informe o saldo inicial: "))
        limite = float(input("Informe o limite: "))
        cheque_especial = input("A conta possui cheque especial? (S/N): ").upper() == "S"

        conta = ContaCorrente(numero_agencia, "Corrente", saldo_inicial, limite, cheque_especial)
    else:
        print("Opção inválida.")
        return

    print("\nConta criada com sucesso!")
    print(f"Titular: {cliente.nome} {cliente.sobrenome}")
    print(f"Tipo de Conta: {conta.tipo_conta}")
    print(f"Número da Agência: {conta.numero_agencia}")
    print(f"Saldo: R${conta.consultar_saldo()}")

    # Exemplo de utilização das operações
    while True:
        print("\nEscolha uma operação:")
        print("1. Consultar Saldo")
        print("2. Sacar")
        print("3. Depositar")
        print("4. Transferir")
        print("5. Obter Extrato")
        print("6. Fechar Conta")
        print("0. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            print(f"Saldo: R${conta.consultar_saldo()}")
        elif opcao == "2":
            valor = float(input("Informe o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == "3":
            valor = float(input("Informe o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == "4":
            valor = float(input("Informe o valor a ser transferido: "))
            destinatario = input("Informe o número da agência do destinatário: ")
            conta.transfere_para(destinatario, valor)
        elif opcao == "5":
            conta.obter_extrato()
        elif opcao == "6":
            conta.fechar_conta()
            print("Conta fechada com sucesso!")
            break
        elif opcao == "0":
            print("Obrigado por utilizar o sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
     
     
    


