#Escreva um programa que gere um dicionário, em que cada chave seja um
#caractere, e seu valor seja o número desse caractere encontrado em uma
#frase lida.
#Exemplo:O rato -> {"O":1,"r":1,"a":1,"t":1,"o":1}

def contar_caracteres(frase):
    contagem = {}
    for caractere in frase:
    
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

frase = input("Digite uma frase: ")

frase = frase.lower()

resultado = contar_caracteres(frase)

print("Ocorrências de cada caractere na frase:")
print(resultado)
