#Escreva um programa que controla a utilização das salas de um cinema.
#Imagine que a lista lugares_vagos=[10,2,1,3,0] contenha o número de
#lugares vagos nas salas 1,2,3,4 e 5, respectivamente. Esse programa lerá o
#número da sala e a quantidade de lugares solicitados. Ele deve informar se
#é possível vender o número de lugares solicitados, ou seja, se ainda há
#lugares livres. Caso seja, possível vender os bilhetes, atualizará o número
#de lugares livres. A saída ocorre quando se digita 0 no número da sala.
import time

salas = [1,2,3,4,5]
lugares_vagos=[10,2,1,3,0] 

def sala_desejada(sala_soli):
    for indice,(elemet_salas,elemet_lugares_vagos) in enumerate(zip(salas,lugares_vagos)):
        if sala_soli == elemet_salas:
            print(f'Na Sala {sala_soli} - restam ainda {elemet_lugares_vagos} lugar(s)')

def lugares_desejados(sala_soli,lugares_soli):
        sala_solic = sala_soli
        lugares_solic = lugares_soli
        for indice,(elemet_salas,elemet_lugares_vagos) in enumerate(zip(salas,lugares_vagos)):
            if sala_solic == elemet_salas:
                if lugares_solic <= elemet_lugares_vagos:
                    elemet_lugares_vagos = elemet_lugares_vagos-lugares_solic
                    print('atualizando...')
                    time.sleep(1)
                    print(f'Na Sala {sala_solic} - agora restam ainda {elemet_lugares_vagos} lugar(s)')
                    lugares_vagos[indice]-=lugares_solic 
                else: 
                    print(f'não temos essa quantidade de lugares na sala {sala_solic}')
        print('Deseja continuar comprando: SIM ou NÃO!')
        opcao = input()            
        while opcao == 'sim' or opcao == 'SIM':
            inicio()


def inicio():            
    sala_soli= int(input('Informe a sala desejada! '))
    sala_desejada(sala_soli)
    lugares_soli= int(input('Informe a quantidade de lugares desejada! '))
    lugares_desejados(sala_soli,lugares_soli)              

inicio()