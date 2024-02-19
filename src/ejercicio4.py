#Ejercicio 2.3.4¶
#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta,
#mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def leeNumero(): 
    numero = input("Introduce un numero: ")
    if not numero.isnumeric():
        raise ValueError
        #numero = input("ERROR.Introduce un numero: ")
    return int(numero)

if __name__ == "__main__":
    try:
        leeNumero()
    except ValueError:
        print("La entrada no es correcta")
        