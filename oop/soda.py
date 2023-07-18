class Soda:
    def __init__(self, ingredient=None):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('малина')
drink1.show_my_drink()
drink2.show_my_drink()