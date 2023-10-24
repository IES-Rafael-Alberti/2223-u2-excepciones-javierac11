from src.ejercicio5 import leeContrasenia, compruebaContrasenia
import pytest

def test_5(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1234')
    assert leeContrasenia() == "1234" 

    
def test_5_except():
    with pytest.raises(NameError):
        compruebaContrasenia("1234", "12345")