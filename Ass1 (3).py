import pytest

@pytest.mark.slow
def test_my_fast():
    sdu = "canteen"
    assert "cant" in sdu

@pytest.mark.slow
def test_my():
    number = 1100
    assert 1000+99+1 == number

