# construir una funcion que reciba una cadena digitada (como parametro) por el usuario y que lo muestre n veces en la pantalla. el valor de n tambien es digitado por el usuario.
def repetir_cadena(cadena, n):
    for _ in range(n):
        print(cadena)

texto = input("Ingrese una cadena de texto: ")
veces = int(input("Ingrese el número de veces que desea repetirla: "))


repetir_cadena(texto, veces)