from src.item import *


class Language:
    all_language = ['EN', 'RU']

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Language, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
