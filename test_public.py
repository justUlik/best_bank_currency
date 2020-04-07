import pytest
import random
from random import randint

from exchange_rate import get_best_exchange_rate

currencies = ["EUR", "USD"]
max_num_brunches = [13, 13]

sufficent_testdata = list(zip(currencies, max_num_brunches))

@pytest.mark.parametrize("currency, max_num_brunches", sufficent_testdata)
def test_size_of_ans(currency, max_num_brunches):
    num_brunches = randint(1, max_num_brunches)
    assert len(get_best_exchange_rate(currency, num_brunches)) == num_brunches

@pytest.mark.parametrize("currency, num_brunches", sufficent_testdata)
def test_size_of_ans_correct(currency, num_brunches):
    with pytest.raises(IndexError) as excinfo:
        excinfo = get_best_exchange_rate(currency, num_brunches + 10000)
    assert "Num of brunces is too big" == str(excinfo.value)

@pytest.mark.parametrize("currency, max_num_brunches", sufficent_testdata)
def test_sort_correct(currency, max_num_brunches):
    num_brunches = randint(1, max_num_brunches)
    excinfo = get_best_exchange_rate(currency, num_brunches)
    assert excinfo == sorted(excinfo, key=lambda tup: tup[2])


@pytest.mark.parametrize("currency, max_num_brunches", sufficent_testdata)
def test_type_excinfo(currency, max_num_brunches):
    num_brunches = randint(1, max_num_brunches)
    excinfo = get_best_exchange_rate(currency, num_brunches)
    assert type(excinfo[0]) == tuple
    assert type(excinfo[0][0]) == str
    assert type(excinfo[0][1]) == str
    assert type(excinfo[0][2]) == float

@pytest.mark.parametrize("currency", currencies)
def test_correct_num_brunches(currency):
    num_brunches = random.uniform(1.00, 13.00)
    with pytest.raises(ValueError) as excinfo:
        excinfo = get_best_exchange_rate(currency, num_brunches)
    assert "Num branches is not correct \nHINT: Num branches must be more then zero and type int" == str(excinfo.value)
