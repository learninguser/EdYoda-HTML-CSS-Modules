from ipynb.fs.full.assignment import *
import pytest

@pytest.mark.parametrize("test_input1, test_input2, expected", [(Time(2, 50), Time(1, 20), "4:10")])
def test_eval1(test_input1, test_input2, expected):
    c = Time.addTime(test_input1, test_input2)
    assert c.displayTime() == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", 
[
    (2,2,4)
])
def test_eval2(test_input1, test_input2, expected):
    assert Pow().pow(test_input1, test_input2) == expected


@pytest.mark.parametrize("test_input, expected", [('Edyoda', 'adoydE')])
def test_eval3(test_input, expected):
    assert Reverse().reverse_words(test_input) == expected

@pytest.mark.parametrize("test_input, expected", 
[
    ("{[}(()", False)
])
def test_eval4(test_input, expected):
    assert Parantheses().is_valid_parenthese(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(4000, 'MMMM')])
def test_eval5(test_input, expected):
    assert Int_solution().int_to_Roman(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [([0,1],[[], [1], [0], [0, 1]])])
def test_eval6(test_input, expected):
    assert Subset().sub_sets(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [((5,7,6,8,2,1),10,(3,4))])
def test_eval7(test_input1, test_input2, expected):
    assert Sum().twoSum(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", 
[
    ([-25, -10, -7, -3, 2, 4, 8, 10],[[-10, 2, 8], [-7, -3, 10]])
])
def test_eval8(test_input, expected):
    assert SumEqualsZero().threeSum(test_input) == expected