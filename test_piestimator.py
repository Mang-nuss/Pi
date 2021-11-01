#author: MJ
#2021-10-30

import pytest
from pi_estimator import Estimator

@pytest.fixture() #Instantiaton
def pe():
    pe = Estimator()
    return pe

#----TESTS---#

def test_correct_value(pe):

    "inside check returns correct value"
    value = pe.insideCheck(1,0)
    assert value == True
    value = pe.insideCheck(1.5,1.5)
    assert value == False

def test_pi_output(pe):

    "pi estimation is output"
    pe.insides = 1
    pe.totals = 2
    value = pe.estimate()
    assert value == 2.0

    pe.insides = 1
    pe.totals = 10
    value = pe.estimate()
    assert value == 0.40

    pe.insides = 10
    pe.totals = 10
    value = pe.estimate()
    assert value == 4.0

def test_sum_is_increased(pe):

    "the nr of attempts is incremented"
    value = pe.insideCheck(1,0)
    assert pe.insides == 1
    assert pe.totals == 1

    "division succeeds"
    value = pe.insides/pe.totals
    assert value == 1
    assert pe.estimate() == 4.0
