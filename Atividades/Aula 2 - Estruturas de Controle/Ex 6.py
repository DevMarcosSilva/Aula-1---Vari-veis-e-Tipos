#A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros
#termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos
#dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da
#série de Fibonacci.

numero = int(input("Informe um numero: "))

def fibonacci():
    print('1',end=" ")
    n1=1
    n2=0
    for i in range(1,numero): 
        temp= n1+n2  
        print(temp, end=" ") 
        n2 = n1
        n1 = temp
    
fibonacci()    