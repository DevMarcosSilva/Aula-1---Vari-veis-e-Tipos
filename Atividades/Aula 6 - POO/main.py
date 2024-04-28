from classes import *
import time

def criarConta():
    nomeTitular = input('INFORME O PRIMEIRO NOME E ÚLTIMO NOME DO TITULAR: ')        
    num_agen = input(f'INFORME A AGENCIA: ')
    tipo = input(f'INFORME O TIPO DE CONTA: Corrente | Poupança | Salário: ' )
    while tipo != 'Corrente' and tipo != 'Poupança' and tipo != 'Salário':
        print('INFORME UM TIPO DE CONTA VÁLIDO!')
        time.sleep(0.5)
        tipo = input(f'INFORME O TIPO DE CONTA: Corrente | Poupança | Salário: ' )
    saldo = int(input(f'INFORME O SALDO DA CONTA: '))
    limite = int(input(f'INFORME O LIMITE: ')) 
    print('CRIANDO CONTA... ')
    time.sleep(1)
    print('CRIANDO CONTA.. ')
    time.sleep(0.5)
    print('CRIANDO CONTA. ')
    print('CONTA CRIADA COM SUCESSO !')
    time.sleep(1)
    print('--------------')
    return nomeTitular,num_agen,tipo,saldo,limite





conta = ContaBancaria(*criarConta())



conta.sacar()

print(f'NOME: {conta.nomeTitular}\nAGÊNCIA: {conta.numero_agencia}\nTIPO: {conta.tipo_conta}\nSALDO: {conta.saldo}\nLIMITE: {conta.limite}')
     

        



