#O quadrado de um número natural n é dado pela soma dos n primeiros
#números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1+3 etc. Dado
#um número n, calcule seu quadrado usando a soma de ímpares ao invés de
#produto.

numero = int(input('Informe um numero: '))


def quadrado():
    for i in range(1,numero):
        i =+ i
        if i%2!=0:
         print(i,end=" ")
       
quadrado()            