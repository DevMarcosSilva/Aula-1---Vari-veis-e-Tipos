from classes import *
        
num_agen = input(f'INFORME A AGENCIA: ')
tipo = input(f'INFORME O TIPO DE CONTA: Corrente | Poupança | Salário: ' )
saldo = int(input(f'INFORME O SALDO DA CONTA: '))
limite = int(input(f'INFORME O LIMITE: ')) 

conta = ContaBancaria(num_agen,tipo,saldo,limite)

print(f'{conta.numero_agencia}\n{conta.tipo_conta}\n{conta.saldo}\n{conta.limite}')
     

        



