#Modifique o programa anterior de forma a ler um número n. Imprima os n
#primeiros números primos.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input('Informe um número inteiro positivo: '))

numeros_primos = []
numero = 2

while len(numeros_primos) < n:
    if eh_primo(numero):
        numeros_primos.append(numero)
    numero += 1

print(f'Os {n} primeiros números primos são: {numeros_primos}')
