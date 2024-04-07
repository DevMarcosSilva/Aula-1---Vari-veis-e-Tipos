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

agenda = []

def menu():
        opcao = int(input(f'TAMANHO AGENDA {len(agenda)} \nOlá, informe o que deseja!\n 1. Inserir nova tarefa\n 2. Editar tarefa\n 3. Visualizar todas as tarefas\n 4. Apagar tarefa\n 5. ordenar por ordem alfabética\n 6. Sair\n'))
        while opcao < 1 or opcao > 6:
            print('OPÇÃO INVÁLIDA! Insira um número de 1 a 5\n')
            time.sleep(1)
            opcao = int(input('Olá, informe o que deseja!\n 1. Inserir nova tarefa\n 2. Editar tarefa\n 3. Visualizar todas as tarefas\n 4. Apagar tarefa\n 5. ordenar por ordem alfabética\n 6. Sair\n'))

        if opcao == 1:
            inserir()
        elif opcao == 2:
            editar()
        elif opcao == 3:
            listar_tarefas()
        elif opcao == 4:
            apagar()
        elif opcao == 5:
            ordenar()  
        elif opcao == 6:
         print('program encerrado até a próxima!')       

def inserir():
    tarefa = {}
    tarefa['titulo'] = input('Informe o título da tarefa que deseja inserir: ')
    for i in agenda:
          if i['titulo'] == tarefa['titulo']:
            print('ERRO: ESTA TAREFA JÁ EXISTE NA AGENDA, INSIRA UM TÍTULO DIFERENTE !')
            time.sleep(2)
            inserir()
            return  
               
    tarefa['data_inicio'] = input('Informe a data de início da tarefa: ')
    tarefa['data_termino'] = input('Informe a data de término da tarefa: ')
    tarefa['e-mail'] = input('Informe o e-mail do usuario: ')
    tarefa['tipo-telefone'] = input('Informe tipo de telefone (celular, fixo, residência ou trabalho): ')
    tarefa['telefone'] = input('Informe o telefone: ')
    tarefa['data-aniversario'] = input('Informe a data de aniversario: ')
    agenda.append(tarefa)
        
    print('Tarefa agendada com sucesso!')
    time.sleep(1)
          
    opcao = int(input('Para cadastrar mais uma tarefa digite 1 ou 2 para retornar ao menu principal: '))
    if opcao == 1:
           inserir()
    elif opcao == 2:
            menu()

def listar_tarefas():
    if not agenda:
        print('A agenda está vazia.')
        time.sleep(2)
        menu()
    else:
        for i, tarefa in enumerate(agenda):
            print(f'Tarefa {i+1}:')
            print(f'Título: {tarefa["titulo"]}')
            print(f'Data de Início: {tarefa["data_inicio"]}')
            print(f'Data de Término: {tarefa["data_termino"]}')
            print(f'E-mail: {tarefa["e-mail"]}')
            print(f'tipo-telefone: {tarefa["tipo-telefone"]}')
            print(f'telefone: {tarefa["telefone"]}')
            print(f'data-aniversario: {tarefa["data-aniversario"]}\n')
    time.sleep(1)
    menu()

def editar():
    opcao = int(input('Informe o número da tarefa que deseja editar, ou digite 0 para visualizar todas as tarefas: '))
    if opcao == 0:
        listar_tarefas()
        opcao = int(input('Informe o número da tarefa que deseja editar: '))
    if opcao > 0 and opcao <= len(agenda):
        tarefa = agenda[opcao - 1]  
        print(f'Editando Tarefa {opcao}:')
        tarefa['titulo'] = input('Informe o novo título da tarefa: ')
        tarefa['data_inicio'] = input('Informe a nova data de início da tarefa: ')
        tarefa['data_termino'] = input('Informe a nova data de término da tarefa: ')
        tarefa['e-mail'] = input('Informe o novo e-mail do usuário: ')
        tarefa['tipo_telefone'] = input('Informe o novo tipo de telefone: ')
        tarefa['telefone'] = input('Informe o novo telefone: ')
        tarefa['data_aniversario'] = input('Informe a nova data de aniversário: ')
        print('Tarefa editada com sucesso!')
        time.sleep(1)
        menu()
    else:
        print('Número de tarefa inválido.')    

def apagar():
    opcao = int(input('Informe o número da tarefa que deseja APAGAR, ou digite 0 para visualizar todas as tarefas: '))
    if opcao == 0:
        listar_tarefas()
        opcao = int(input('Informe o número da tarefa que deseja APAGAR: '))
        if opcao > 0 and opcao <= len(agenda):
            tarefa = agenda[opcao - 1]  
            print(f'VAMOS APAGAR A TAREFA {opcao}:')
            print(f'Título: {tarefa["titulo"]}')
            print(f'Data de Início: {tarefa["data_inicio"]}')
            print(f'Data de Término: {tarefa["data_termino"]}')
            print(f'E-mail: {tarefa["e-mail"]}')
            print(f'tipo-telefone: {tarefa["tipo-telefone"]}')
            print(f'telefone: {tarefa["telefone"]}')
            print(f'data-aniversario: {tarefa["data-aniversario"]}\n')
        deletar = int(input('para apagar a tarefa digite 1 ou 2 para retonar ao menu inicial'))
        if deletar == 1:
          del agenda[opcao-1]
          print('Tarefa apagada com sucesso!')
          time.sleep(1)
          menu()
    elif opcao != 0:
            if opcao > 0 and opcao <= len(agenda):
                tarefa = agenda[opcao - 1]  
                print(f'VAMOS APAGAR A TAREFA {opcao}:')
                print(f'Título: {tarefa["titulo"]}')
                print(f'Data de Início: {tarefa["data_inicio"]}')
                print(f'Data de Término: {tarefa["data_termino"]}')
                print(f'E-mail: {tarefa["e-mail"]}')
                print(f'tipo-telefone: {tarefa["tipo-telefone"]}')
                print(f'telefone: {tarefa["telefone"]}')
                print(f'data-aniversario: {tarefa["data-aniversario"]}\n')    
            deletar = int(input('para apagar a tarefa digite 1 ou 2 para retonar ao menu inicial'))
            if deletar == 1:
                del agenda[opcao-1]
                print('Tarefa apagada com sucesso!')
                time.sleep(1)
                menu()   
            
def ordenar():
    agenda_ordenada = sorted(agenda, key=lambda tarefa: tarefa["titulo"])  
    for i, tarefa in enumerate(agenda_ordenada):
        print(f'Título: {tarefa["titulo"]}')
        print(f'Data de Início: {tarefa["data_inicio"]}')
        print(f'Data de Término: {tarefa["data_termino"]}')
        print(f'E-mail: {tarefa["e-mail"]}')
        print(f'tipo-telefone: {tarefa["tipo-telefone"]}')
        print(f'telefone: {tarefa["telefone"]}')
        print(f'data-aniversario: {tarefa["data-aniversario"]}\n')    
        time.sleep(1)
        menu()

menu()
