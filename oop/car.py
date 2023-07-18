class CarClass:
    info = 'Описание класса Машина'

    def __init__(self, vendor, model, year):
        self.vendor = vendor
        self.model = model
        self.year = year
        self.odometr = 0

    def show_full_name(self):
        print(f'{self.vendor} {self.model} {self.year} года выпуска')

    def update_odometr(self, km):
        if km <= 0:
            print('Недопустимое значение')
        else:
            self.odometr += km
            print(f'Новое значение пробега {self.odometr} км')

    def move(self, km):
        if km <= 0:
            print('Недопустимое значение')
        else:
            print(f'Машина проехала {km} км')
            self.update_odometr(km)


"""car1 = CarClass('BMW', 'X6', 2018)
car2 = CarClass(vendor='Toyota', model='Camry', year=2003)
'''CarClass.info = 'Новое Описание класса Машина'
print(car1.info)
print(car2.info)'''
car1.show_full_name()
car2.show_full_name()
car1.update_odometr(-100)
car1.update_odometr(1)
car1.move(500)"""