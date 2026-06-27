import pytest

from src.calculator import add, divide


@pytest.mark.smoke
def test_add():
    assert add(2, 3) == 5


def test_equality():
    assert 5 == 5


def test_inequality():
    assert 5 != 6


def test_greater_than():
    assert 10 > 5


def test_less_or_equal():
    assert 3 <= 3


# ! Проверка на истинность (Truthiness)
# ! Проверить что что-то существует (не является None, False, 0 или пустой коллекцией).
def test_string_is_truthy():
    # Непустая строка - это True в логическом контексте
    assert "hello"


def test_list_is_truthy():
    # Непустой список - это True
    assert [1, 2, 3]


# ! Проверка на ложность (Falsiness)
# ! Проверить что значение является ложным (falsy) - то есть это 0, None, False, "", [] и т.д..
def test_empty_list_is_falsy():
    # Пустой список - это False в логическом контексте
    # not False -> Ture, поэтому assert проходит
    assert not []


def test_zero_is_falsy():
    assert not 0


# ! Проверка на вхождение (int)
def test_item_in_list():
    my_list = ["apple", "banana", "cherry"]
    assert "banana" in my_list


def test_substring_in_string():
    greeting = "Hello, world!"
    assert "world" in greeting


# ! Комбинированные проверки
def test_complex_expression():
    x = 10
    assert x > 5 and x % 2 == 0


"""
! Тесты для ошибочных ситуаций
"""


def test_add_raises_type_error_on_string_input():
    with pytest.raises(TypeError):
        add(5, "hello")


"""
! Тесты для деления
"""


# ! Проверить что текст ошибки содержит нужную фразу
def test_divide_by_zero_raises_valuer_error_with_message():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    # Проверить что текст ошибки содержит нужную фразу
    assert "Нельзя делить на ноль" in str(excinfo.value)


"""
! Маркировка тестов.

Чтобы официально "зарегистрировать" маркеры и убрать в выводе pytest предупреждения о неизвестных маркерках,
нужно создать в корневой папке проекта конфигурационный файл pytest.ini и перечислить их там.
"""


@pytest.mark.regression
def test_divide():
    assert divide(10, 2) == 5


@pytest.mark.regression
def test_divide_by_zero_raises_value_error_with_message():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)

    assert "Нельзя делить на ноль" in str(excinfo.value)


@pytest.mark.slow
def test_very_slow_calculation():
    """Гипотетический тест, который работает очень долго."""
    # Для примера он будет просто успешным
    assert True


@pytest.mark.smoke
@pytest.mark.regression
def test_critical_function():
    """
    ! Пример как применить нескольких маркеров к одному тесту
    ! Этот тест является и дымовым, и регрессионным.
    """
    assert True


"""
Встроенные маркеры skip, skipif.
! Всегда нужно указывать почему тест пропускается.

Чтобы увидеть пропущеные тесты с причинами пропуска и отдельно от работающих тестов,
нужно ввести в командной строке:
! pytest -rs
    или:
! pytest -v
"""
import sys


@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0")
def test_subtraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Требуется Python 3.10 или выше")
def test_new_python_feature():
    """Тест, использующий синтаксис, доступный только в новых версиях Python."""
    # Пример использования match-case, который появился в Python 3.10
    result = 0
    match 1:
        case 1:
            result = 1

    assert result == 1


"""
Встроенный маркер xfail (ожидаемый провал).
! Этот маркер говорит Pytest: "Я знаю, что этот тест сейчас падает, и это нормально.
! Запусти его, но не считай его падение провалом всей тестовой сессии.
! Просто отметь, что он провалился, как и ожидалось".
Основной сценарий использования xfail — тестирование известного бага в основном коде.
"""


@pytest.mark.xfail(
    reason="Известный баг с точностью float, будет исправлени в #TICKET-123"
)
def test_add_floats_bug():
    # Этот тест будет падать из-за особенностей представления float в Python
    assert add(0.1, 0.2) == 0.3


"""
Запуск тестов по маркерам с помощью флага -m.
! Синтаксис запуска тестов помеченных маркерами:
!    pytest -m <имя_маркера>
    Например:
!    pytest -m regression -v

Можно комбинировать какие тесты запускать испольну логические операторы: not, and, or.
    Примеры использования:
- запустить все тесты кроме медленных:
!    pytest -m "not slow"
- запустить только те тесты, которые имеют оба маркера и smoke и regression:
!    pytest -m "smoke and regression" -v
- запустить тесты, имеющие хотя бы один из маркеров.
Запустятся и "дымовые", и "регрессионные" тесты за один раз:
!    pytest -m "smoke or regression" -v
"""


"""
! ФИКСТУРЫ.
"""


# Напишите одну фикстуру и два теста, которые ее используют
@pytest.fixture
def sample_order():
    return {"order_id": 42, "amount": 99.90, "currency": "USD"}


def test_order_id(sample_order):
    assert sample_order.get("order_id") == 42


def test_order_currency(sample_order):
    assert sample_order.get("currency") == "USD"
