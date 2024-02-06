"""Здесь надо написать тесты с использованием pytest для модуля item."""
from config import *
from src.phone import *


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"

    item1.name = "Smartphone"
    assert item1.name == "Smartphone"

    item1.name = "Суперсмартфон"
    assert item1.name == "Суперсмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ITEMS)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('12.9') == 12


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert item1 + 5 is None
