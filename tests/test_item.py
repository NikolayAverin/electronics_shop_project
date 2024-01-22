"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import *

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000