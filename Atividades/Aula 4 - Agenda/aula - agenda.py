lista_contatos =[]

def menu():
    ope= input("""
                    MENU DE OPÇÃO 
                    1-SALVAR CONTATO;
                    2- ALTERAR CONTATO;
                    3-BUSCAR CONTATO;44
                    4-APAGAR CONTATO;
                    5-LISTAR CONTATOS;
                    0-SAIR DA AGENDA
    """
    )
    return ope

def salvarcontato(**kwargs):
    lista_contatos.append(kwargs)
    return print(f'Contato de {kwargs["nome"]}, foi salvo com sucesso')

def alterarcontato(nome,*args):
    for i,contato in enumerate(lista_contatos):
        if contato['nome']==nome:    
            for key in enumerate(contato.keys()):
                if args[i]!=None:
                    contato[key]=args[i]