"""Документация для ООП
Создается класс в каком - то общем смысле
Например Knife, у нее есть общие свойства по типу - материал клинка, материал ручки, цвет ручки и тд
А вот Forging имеющая рукоядку из слоновой кости,с синим цветом рукоядки, сделана из стали 65Х13  -->
будет являться ОБЪЕКТОМ класс Knife
"""


# Пример

class KnifeEitor:
    def __init__(self, steel, collorhandle,
                 handle):                  # функция (def)__init__ выступает своего рода кузней в которой куется нож (обжигается сталь, создается ручка и цвет)
        self.steel_material = steel        # Self определяет ключевое свойство объекта
        self.collor_handle = collorhandle
        self.handle_material = handle

                                           # Self у функции обозначает принадлежность к классу
    def forging_craft(self,
                      full_coast):         # Функции которые определенны в классе называют методом класс например: Forging_Craft Является методом класса
        print(
            f"Нож куется из стали {self.steel_material}, цвет ножа {self.collor_handle}, с рукоядкой из {self.handle_material}. Стоимость его { full_coast}")


                                           # ВСЕ ЭТО НАЗЫВАЮТ ИНКАПСУЛЯЦИЕ (Упаковка данных и функционала внутри одного объекта)

finka_nkvd = KnifeEitor("65Х13", "Красный", "Слоновая кость")

print(finka_nkvd.steel_material)
print(finka_nkvd.handle_material)
print(finka_nkvd.collor_handle)

finka_nkvd.forging_craft("10000$")

                                           # Создаем наследование для нового ножа который будет дополнен функционалом
