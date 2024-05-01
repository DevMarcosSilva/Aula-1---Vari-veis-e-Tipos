with open('listas.txt','r',encoding="utf-8") as arquivo:
    dados = arquivo.readlines()
    lista1=set(dados[1].split())
    lista2=set(dados[2].split())
    lista3=set(dados[3].split())
    lista4=set(dados[4].split())
    lista5=set(dados[5].split())



    
       
elemen_n_repetem=(lista1^lista2^lista3^lista4^lista5)-(lista1&lista2&lista3&lista4&lista5)

todos_elementos = lista1.union(lista2, lista3, lista4, lista5)

contagem = {}

for elemento in todos_elementos:
   
    contagem[elemento] = contagem.get(elemento, 0) + (1 if elemento in lista1 else 0)
    
    contagem[elemento] = contagem.get(elemento, 0) + (1 if elemento in lista2 else 0)
    
    contagem[elemento] = contagem.get(elemento, 0) + (1 if elemento in lista3 else 0)
    
    contagem[elemento] = contagem.get(elemento, 0) + (1 if elemento in lista4 else 0)
    
    contagem[elemento] = contagem.get(elemento, 0) + (1 if elemento in lista5 else 0)

with open('listasSaida.txt','w',encoding="utf-8") as arquivoSaida:
    arquivoSaida.write(f'Elementos que aparecem uma única vez: {elemen_n_repetem}')
    arquivoSaida.write('\n-----------------------------\n')
    arquivoSaida.write('Repetições: \n')
    for elemento, ocorrencias in contagem.items():
        arquivoSaida.write(f"'{elemento}', se repete: {ocorrencias}\n")
    arquivoSaida.write('-----------------------------')
    resultado = lista5-lista1
    
    arquivoSaida.write(f'\nElementos presentes na última lista mas não na primeira: {resultado}')
    
