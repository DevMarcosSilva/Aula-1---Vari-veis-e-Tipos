class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.registrar_transacao(f"Saque: R${valor}")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def depositar(self, valor):
        self.saldo += valor
        self.historico.registrar_transacao(f"Depósito: R${valor}")

    def transfere_para(self, destino, valor):
        if self.sacar(valor) and isinstance(destino, ContaBancaria) and hasattr(destino, 'depositar'):
            destino.depositar(valor)
            self.historico.registrar_transacao(f"Transferência para {destino}: R${valor}")
            return True
        else:
            return False


    def obter_extrato(self):
        self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular

    def fechar_conta(self):
        self.titular = None
        self.saldo = 0


class Historico:
    def __init__(self):
        self.data_da_abertura = "Data de abertura: "
        self.transacoes = []

    def registrar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def imprime(self):
        print("Histórico de transações:")
        for transacao in self.transacoes:
            print(transacao)


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        return f"Nome: {self.nome} {self.sobrenome}, CPF: {self.cpf}"


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self):
        juros = self.saldo * 0.01  # Exemplo de cálculo de juros mensal
        self.depositar(juros)


class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.historico.registrar_transacao(f"Utilização do cheque especial: R${valor}")
            return True
        else:
            print("Saldo insuficiente e limite de cheque especial ultrapassado.")
            return False
