from a01 import *
import pytest

@pytest.mark.parametrize("test_input, expected", [('aabdffdcsgba','abdfcsg')])
def test_eval1(test_input, expected):
    assert question_first_solution(test_input)== expected


@pytest.mark.parametrize("test_input, expected", [('restart', 'resta@t')])
def test_eval2(test_input, expected):
    assert question_second_solution(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [("abc","xyz", 'xyc abz')])
def test_eval3(test_input1, test_input2, expected):
    assert question_third_solution(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [('abcdefghij', 'aAcAeAgAiA')])
def test_eval4(test_input, expected):
    assert question_fourth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [('abcd', 'cdcdcdcd')])
def test_eval5(test_input, expected):
    assert question_fifth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [('abcd', 'dcba')])
def test_eval6(test_input, expected):
    assert question_sixth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [("bfsaxc",'abcfsx')])
def test_eval7(test_input, expected):
    assert question_seventh_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [("davfaba", 'daba')])
def test_eval8(test_input, expected):
    assert question_eighth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [('abcdAnVBC1', 'ABCDaNvbc1')])
def test_eval9(test_input, expected):
    assert question_ninth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [('edyoda.com', '{e: 1,d: 2,y: 1,o: 2,a: 1,.: 1,c: 1,m: 1,}')])
def test_eval10(test_input, expected):
    assert question_tenth_solution(test_input) == expected