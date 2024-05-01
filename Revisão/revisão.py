
"""def menu():
    dado = float(input("Informe um valor: "))
    while dado< 0 or dado>100000000:
        print('Valor inválido! digite um valor entre 0 e 1000000.00')
        menu()
        break
    return dado"""
    
    
    
def decompor():
    dado = float(input("Informe um valor: "))
    notas = [100.00,50.00,20.00,10.00,5.00,2.00]
    print (f"R$ {dado}:")
    for x in notas:
        print ("%i nota(s) de R$ %.2f"%((dado/x),x))
        dado %= (x)
    
        




decompor()