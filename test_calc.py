import time
import pytest
from decorators import time_counter


@time_counter
def test_calc_addition(dlg):
    dlg.child_window(auto_id="num1Button", control_type="Button").click()
    dlg.child_window(auto_id="plusButton", control_type="Button").click()
    dlg.child_window(auto_id="num1Button", control_type="Button").click()
    dlg.child_window(auto_id="equalButton", control_type="Button").click()
    # dlg.type_keys('1+1=')
    answer = dlg.child_window(auto_id="CalculatorResults", control_type="Text")
    assert answer.window_text().split()[2] == '2', 'Addition error'


@time_counter
def test_calc_subtraction(dlg):
    dlg.type_keys('3-1=')
    answer = dlg.child_window(auto_id="CalculatorResults", control_type="Text")
    assert answer.window_text().split()[2] == '2', 'Subtraction error'


@time_counter
def test_calc_multiply(dlg):
    dlg.type_keys('4*3=')
    answer = dlg.child_window(auto_id="CalculatorResults", control_type="Text")
    assert answer.window_text().split()[2] == '12', 'Multiply error'


@time_counter
def test_calc_divide(dlg):
    dlg.type_keys('9/3=')
    answer = dlg.child_window(auto_id="CalculatorResults", control_type="Text")
    assert answer.window_text().split()[2] == '3', 'Divide error'


# dlg.print_control_identifiers()



