# task 3


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def get_ful_name(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        print(f'Имя сотрудника :{surname + " " + name} , должность: {position}')

    def get_total_income(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        print(f'Доход:{wage + bonus}')


p = Position()
p.get_ful_name('Игрорь', 'Захаров', 'слесарь')
p.get_total_income(1000, 100)

