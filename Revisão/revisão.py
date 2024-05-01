def decompor(dado):
    notas = [100.00,50.00,20.00,10.00,5.00,2.00]
    moedas = [1.00,0.50,0.25,0.10,0.05,0.01]
    
    print (f"R$ {dado}:")
    for x in notas:
        print ("%i nota(s) de R$ %.2f"%((dado/x),x))
        dado %= (x)
    print('-----------------------')    
    for x in moedas:
        print("%i moeda(s) de R$ %.2f"%((dado/x),x))
        dado %= (x)    

dado = float(input("Informe um valor: "))
while dado< 0 or dado>100000000:
     print('Valor inválido! digite um valor entre 0 e 1000000.00')
     dado = float(input("Informe um valor: "))  

decompor(dado)   
    
    

        




