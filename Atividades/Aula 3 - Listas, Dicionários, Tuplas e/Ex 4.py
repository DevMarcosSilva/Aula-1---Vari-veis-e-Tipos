#A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T= [-10, -8, 0, 1, 2, 5, -2,-4].
# Faça um programa que imprima a menor e a maior
#temperatura, assim como a temperatura média.

lista = [-10, -8, 0, 1, 2, 5, -2,-4]

def maior_menor_media():
    maior_temp = max(lista)
    menor_temp = min(lista)
    media = sum(lista)/ len(lista)
    print('A MAIOR temperatura registrada em Mons foi : ',maior_temp)
    print('A MENOR temperatura registrada em Mons foi : ',menor_temp)
    print('A MÉDIA de temperatura registrada em Mons foi : ',media)

maior_menor_media()   