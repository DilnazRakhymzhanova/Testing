import pytest

@pytest.mark.slow
def test_my_fast():
    sdu = "Aruzhan"
    assert "Aru" in sdu

@pytest.mark.slow
def test_my():
    number = 1100
    assert 1000+99+1 == number

