from unittest.mock import Mock

import pytest

from price import final_price, get_rate


@pytest.mark.parametrize(
    ("price", "discount", "expected"),
    [(100, 0, 100), (100, 0.2, 80), (19.9, 0.5, 9.95)],
)
def test_final_price(price, discount, expected):
    assert final_price(price, discount) == expected


def test_negative_price_regression():
    with pytest.raises(ValueError, match="non-negative"):
        final_price(-1)


def test_get_rate_without_network():
    client = Mock()
    client.get.return_value = {"rate": 0.8}

    assert get_rate(client) == 0.8
    client.get.assert_called_once_with("/rate")


def test_invalid_discount():
    with pytest.raises(ValueError, match="between 0 and 1"):
        final_price(100, 1.5)