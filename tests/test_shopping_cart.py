import pytest

from src.shopping_cart import ShoppingCart


# 1. Создание фикстуры
@pytest.fixture
def filled_cart():
    """Создает и возвращает корзину с двумя товарами."""
    # 2. Здесь код ПОДГОТОВКИ (Setup)
    cart = ShoppingCart()
    cart.add_item("apple", price=10)
    cart.add_item("banana", price=20)
    # 3. Вернуть подготовленный объект
    return cart


# 4. Текст, который запрашивает фикстуру
def test_add_item(filled_cart):
    # 'filled_cart' - здесь это тот самый объект 'cart', который вернула фикстура
    filled_cart.add_item("cherry", price=30)
    assert "cherry" in filled_cart.items


def test_get_total_price(filled_cart):
    # Можно использовать ту же самую фикстуру в другом тесте
    assert filled_cart.get_total_price() == 30
