from a01 import *
import pytest

@pytest.mark.parametrize("test_input, expected", [(5, ['78.50', '31.40'])])
def test_eval1(test_input, expected):
    c1 = Circle(test_input)
    assert c1.Display() == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [('abc', 123, ('abc', 123))])
def test_eval2(test_input1, test_input2, expected):
    s1 = Student(test_input1, test_input2)
    assert s1.display() == expected

@pytest.mark.parametrize("test_input, expected", [(25, '77.00')])
def test_eval3(test_input, expected):
    t =Temperature()
    assert t.convertFahrenhiet(test_input) == expected or t.convertCelsius(test_input)==expected

@pytest.mark.parametrize("test_input, expected", [([0,1],[[], [1], [0], [0, 1]])])
def test_eval4(test_input, expected):
    assert Subset().sub_sets(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [((10,20,30,40,50,60,70),50,[(1, 2), (0, 3)])])
def test_eval5(test_input1, test_input2, expected):
    assert Sum().twoSum(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [([-25, -10, -7, -3, 2, 4, 8, 10],[[-10, 2, 8], [-7, -3, 10]])])
def test_eval6(test_input, expected):
    assert SumEqualsZero().threeSum(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [('V',5)])
def test_eval7(test_input, expected):
    assert RomanToInt().roman_to_int(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(500,500)])
def test_eval8(test_input, expected):
    assert BankAccount().deposit(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(500,5000)])
def test_eval9(test_input, expected):
    b = BankAccount()
    b.deposit(5500)
    assert b.withdraw(test_input) == expected

@pytest.mark.parametrize("test_input, expected", 
[(6000, 'Sorry, minimum balance must be maintained.')])
def test_eval10(test_input, expected):
    m = MinimumBalanceAccount()
    m.deposit(10000)
    assert m.withdraw(test_input) == expected