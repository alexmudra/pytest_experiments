#https://www.youtube.com/watch?v=1HtEPEn4-LY
from utils.test_div_func import division
import pytest

@pytest.mark.parametrize('f_st_value, second_value, expected_result', [(10, 5, 2),
                                                                       (20, 5, 4),
                                                                       (100, 20, 5),
                                                                       (-10, 5, -2)])
def test_div_positive_with_2_int(f_st_value, second_value, expected_result ):
    assert division(f_st_value, second_value) == expected_result


# @pytest.mark.parametrize('f_st_value, second_value', [(10, 0)])
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        division(20, 0)

def test_TypeError():
    with pytest.raises(TypeError):
        division(20, 'str')