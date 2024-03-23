#Modifique o programa anterior de forma a ler um número n. Imprima os n
#primeiros números primos.

numero = int(input('Informe um numero: '))
cont = 0


for i in range(numero):
    num_inf=numero
    if numero > 1 and numero % numero == 0 and numero % 1 == 0 and numero %2 !=0:
        cont += numero
        print(cont, end=" ")
    else:
        print('erro')    
