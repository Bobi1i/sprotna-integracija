import pytest
from main import deli
 
 
def test_deli_pozitivni():
    assert deli(10, 2) == 5.0
 
def test_deli_negativni():
    assert deli(-9, 3) == -3.0
 
def test_deli_decimalni_rezultat():
    assert deli(1, 3) == pytest.approx(0.333, rel=1e-2)
 
def test_deli_z_niclo_vrze_napako():
    with pytest.raises(ValueError, match="Deljenje z nič ni dovoljeno!"):
        deli(5, 0)