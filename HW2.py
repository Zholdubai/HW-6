class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    current_balance = 0

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


boby = Jack('Boby', 'Smith', '012345678', 100)


class Vito(Jack):
    _n_number = 50

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def balanc(self):
        a = boby.balance - self._n_number
        final = self.balance + a
        print(f'Balance:',final)


dan = Vito('Dan', 'Trump', '987654321', 50)
Vito.balanc(dan)