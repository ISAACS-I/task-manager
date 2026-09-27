"""Lab 3 - Dynamic analysis tests for calculate_discount()."""

import pytest
from app.tasks import calculate_discount


class TestValidPartitions:
   
    def test_premium_valid_positive_price(self):
        assert calculate_discount(100, True) == 80.0

    def test_non_premium_valid_positive_price(self):
        assert calculate_discount(100, False) == 100

    def test_premium_zero_price(self):
        assert calculate_discount(0, True) == 0

    def test_non_premium_zero_price(self):
        assert calculate_discount(0, False) == 0


class TestBoundaryValues:

    def test_premium_tiny_positive(self):
        assert calculate_discount(0.01, True) == pytest.approx(0.008)

    def test_non_premium_tiny_positive(self):
        assert calculate_discount(0.01, False) == 0.01

    def test_premium_boundary(self):
        assert calculate_discount(0.00, True) == 0.00

    def test_non_premium_boundary(self):
        assert calculate_discount(0.00, False) == 0.00


class TestInvalidInputs:

    def test_negative_price_premium(self):
        with pytest.raises(ValueError):
            calculate_discount(-0.01, True)

    def test_negative_price_non_premium(self):
        with pytest.raises(ValueError):
            calculate_discount(-0.01, False)

    def test_is_premium_as_int_one(self):
        # None represents a missing/null premium status.
        with pytest.raises(TypeError):
            calculate_discount(100, 1)

    def test_is_premium_as_none(self):
        # None represents a missing/null premium status.
        with pytest.raises(TypeError):
            calculate_discount(0, None)