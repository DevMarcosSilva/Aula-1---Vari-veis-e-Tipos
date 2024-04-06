#Faça um programa que controle uma agenda. Com as funções apaga() , 
#altera() , lista() , le() , grava() , menu() . Depois faça as seguintes
#melhorias:
#a. Exiba o tamanho da agenda no menu principal;
#b. Exiba a posição de cada elemento;
#c. Exiba a opção de ordenar a lista por nome no menu principal;
#d. Exiba uma mensagem de erro caso duas entradas na agenda tenham o
#mesmo nome;
#e. Adicione também a data de aniversário e email de cada pessoa.
#f. Permita o cadastro de tipos de telefone: celular, fixo, residência ou
#trabalho
import time
numero_Tarefas = [10]
nomeTarefa = []
dataInicio = []
dataTerm = []
i = 0
def menu():
    opcao = int(input('Olá informe o que deseja!\n 1.Inserir nova tarefa\n 2.editar tarefa\n 3.visualiza todas as tarefas\n 4.Apagar tarefa\n 5.Sair da agenda\n'))
    while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 :
       print('Opçao inválida insira um numero de 1 a 5\n')
       time.sleep(1)
       menu()
    if opcao == 1:
        inserir()
    elif opcao == 2:
        listadeTarefas()          

def inserir(i=0):
    
    while i < len(numero_Tarefas):
        nomeinserido = {}
        nomeinserido['nome-tarefa'] = input('Informe o título da tarefa que deseja inserir: ')
        nomeTarefa.append(nomeinserido)

        dataInicioUser = {}
        dataInicioUser['data-inicio'] = input('Informe a data de inicio da tarefa: ')
        dataInicio.append(dataInicioUser)
        
        dataTermUser = {}
        dataTermUser['data-termino'] = input('Informe a data de término da tarefa: ')
        dataTerm.append(dataTermUser)

        print(f'Tarefa agendada com sucesso! Nº TAREFA É: {i+1}')
        i += 1
        
    
    opcao = int(input('Para cadastrar mais uma tarefa digite 1 ou 2 para retornar ao menu principal'))
    if opcao == 1:
        inserir()
    elif opcao == 2:
        menu()    

def listadeTarefas():
    for i in range(0,len(nomeTarefa)):
        print(f'Tarefa {i+1}')
        print(nomeTarefa[i])
        print(dataInicio[i])
        print(dataTerm[i])
        

menu()
  