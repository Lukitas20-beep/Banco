class Animal():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def som(self):
        print(self.nome,"fez um som")

    def comer(self):
        print(self.nome,"foi comer")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(self.nome,"miou")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def mugir(self):
        print(self.nome,"mugiu")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def somdecoelho(self):
        print(self.nome,"está fazendo sons de coelho")

gato = Gato("Adamastor Nostredamus","roxo")
gato.miar()
gato.comer()
vaca = Vaca("Mimosa","azul")
vaca.mugir()
vaca.comer()
coelho = Coelho("Roberto, o coelho","lilás")
coelho.somdecoelho()
coelho.comer()
