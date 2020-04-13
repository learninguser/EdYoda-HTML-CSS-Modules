from ipynb.fs.full.assignment import *
import pytest

@pytest.mark.parametrize("test_input, expected", [([('English', 95), ('Science', 95), ('Maths', 90), ('Social sciences', 88)],[('Social sciences', 88), ('Maths', 90), ('English', 95), ('Science', 95)])])
def test_eval1(test_input, expected):
    assert question_first_solution(test_input)== expected

@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],'Even Numbers: [2, 4, 6, 8, 10], Odd Numbers: [1, 3, 5, 7, 9]')])
def test_eval2(test_input, expected):
    assert question_second_solution(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9],[1, 2, 8, 9])])
def test_eval3(test_input1, test_input2, expected):
    assert question_third_solution(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [([1, 2, 3, 5, 7, 8, 9, 10],(5,3))])
def test_eval4(test_input, expected):
    assert question_fourth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],['Monday', 'Friday', 'Sunday'])])
def test_eval5(test_input, expected):
    assert question_fifth_solution(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [([1,2,3],[2,3,4],[3,5,7])])
def test_eval6(test_input1, test_input2, expected):
    assert question_sixth_solution(test_input1, test_input2,) == expected

@pytest.mark.parametrize("test_input, expected", [([('Harry', 8.0),('Garry',8.0),('Steve',9.5),('Daniel', 7.0)],'Garry, Harry')])
def test_eval7(test_input, expected):
    assert question_seventh_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(["php", "w3r", "Python", "abcd", "Java", "aaa"],['php', 'aaa'])])
def test_eval8(test_input, expected):
    assert question_eighth_solution(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [(["bcda", "abce", "cbda", "cbea", "adcb"],'abcd',['bcda', 'cbda', 'adcb'])])
def test_eval9(test_input1, test_input2, expected):
    assert question_ninth_solution(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],[19, 65, 57, 39, 152, 190])])
def test_eval10(test_input, expected):
    assert question_tenth_solution(test_input) == expected