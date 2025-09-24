import pytest
import src.task2 as task2

@pytest.mark.parametrize("var, expected_type", [
    (task2.int_var, int),
    (task2.float_var, float),
    (task2.string_var, str),
    (task2.bool_var, bool)
])
def test_data_types(var, expected_type):
    #checking if the varaibles have the expected variable types
    assert isinstance(var, expected_type)

