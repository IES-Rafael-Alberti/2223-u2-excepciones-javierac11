#Ejercicio 2.3.1¶
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha 
#cumplido (desde 1 hasta su edad).

def leeEdad():
    edad = input("Introduce tu edad: ")
    try:
        edad = int(edad)    
        return edad
    except ValueError:
        print("Error al introducir la edad")
        raise
        
def aniosCumplidos(edad: int) -> list:
    anios = []
    for x in range(1, edad+1):
        anios.append(x)
    return anios
        
if __name__ == "__main__":
    edad = leeEdad()
    print(aniosCumplidos(edad))