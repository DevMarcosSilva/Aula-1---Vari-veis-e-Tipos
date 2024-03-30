#Crie uma lista chamada sandwich_orders e a preencha com os nomes de
#vários sanduíches. Em seguida, crie uma lista vazia chamada
#finished_sandwiches. Percorra a lista de pedidos de sanduíches com um
#laço e mostre uma mensagem para cada pedido, por exemplo, Preparei seu
#sanduíche de atum. À medida que cada sanduíche for preparado, transfira para a lista de sanduíches prontos. Depois que todos os sanduíches
#estiverem prontos, mostre uma mensagem que liste cada sanduíche
#preparado.
import time

sandwich_orders = ['Frango', 'Atum', 'Vegetariano', 'Presunto e Queijo']

finished_sandwiches = []

print("Preparando os pedidos de sanduíches:")
for sandwich in sandwich_orders:
    print("Preparando seu sanduíche de " + sandwich + ".")
    finished_sandwiches.append(sandwich)
    time.sleep(1)

print("\nSanduíches preparados:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
    time.sleep(1)
