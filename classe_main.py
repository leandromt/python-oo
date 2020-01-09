from car import Car

carro = Car('Vermelho', 'Fiat', 2019, 50)
print('Carro do leandro')
print(carro.cor)
print(carro.fabricante)
print(carro.ano)
print(carro.km)
print(carro.quantidade_rodas)
carro.show_qtde_rodas()
carro.drive()
carro.buzina()


print()
print()

carro2 = Car('Branco', 'Pegout', 2014, 115)
print('Carro da juliana')
print(carro2.cor)
print(carro2.fabricante)
print(carro2.ano)
print(carro2.km)
print(carro2.quantidade_rodas)
carro2.drive()
carro2.buzina()
carro2.show_qtde_rodas()
