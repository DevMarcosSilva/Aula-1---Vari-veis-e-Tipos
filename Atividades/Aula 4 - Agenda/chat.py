import time

agenda = []

def menu():
    opcao = int(input('Olá, informe o que deseja!\n 1. Inserir nova tarefa\n 2. Editar tarefa\n 3. Visualizar todas as tarefas\n 4. Apagar tarefa\n 5. Sair da agenda\n'))
    while opcao < 1 or opcao > 5:
        print('OPÇÃO INVÁLIDA! Insira um número de 1 a 5\n')
        time.sleep(1)
        opcao = int(input('Olá, informe o que deseja!\n 1. Inserir nova tarefa\n 2. Editar tarefa\n 3. Visualizar todas as tarefas\n 4. Apagar tarefa\n 5. Sair da agenda\n'))

    if opcao == 1:
        inserir()
    elif opcao == 3:
        listar_tarefas()

def inserir():
    tarefa = {}
    tarefa['titulo'] = input('Informe o título da tarefa que deseja inserir: ')
    tarefa['data_inicio'] = input('Informe a data de início da tarefa: ')
    tarefa['data_termino'] = input('Informe a data de término da tarefa: ')
    tarefa
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
    else:
        for i, tarefa in enumerate(agenda):
            print(f'Tarefa {i+1}:')
            print(f'Título: {tarefa["titulo"]}')
            print(f'Data de Início: {tarefa["data_inicio"]}')
            print(f'Data de Término: {tarefa["data_termino"]}\n')
    

menu()
