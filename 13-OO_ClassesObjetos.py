class Zoo:
    leao = 5


animal = Zoo()
print(animal.leao)

print('\n')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print('Bem-vindo {}.'.format(self.nome))


homem = Pessoa('Allyson', 18)

homem.saudacao()


print('\n')


class Planta:
    def __init__(this, nome, altura):
        this.nome = nome
        this.altura = altura

    def descricao(this):
        print('A planta {} possui um altura de {}cm.'.format(this.nome, this.altura))


vegetal = Planta('CENOURA'.lower(), '20')
vegetal.descricao()


print('\n')


class Eu:
    def __init__(self, nome, idade, faculdade):
        self.nome = nome
        self.idade = idade
        self.faculdade = faculdade

    def verificar(self):
        if self.nome != 'Allyson':
            print('Seu nome é {}'.format(self.nome))
        else:
            print('Seu nome é Allyson, possui {} e estuda na {}.'.format(self.idade, self.faculdade))


zharfi = Eu('allyson'.capitalize(), 18, 'udf'.upper())

zharfi.idade = 25
zharfi.faculdade = 'UNB'
# del zharfi.idade
zharfi.verificar()
