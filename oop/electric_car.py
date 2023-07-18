from car import CarClass


class Battery:
    def __init__(self, charge=100):
        self.charge = charge
        self.name = 'Батарейка'

    def show_charge_level(self):
        return f'Уровень заряда батареии: {self.charge}'


class ElectricCar(CarClass):
    info = 'Класс с описанием электромобиля'

    def child_method(self):
        print('Метод класса-наследника')

    def __init__(self, vendor, model, year):
        super().__init__(vendor, model, year)
        self.battery = Battery()

    def show_full_name(self):
        print(f'{self.vendor} {self.model} {self.year} года выпуска. {self.battery.show_charge_level()}')


car1 = ElectricCar('Tesla', 'S', 2023)
car2 = CarClass(vendor='Toyota', model='Camry', year=2003)
car1.show_full_name()

