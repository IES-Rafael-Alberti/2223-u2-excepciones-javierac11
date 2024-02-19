from src.ejercicio4 import leeNumero
import pytest

def test_4(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert leeNumero() == 5 

    
def test_4_except(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'ds')
    with pytest.raises(ValueError):
        leeNumero()