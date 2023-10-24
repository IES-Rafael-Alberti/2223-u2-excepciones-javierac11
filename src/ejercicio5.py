#Ejercicio 2.3.5¶
#Escribir que solicite una contraseña, y si no coincide con la que se tiene, 
#lance la excepción NameError con el mensaje, "Incorrect Password!!

def leeContrasenia() -> str:
    contrasenia = input("Introduce la contraseña: ")
    return contrasenia
    
def compruebaContrasenia(contrasenia, contrasenia_input) -> bool:
    if contrasenia == contrasenia_input:
        return True
    else:
        raise NameError("Incorrect Password!!")

if __name__ == "__main__":
    try:
        contrasenia = leeContrasenia()
        if compruebaContrasenia("12345", contrasenia):
            print("Correcta")
    except:
        print("Incorrect Password!!")