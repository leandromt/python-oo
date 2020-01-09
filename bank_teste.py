import bank

b = bank.Account('123-12', 50)
# print(b.number)
# print(b.total)
# print()
#
# print('----- DEPOSITO -------')
# b.deposit(500)
# print(b.number)
# print(b.total)
# print()
# print('----- SAQUE -------')
# print()
# b.withdraw(200)
# print(b.number)
# print(b.total)
#
# print('----- EXTRATO -------')
# print()
# print(b.get_total())

# COM MODIFICADORES DE ACESSO
b.withdraw(200)
print(b.get_total())

