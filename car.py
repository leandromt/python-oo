# classes sempre comelam com letras maiusculas
class Car:

    # variaveis de classe | atributo generalista
    quantidade_rodas = 4

    # metodo construtor e variaveis do objeto
    def __init__(self, cor, fabricante, ano, km):
        # atributos de instancia
        self.cor = cor
        self.fabricante = fabricante
        self.ano = ano
        self.km = km

    # metodo de instancia
    # tem acesos aos atributos da instancia (self)
    def drive(self):
        print(f'Começou a dirigir o {self.fabricante}')

    # metodo estatico
    # generelista e nao acessa os atributos da instancia
    @staticmethod
    def buzina():
        print('Bibi bi bi bi...')

    # metodo de classe
    # tem acesso aos atributos da classe
    @classmethod
    def show_qtde_rodas(cls):
        print(cls.quantidade_rodas)
