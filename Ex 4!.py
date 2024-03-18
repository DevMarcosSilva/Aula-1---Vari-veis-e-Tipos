#Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, 
# separa o número em seus dígitos individuais e imprime os dígitos separados uns dos outros por três espaços cada. 
# Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.

numero = input('Informe um numero com 5 digitos: ')

def separa_digitos():
  for i in range(0,1):
       print(numero[i],numero[i+1],numero[i+2],numero[i+3],numero[i+4])

separa_digitos()