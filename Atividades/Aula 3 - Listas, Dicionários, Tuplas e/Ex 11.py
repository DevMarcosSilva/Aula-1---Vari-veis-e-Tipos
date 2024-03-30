#Comece com o programa que você escreveu no Exercício 10. Crie dois
#novos dicionários que representem pessoas diferentes e armazene os três
#dicionários em uma lista chamada people. Percorra sua lista de pessoas
#com um laço. À medida que percorrer a lista, apresente tudo que você sabe
#sobre cada pessoa.

people = []

for _ in range(3):  
    pessoa = {}
    pessoa['first_name'] = input("Informe o primeiro nome da pessoa: ")
    pessoa['last_name'] = input("Informe o sobrenome da pessoa: ")
    pessoa['age'] = int(input("Informe a idade da pessoa: "))
    pessoa['city'] = input("Informe a cidade em que a pessoa vive: ")
    people.append(pessoa)  

print("\nInformações sobre as pessoas:")

for pessoa in people:
    print("\nNome:", pessoa['first_name'], pessoa['last_name'])
    print("Idade:", pessoa['age'])
    print("Cidade:", pessoa['city'])
