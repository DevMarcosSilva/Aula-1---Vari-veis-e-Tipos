#Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar ou par.

numero = int(input('Informe um numero inteiro: '))

def calculo_impar_par():
    if (numero % 2) == 0:
        print(f'{numero} é par')
    else: 
        print(f'{numero} é impar')
    
calculo_impar_par()            