import pytest

from seasons import get_birth, Seasons 

def test_date():
    assert get_birth('1990-01-01') == "1990-01-01"
    assert get_birth('1990-01-02') == "1990-01-01"
    
def test_class():
    assert Seasons.nbresjour(12) == "twelve minutes"