from src.ejercicio3 import cuentaAtras
import pytest

def test_3():
    
    assert cuentaAtras(3) == [3, 2, 1, 0]
    
def test_3_except():
    with pytest.raises(ValueError):
            cuentaAtras(-1)