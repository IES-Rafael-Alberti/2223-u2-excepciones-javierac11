#Ejercicio 2.3.2¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los 
#números impares desde 1 hasta ese número separados por comas.

def pedir_numero():
    try:
        numero = int(input("Introduce un numero: "))
        if numero <= 0:
            raise ValueError("Numero invalido")
        return numero
    except ValueError:
        raise ValueError("No es un numero")
    
def numerosImpares(numero: int) -> list:
    impares = []
    for numero in range(1, numero+1):
        if numero % 2 != 0:
            impares.append(numero)
    return impares

if __name__ == "__main__":
    
    
    numero = pedir_numero()
    impares = numerosImpares(numero)
    for numero in impares:
        if impares.index(numero) == len(impares)-1:
            print(numero)
        else:
            print(numero, end=", ")