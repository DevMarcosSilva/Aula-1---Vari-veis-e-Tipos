#Faça um programa que leia uma expressão com parênteses. Usando
#pilhas, verifique se os parênteses foram abertos e fechados na ordem
#correta.
#Exemplo:
#(()) OK
#()()(()()) OK
#( ) ) Erro


def verifica_parentheses(expressao):
    
    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            
            if not pilha:
                return False
            else:
            
                pilha.pop()

    
    return not pilha

expressao = input("Digite a expressão com parênteses: ")


if verifica_parentheses(expressao):
    print("Os parênteses estão ok.")
else:
    print("Erro!")


