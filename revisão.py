N = int(input()) 

notas = [100.00,50.00,20.00,10.00,5.00,2.00]
print ("R$ %d:"%(N))
for x in notas:
    print ("%i nota(s) de R$ %.2f"%((N/x),x))
    N %= x