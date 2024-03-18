#Escreva um programa que converta uma temperatura digitada em "C” em “F”. A fórmula para essa conversão é: F =(9/5)*C + 32

temperatura_Celsus = float(input('Informe a temperatura em graus celsus: '))

def converter_temp():
    F =(9/5)*temperatura_Celsus+32
    return F
   

print(f'{temperatura_Celsus}º corresponde a {converter_temp()}º Fahrenheit')