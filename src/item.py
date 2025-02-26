import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            print("Можно складывать только экземпляры классов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
        else:
            self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        try:
            with open(file, encoding='windows-1251') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                count = 0
                item_all = []
                for row in reader:
                    if count == 0:
                        count += 1
                    else:
                        item_all.append(cls(row[0], row[1], row[2]))
            cls.all = item_all
        except FileNotFoundError:
            print(f'Отсутствует файл {file}')
            raise
        except IndexError:
            raise InstantiateCSVError(f'Файл {file} поврежден')
            # print(f'Файл {file} поврежден')

    @staticmethod
    def string_to_number(string_number):
        if string_number.isdigit():
            return int(string_number)
        else:
            return int(float(string_number))


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.args = args
        print(self.args)
