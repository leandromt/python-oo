class Account:

    def __init__(self, number):
        self.__number = number
        # private self.total = total
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        if self.__total >= value:
            self.__total -= value
            self.__total -= 1

    def get_total(self):
        return self.__total


class Account2(Account):

    def __init__(self, number, cvv):
        super(Account2, self).__init__(number)
        self.__cvv = cvv

    def withdraw(self, value):
        # _Account_total - Acesso o atributo privado da classe pai
        if self._Account__total >= value:
            self._Account__total -= value
            self._Account__total -= 2

    def get_cvv(self):
        return self.__cvv
