#Ejercicio 2.3.3¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta 
#atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto. 

def leeNumero(): 
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def cuentaAtras(numero):
    if numero < 0:
        raise ValueError
    numeros = []
    for x in range(numero, -1, -1):
        numeros.append(x)
    return numeros

def construyeMensaje(numeros: list):
    mensaje = ""
    
    for numero in numeros:
        if numero != 0:
            mensaje += f"{numero}, "
        else:
            mensaje += f"{numero}"
    return mensaje
    
if __name__ == "__main__":
    try:
        numero = leeNumero()
        numeros_del_cero_al_numero = cuentaAtras(numero)
        print(construyeMensaje(numeros_del_cero_al_numero))
    except:
        print("ERROR. Numero negativo")
