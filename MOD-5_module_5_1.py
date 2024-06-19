
# Задача "Developer - не только разработчик"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print(f'В "{self.name}" такого этажа не существует!')


devGreen = House('ЖК Грин-Сити', 17)
devVnuk = House('ЖК Новое-Внуково', 12)
print('------------------------------------------------')
print(f'В "{devGreen.name}"-{devGreen.floors} этажей ')
print(f'В "{devVnuk.name}"-{devVnuk.floors} этажей ')
print('------------------------------------------------')
devGreen.go_to(11)
print('------------------------------------------------')
devVnuk.go_to(13)
print('------------------------------------------------')



