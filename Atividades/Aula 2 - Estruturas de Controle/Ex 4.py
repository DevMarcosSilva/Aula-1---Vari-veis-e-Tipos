#O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n
#fatorial”) e é definido como segue:
#n! = n · (n – 1) · (n – 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! =
#1 (para n = 0)
#Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120.
#Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
#fatorial.

numero_informado = int(input('informe um numero interiro maior que 0: '))

def fatorial():
    resultado = 1
    for i in range(numero_informado,0,-1):
        resultado *= i
    return resultado

fatorial()
print(fatorial())
