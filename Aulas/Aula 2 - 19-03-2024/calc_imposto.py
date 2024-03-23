# Um problema comum é quando temos de pagar Imposto de Renda. 
# Normalmente, pagamos o Imposto de Renda por faixa de salário. 
# Imagine que, para salários menores que R$ 1.000,00, não teríamos imposto a pagar, ou seja, alíquota 0%. 
# Para salários entre R$ 1.000,00 e R$ 3.000,00, pagaríamos 20%. 
# Acima desses valores, a alíquota seria de 35%. 
# Quem ganha R$ 4.000,00 tem os primeiros R$ 1.000,00 isentos de imposto; com o montante entre R$1.000,00 e R$ 3.000,00 pagando 20%, e o restante pagando os 35%.

salario = int(input('Informe o seu salário: '))


def calcular_imposto():
    if salario == 1000:
        print('Não tem imposto')
    
    elif salario >= 1000 or salario <= 3000:
         imposto = salario * 0.20 
         print(imposto)  

calcular_imposto()