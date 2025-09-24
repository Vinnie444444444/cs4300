import pytest
from src.task4 import calculate_discount
#the data that will be tested
@pytest.mark.parametrize("price, discount, expected", [
    (100, 10, 90),
    (50.0, 25, 37.5),
    (200, 0, 200),
    (200, 100, 0)
])
def test_discount_values(price, discount, expected):
    assert calculate_discount(price, discount) == expected
#sned a price and a discount
def test_invalid_inputs():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)
    with pytest.raises(TypeError):
        calculate_discount(100, "10")
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
    with pytest.raises(ValueError):
        calculate_discount(100, 105)

