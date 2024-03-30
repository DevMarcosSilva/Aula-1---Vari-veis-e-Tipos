#Vamos tentar resolver alguns desafios. Dada a lista = [12, -2, 4, 8, 29, 45,78, 36, -17, 2, 12, 8, 3, 3,-52]
# faça um programa que:
#a. imprima o maior elemento;
#b. imprima o menor elemento;
#c. imprima os números pares;
#d. imprima o número de ocorrências do primeiro elemento da lista;
#e. imprima a média dos elementos;
#f. imprima a soma dos elementos de valor negativo

lista =  [12, -2, 4, 8, 29, 45,78, 36, -17, 2, 12, 8, 3, 3,-52]

def menu():
    print('Informe a opação desejada!')
    print('a. imprimir o maior elemento')
    print('b. imprimir o menor elemento')
    print('c. imprimir os números pares')
    print('d. imprimir o número de ocorrências do primeiro elemento da lista')
    print('e. imprimir a média dos elementos')
    print('f. imprimir a soma dos elementos de valor negativo!')
    print('g. imprimir todas as alternativas anteriores!')
    opcao = input("")
    print(opcao)
    
    if opcao == 'a' or opcao == 'A':
        maior()
    elif opcao == 'b' or opcao == 'B':
        menor()
    elif opcao == 'c' or opcao == 'C':
        numeros_pares()
    elif opcao == 'd' or opcao == 'D':
        ocorrencias()
    elif opcao == 'e' or opcao == 'E':
        media()                 
    elif opcao == 'f' or opcao == 'F':
        soma_negativo()
    elif opcao == 'g' or opcao == 'G':
        maior()
        menor()
        numeros_pares()
        ocorrencias()
        media()
        soma_negativo()   

def maior():
    maior_num = max(lista)
    print('O MAIOR elemento da lista é :',maior_num)   

def menor():
    menor_num = min(lista)
    print('O MENOR elemento da lista é :',menor_num)

def numeros_pares():
    print('Os números pares na lista são: ')
    for i in lista:
        if i%2==0:
            print(i, end=" ")

def ocorrencias():
    num_ocor = lista[0]
    cont = 0
    for i,elemento in enumerate(lista):
       if elemento == num_ocor:
           cont = cont + 1
    print(f'\nO elemento {lista[0]} apareceu {cont} vezes!')  

def media():
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)
    print('A média dos elementos é: ',"{:.2f}".format(media))
        
def soma_negativo():
    soma = 0
    for i in lista:
        if i < 0:
          soma +=i 
    print('A soma dos valores negativos da lista é:',soma, end=" ")         
    
                 



 
               


#ocorrencias()
#menor()
#maior()
#soma_negativo()
#media()
#numeros_pares()
menu()