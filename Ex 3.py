numero = int(input('Informe um numero inteiro: '))

def calculo_impar_par():
    if (numero % 2) == 0:
        print(f'{numero} é par')
    else: 
        print(f'{numero} é impar')
    
calculo_impar_par()            