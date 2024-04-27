import csv
import os
from datetime import datetime
import time

agenda = []

def menu():
    print(f'TAMANHO AGENDA: {len(agenda)}')
    opcao = int(input('Olá, informe o que deseja:\n 1. Inserir nova tarefa\n 2. Editar tarefa\n 3. Visualizar todas as tarefas\n 4. Apagar tarefa\n 5. Ordenar por nome\n 6. Aniversariantes do dia\n 7. Sair\n'))
    while opcao < 1 or opcao > 7:
        print('OPÇÃO INVÁLIDA! Insira um número de 1 a 7\n')
        opcao = int(input('Olá, informe o que deseja:\n 1. Inserir nova tarefa\n 2. Editar tarefa\n 3. Visualizar todas as tarefas\n 4. Apagar tarefa\n 5. Ordenar por nome\n 6. Aniversariantes do dia\n 7. Sair\n'))

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
        aniversariantes_do_dia()
    elif opcao == 7:
        print('Programa encerrado até a próxima!')
    elif opcao == 8:
        print("ler dados")    
        

def inserir():
    tarefa = {}
    tarefa['titulo'] = input('Informe o título da tarefa que deseja inserir: ')
    if any(x['titulo'] == tarefa['titulo'] for x in agenda):
        print('ERRO: ESTA TAREFA JÁ EXISTE NA AGENDA, INSIRA UM TÍTULO DIFERENTE!')
        return inserir()
        
    tarefa['data_inicio'] = input('Informe a data de início da tarefa (dd/mm/aaaa): ')
    tarefa['data_termino'] = input('Informe a data de término da tarefa (dd/mm/aaaa): ')
    tarefa['e-mail'] = input('Informe o e-mail do usuário: ')
    tarefa['tipo_telefone'] = input('Informe tipo de telefone (celular, fixo, residência ou trabalho): ')
    tarefa['telefone'] = input('Informe o telefone: ')
    tarefa['data_aniversario'] = input('Informe a data de aniversário (dd/mm/aaaa): ')
    agenda.append(tarefa)
    grava()
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
        for i, tarefa in enumerate(agenda, 1):
            print(f'Tarefa {i}:')
            print(f'Título: {tarefa["titulo"]}')
            print(f'Data de Início: {tarefa["data_inicio"]}')
            print(f'Data de Término: {tarefa["data_termino"]}')
            print(f'E-mail: {tarefa["e-mail"]}')
            print(f'Tipo de telefone: {tarefa["tipo_telefone"]}')
            print(f'Telefone: {tarefa["telefone"]}')
            print(f'Data de aniversário: {tarefa["data_aniversario"]}')
            print()
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
        tarefa['data_inicio'] = input('Informe a nova data de início da tarefa (dd/mm/aaaa): ')
        tarefa['data_termino'] = input('Informe a nova data de término da tarefa (dd/mm/aaaa): ')
        tarefa['e-mail'] = input('Informe o novo e-mail do usuário: ')
        tarefa['tipo_telefone'] = input('Informe o novo tipo de telefone: ')
        tarefa['telefone'] = input('Informe o novo telefone: ')
        tarefa['data_aniversario'] = input('Informe a nova data de aniversário (dd/mm/aaaa): ')
        print('Tarefa editada com sucesso!')
        menu()
    else:
        print('Número de tarefa inválido.')

def apagar():
    opcao = int(input('Informe o número da tarefa que deseja APAGAR, ou digite 0 para visualizar todas as tarefas: '))
    if opcao == 0:
        listar_tarefas()
        opcao = int(input('Informe o número da tarefa que deseja APAGAR: '))
    if opcao > 0 and opcao <= len(agenda):
        del agenda[opcao - 1]
        print('Tarefa apagada com sucesso!')
    else:
        print('Número de tarefa inválido.')
    menu()

def ordenar():
    agenda.sort(key=lambda x: x['titulo'])
    print('Agenda ordenada por título.')
    listar_tarefas()

def aniversariantes_do_dia():
    hoje = datetime.now().strftime('%d/%m')
    aniversariantes = [tarefa for tarefa in agenda if tarefa['data_aniversario'] == hoje]
    if aniversariantes:
        print('Aniversariantes do dia:')
        for aniversariante in aniversariantes:
            print(f'Título: {aniversariante["titulo"]}')
            print(f'Data de Aniversário: {aniversariante["data_aniversario"]}')
            print()
    else:
        print('Não há aniversariantes hoje.')
    menu()

def grava():
    with open('agenda.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['titulo', 'data_inicio', 'data_termino', 'e-mail', 'tipo_telefone', 'telefone', 'data_aniversario'])
        writer.writeheader()
        writer.writerows(agenda)

def le():
    if os.path.exists('agenda.csv'):
        with open('agenda.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                agenda.append(row)

le()  # Lê os dados da agenda do arquivo CSV, se existir
menu()  # Inicia o programa
