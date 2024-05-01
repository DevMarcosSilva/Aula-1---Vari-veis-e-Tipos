with open('listas.txt','r',encoding="utf-8") as arquivo:
    dados = arquivo.readlines()
    lista1=set(dados[1].split())
    lista2=set(dados[2].split())
    lista3=set(dados[3].split())
    lista4=set(dados[4].split())
    lista5=set(dados[5].split())
    
    
    '''teste = set(lista3)
    teste2 = set(lista4)
    
    result= teste.intersection(teste2)'''
    print(lista1 | lista2)
