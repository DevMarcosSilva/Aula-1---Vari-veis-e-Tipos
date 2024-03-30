#Escreva um programa que compare duas listas. Considere a primeira lista
#como a versão inicial e a segunda como a versão após alterações.
#Utilizando operações com conjuntos, seu programa deverá imprimir a lista
#de modificações entre essas duas versões, listando:
# ◦ os elementos que não mudaram
# ◦ os novos elementos
# ◦ os elementos que foram removidos

def comparar_listas(lista_inicial, lista_alterada):
    
    conjunto_inicial = set(lista_inicial)
    conjunto_alterado = set(lista_alterada)
    
    
    iguais = conjunto_inicial.intersection(conjunto_alterado)
    
    
    novos = conjunto_alterado - conjunto_inicial
    
    
    removidos = conjunto_inicial - conjunto_alterado
    

    print("Elementos que não mudaram:")
    print(iguais)
    print("\nNovos elementos:")
    print(novos)
    print("\nElementos removidos:")
    print(removidos)

lista_inicial = [1, 2, 3, 4, 5]
lista_alterada = [2, 3, 5, 6, 7]
comparar_listas(lista_inicial, lista_alterada)

