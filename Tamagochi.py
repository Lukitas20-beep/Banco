class Tamagochi:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self):
        if self.comendo == True:
            print(self.nome,"já está comendo")
            self.comendo = False
        elif self.dormindo == True:
            print(self.nome,"não pode comer, pois está dormindo")
        elif self.falando == True:
            print(self.nome,"não pode comer, pois está falando")
        else:
            print(self.nome,"começou a comer")
            self.comendo = True

    def falar(self):
        if self.falando == True:
            print(self.nome,"já está falando")
            self.falando = False
        elif self.dormindo == True:
            print(self.nome,"não pode falar, pois está dormindo")
        elif self.comendo == True:
            print(self.nome,"não pode falar, pois está comendo")
        else:
            print(self.nome,"começou a falar")
            self.falando = True

    def dormir(self):
        if self.dormindo == True:
            print(self.nome,"já está dormindo")
            self.dormindo = False
        elif self.falando == True:
            print(self.nome,"não pode dormir, pois está falando")
        elif self.comendo == True:
            print(self.nome,"não pode dormir, pois está comendo")
        else:
            print(self.nome,"começou a dormir")
            self.dormindo = True

    def apresentar(self):
        print("Meu nome é:",self.nome,"Minha idade é:",self.idade,"E peso:",self.peso,"kg")

p1 = Tamagochi("Lucas",78,19)
p1.comer()
p1.dormir()
p1.falar()
p1.apresentar()
