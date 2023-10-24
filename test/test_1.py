from src.ejercicio1 import leeEdad
import pytest


def test_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '25')
    assert leeEdad() == 25
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(ValueError):
        leeEdad()
