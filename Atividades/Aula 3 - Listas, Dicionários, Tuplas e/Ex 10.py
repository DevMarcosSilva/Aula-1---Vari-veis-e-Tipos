#Use um dicionário para armazenar informações sobre uma pessoa que
#você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
#cidade em que ela vive. Você deverá ter chaves como first_name,
#last_name, age e city. Mostre cada informação armazenada em seu
#dicionário.


pessoa = {}
pessoa['first_name'] = input("Informe o primeiro nome da pessoa: ")
pessoa['last_name'] = input("Informe o sobrenome da pessoa: ")
pessoa['age'] = int(input("Informe a idade da pessoa: "))
pessoa['city'] = input("Informe a cidade em que a pessoa vive: ")


print("\nInformações sobre a pessoa:")
print("Primeiro nome:", pessoa['first_name'])
print("Sobrenome:", pessoa['last_name'])
print("Idade:", pessoa['age'])
print("Cidade:", pessoa['city'])
