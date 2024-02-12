from src.item import Item
from config import *

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('item.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(ITEMS_WITHOUT_COLLUMS)
    # InstantiateCSVError: Файл item.csv поврежден
