from src.ejercicio1 import leeEdad
import pytest


def test_leeEdad_valida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '25')
    assert leeEdad() == 25

def test_leeEdad_invalida_texto(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'abc')
    with pytest.raises(ValueError):
        leeEdad()
