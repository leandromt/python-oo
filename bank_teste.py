import bank

# b = bank.Account('123-12')
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
c1 = bank.Account('123-12')
c1.deposit(250)
c1.withdraw(200)
print(c1.get_total())


# DETALHAMENTO DA CLASSE
print(type(c1))
print(c1.__class__)


# HERANÇA
c2 = bank.Account2('321-21', 123)
c2.deposit(250)
c2.withdraw(200)
print(c2.get_cvv())
print(c2.get_total())
