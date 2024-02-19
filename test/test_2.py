from src.ejercicio2 import pedir_numero
import pytest

def test_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '-3')
    with pytest.raises(ValueError):
        pedir_numero()
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(ValueError):
        pedir_numero()
    
