grid=[["00","01","02"],["10","11","12"],["20","21","22"]]

for linha in range(0,len(grid)) :
    for coluna in range(0,len(grid[linha])):
        print(grid[linha][coluna],end=" ")
    print()
    
jogada = input('entre com o simbolo X ou 0:')
linha= int(input('qual linha'))
coluna= int(input('qual coluna'))       