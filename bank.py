class Account:

    def __init__(self, number, total):
        self.__number = number
        # private self.total = total
        self.__total = total

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        if self.__total >= value:
            self.__total -= value

    def get_total(self):
        return self.__total
