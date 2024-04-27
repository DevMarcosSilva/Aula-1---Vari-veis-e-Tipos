class ContaBancaria:
    def  __init__(self,numero_agencia,tipo_conta,saldo,limite):
        self.numero_agencia = numero_agencia
        self.tip_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
    
    def consultar_saldo(self):
        print(f"O saldo é: {self.saldo}")    
        
 
 
 
Conta = input(f'informe o num da agen ',ContaBancaria())

print(Conta.saldo)    
'''
 def sacar(self,valor):
        return "o valor sacado foi {}\n seu saldo agora é {}".format(self.saldo)
    
    def depositar(self,valor):
        print(f'qual é o valor que deseja depositar?')  
    
    def transfere_para(self,destino,valor):
        #terminar
    
    def obter_extrato(self):    
        #terminar
    
    def alterar_titular(self,novo_titular) :     
        #terminar
    
    def fechar_conta(self) :     
      
        
class historico:
    d        
'''