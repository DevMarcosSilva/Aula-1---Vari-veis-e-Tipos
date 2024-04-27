class ContaBancaria:
    def  __init__(self,numero_agencia,tipo_conta,saldo,limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.Lista_tip_conta = ['Corrente','Poupança','Salário']
        if self.tipo_conta in self.Lista_tip_conta:
            self.tipo_conta == self.Lista_tip_conta
        else:
            raise Exception('conta invalida')       
        self.saldo = saldo
        self.limite = limite
    
    def consultar_saldo(self):
        print(f"O saldo é: {self.saldo}")    
    
    def sacar(self):
        sacar = int(input('Informe o valor que deseja sacar: '))
        saldoFinal = self.saldo-sacar 
        print(f'Seu saldo agora é {saldoFinal}')
        
'''    
    def depositar(self,valor):
        print(f'qual é o valor que deseja depositar?')  
    
    def transfere_para(self,destino,valor):
        #terminar
    
    def obter_extrato(self):    
        #terminar
    
    def alterar_titular(self,novo_titular) :     
        #terminar
    
    def fechar_conta(self) :     
'''      
                
        