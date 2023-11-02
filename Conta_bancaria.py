class ContaBancaria:
    def __init__(self,numero,saldo,nome,tipo):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.limite = 100
        self.status = False

    def ativoinativo(self):
        if self.status == False:
            print("A conta foi ativada")
            self.status = True
        else:
            print("A conta já está ativa")

    def limite(self,valor_limite):
        if self.limite == 0:
            self.limite = valor_limite * -1
            print("Foi adicionado o valor limite, em R$, de:",self.limite * -1)
        else:
            print("O limite da conta foi ativado")

    def depositar(self,valor_depositado):
        if valor_depositado > 0:
            self.saldo += valor_depositado
            print("O valor depositado foi de:",valor_depositado)
        else:
            print("Não dá pra depositar um valor negativo/nulo")

    def sacar(self, valor_sacado):
        if (self.saldo - valor_sacado) < self.limite:
            print("O valor sacado é maior do que o limite da conta")
            self.limite -= valor_sacado
        else:
            print("É possível sacar, e foi sacado R$",valor_sacado)
            self.saldo -= valor_sacado

    def verificarsaldo(self):
        if self.saldo > 0:
            print("Seu saldo é de:",self.saldo,"R$ e seu limite é de R$:",(self.limite * 1))
        else:
            print("Seu saldo é de 0 R$","e seu limite é de R$:",(self.limite-self.saldo))

pessoahumana = ContaBancaria(1923,0,"Lucas","Poupança")
pessoahumana.ativoinativo()
pessoahumana.depositar(30)
pessoahumana.sacar(100)
pessoahumana.verificarsaldo()
