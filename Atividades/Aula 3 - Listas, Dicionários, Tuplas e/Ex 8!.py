#Escreva um programa que compare duas listas. Utilizando operações com
#conjuntos, imprima:
#os valores comuns às duas listas
#os valores que só existem na primeira
#os valores que existem apenas na segunda
#uma lista com os elementos não repetidos das duas listas.
#a primeira lista sem os elementos repetidos na segunda

lista1 = [1,5,6,9,4,8,6]
lista2 = [5,69,8,-5,6,4,7]

def valor_comum():
    conju_lista1= set(lista1)
    conju_lista2= set(lista2)
    elemento_comum = conju_lista1.intersection(conju_lista2)
    print('A interseção entre os elementos da lista 1 é lista 2 são:')
    for elemento in elemento_comum:
        print(elemento, end=" ")
 

        
valor_comum()        