class contaBancaria:
    def __init__(self, numero,saldo,nome,tipo,limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.status = True

    def verificarSaldo(self):
        print("Seu saldo é de R$:",self.saldo)

    def depositar(self,valordepositado):
        self.saldo += valordepositado
        print("O valor depositado foi de R$:",valordepositado)
        self.verificarSaldo()

    def sacar(self,valorsacado):
        if valorsacado > self.limite:
            print("É possível sacar pois tem R$:",self.limite,"no banco, e o valor de saque R$:",valorsacado, 'é viável')
        elif valorsacado > self.saldo:
            print("Não é possível sacar, pois R$:",valorsacado,"é mais do que tem no banco R$:",self.limite)
        else:
            self.saldo -= valorsacado
            print("Foi sacado R$:", valorsacado)
            self.verificarSaldo()

    def contaAtivaInativa(self):
        if self.status == False:
            print("A conta agora está ativa")
            self.status = True
        else:
            print("A conta já está ativa")


conta1 = contaBancaria(12345,4000,"lucas","Poupança",8000)
conta1.contaAtivaInativa()
conta1.verificarSaldo()
conta1.sacar(700)
conta1.depositar(10)
