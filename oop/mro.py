class Archer:
    def attack(self):
        print('Стреляет из лука')


class Warrior:
    def attack(self):
        print('Бьет мечом')

    def shield_up(self):
        print('Закрывается щитом')


class MovementMixIn:
    def move(self, m):
        print(f'Игрок прошел {m} метров')


class MultiClass(Archer, Warrior, MovementMixIn):
    pass


player = MultiClass()
player.attack()
player.shield_up()
player.move(6)
