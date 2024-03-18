#Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, 
# e calcule as raízes x’ e x” através da fórmula de Báskara.
import math

a = int(input('informe A: '))
b = int(input('informe B: '))
c = int(input('informe C: '))

    
def delta():
    delta = (b**2)-(4*a*c)
    return delta

def calculo_x1():
    x1= (-b + math.sqrt(delta())) / (2 * a)
    return x1

def calculo_x2():
   x2= -b-math.sqrt(delta())/2*a
   return x2

if delta() < 0:
    print('A equação não possui raízes reais')
else:    
    print("x1:", delta())
    print("x1:", calculo_x1())
    print("x2:", calculo_x2())
    