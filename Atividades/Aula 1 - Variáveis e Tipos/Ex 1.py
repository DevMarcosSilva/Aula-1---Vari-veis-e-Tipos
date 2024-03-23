#Escreva um aplicativo que solicita ao usuário inserir dois inteiros, 
# obtém do usuário esses números e imprime sua soma,
# produto, diferença e divisão.

numero1 = int(input('Informe o primeiro numero inteiro: '))
numero2 = int(input('Informe o segundo numero inteiro:' ))


def soma():
    resultado_soma = numero1 + numero2
    return resultado_soma

def produto():
    resultado_produto = numero1 * numero2
    return resultado_produto

def diferenca():
    if numero1 > numero2 or numero1 == numero2 :
        resultado_diferenca = numero1 - numero2
        return resultado_diferenca
    
    elif numero2 > numero1:
        resultado_diferenca = numero2 - numero1
        return resultado_diferenca

def divisao():
    resultado_divisao = numero1 / numero2
    return resultado_divisao
    
print(f'\nA soma de {numero1} + {numero2} é igual a: {soma()} ')
print(f'A diferença entre {numero1} e {numero2} é : {diferenca()} ')
print(f'O resultado da divisão de {numero1} por {numero2} é : {divisao()}')
print(f'O produto de {numero1} x {numero2} é : {produto()} \n')
    