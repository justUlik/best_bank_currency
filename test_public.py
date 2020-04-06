import pytest

from exchange_rate import get_best_exchange_rate

def test_get_best_exchange_rate_indexes():
    with pytest.raises(IndexError) as excinfo:
        excinfo = get_best_exchange_rate("RUB", 1)

def test_get_best_exchange_rate_types():
    excinfo = get_best_exchange_rate("USD", 3)
    assert type(excinfo[0]) == tuple
    assert type(excinfo[0][0]) == str
    assert type(excinfo[0][1]) == str
    assert type(excinfo[0][2]) == float

def test_get_best_exchange_rate_len():
    num_branches = 3
    currency_code = "EUR"
    excinfo = get_best_exchange_rate(currency_code, num_branches)
    assert len(excinfo) == num_branches

def test_get_best_exchange_rate_sort():
    num_branches = 6
    currency_code = "EUR"
    excinfo = get_best_exchange_rate(currency_code, num_branches)
    sorted_excinfo = sorted(excinfo, key=lambda tup: tup[2])
    assert excinfo == sorted_excinfo
