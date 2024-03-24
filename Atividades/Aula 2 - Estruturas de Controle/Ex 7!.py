#Numa certa agência bancária, as contas são identificadas por números de
#até seis dígitos seguidos de um dígito verificador, calculado conforme
#exemplificado a seguir. Dado um número de conta n, exiba o número de
#conta completo correspondente. Seja n = 7314 o número da conta.
#Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15;
#Calculamos o resto da divisão de s por 10 e obtemos o dígito d = 5. Número
#de conta completo: 007314−5

numero = input("Informe um numero de até 6 digitos: ")

def conta():
   conv = int(numero)
   for i in range(0,conv):
    resultado = conv[i]+conv[i+i]
    
    print(resultado)
conta()
