#Escreva um programa que copie os valores pares para uma lista e os
#valores ímpares para outra lista. A lista inicialmente de valores é V=[9,8,7,12,0,13,21] .

lista = [9,8,7,12,0,13,21]
par = []
impar = []

def num_par_e_num_impar():
    for i in lista:
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)              
    
num_par_e_num_impar()
print(f'Os numeros pares da lista são: ',par)
print(f'Os numeros impares da lista são: ',impar)          
