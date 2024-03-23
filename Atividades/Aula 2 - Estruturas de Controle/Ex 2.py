#Escreva um programa que leia um número e verifique se é ou não um
#número primo.

numero = int(input('Informe um numero: '))

if numero > 1 and numero % numero == 0 and numero % 1 == 0 and numero %2 !=0: 
    print(f'{numero} é primo!')
else:
    print(f'{numero} NÃO é primo!')    