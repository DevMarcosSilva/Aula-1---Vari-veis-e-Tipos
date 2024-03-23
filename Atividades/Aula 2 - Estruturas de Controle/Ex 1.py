#Escreva um programa que exiba uma lista de opções (menu): adição,
#subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
#escolhida. Repita até que a opção saída seja escolhida.

def menu():
    print('Esolha a opção desejada!')
    print('1. Adição.\n2. Subtração.\n3. Divisão.\n4. Multiplicação.\n0. Sair.')
    opcao = int(input())
    return operacao(opcao)

def operacao(opcao):
        while opcao !=0:
            n1 = int(input('Informe o Primeiro numero: '))
            n2 = int(input('Informe o Segundo numero: '))
            if opcao==1:
                print(f'A adição de {n1} + {n1} = {n1+n2}') 
                voltar = int(input('Deseja continuar? 1(SIM) ou 2(NÃO)'))
                if voltar == 1:
                    menu()
            elif opcao==2:
                print(f'A subtração de {n1} - {n2} = {n1-n2}')
                voltar = int(input('Deseja continuar? 1(SIM) ou 2(NÃO)'))
                if voltar == 1:
                    menu()
            elif opcao==3:
                print(f'A divisão de {n1} / {n2} = {n1/n2}')
                voltar = int(input('Deseja continuar? 1(SIM) ou 2(NÃO)'))
                if voltar == 1:
                    menu()
            elif opcao==4:
                print(f'A multiplicação de {n1} x {n2} = {n1*n2}')
                voltar = int(input('Deseja continuar? 1(SIM) ou 2(NÃO)'))
                if voltar == 1:
                    menu()
            else:
                print(f'Opção inválida!')
                voltar = int(input('Deseja continuar? 1(SIM) ou 2(NÃO)'))
                if voltar == 1:
                    menu()             
            break
   
menu()
print('Programa encerrado!') 