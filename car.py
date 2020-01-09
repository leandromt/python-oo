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
    def drive(self):
        print(f'Começou a dirigir o {self.fabricante}')
