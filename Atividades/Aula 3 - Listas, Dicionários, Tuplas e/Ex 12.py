#Crie vários dicionários, em que o nome de cada dicionário seja o nome de
#um animal de estimação. Em cada dicionário, inclua o tipo do animal e o
#nome do dono. Armazene esses dicionários em uma lista chamada pets.
#Em seguida, percorra sua lista com um laço e, à medida que fizer isso,
#apresente tudo que você sabe sobre cada animal de estimação.

pets = []

for i in range(3):  
    pet = {}  
    pet['nome'] = input("Informe o nome do animal de estimação: ")
    pet['tipo'] = input("Informe o tipo do animal (ex: Cachorro, Gato, etc.): ")
    pet['dono'] = input("Informe o nome do dono do animal: ")
    pets.append(pet)  

print("\nInformações sobre os animais de estimação:")
for pet in pets:
    print("\nNome:", pet['nome'])
    print("Tipo:", pet['tipo'])
    print("Dono:", pet['dono'])
