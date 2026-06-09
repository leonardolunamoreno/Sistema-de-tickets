# Calculadora en Python
# Versión 1.0 
# Leonardo Luna 
# 05 / 06 / 2026 

# Requisitos para el funcionamiento: 

# Objetivo: 
# Programa diseñado para resolver operaciones aritméticas básicas

# Descripción general:
# El praograma muestra un menú con 4 opciones de operación. El usuario puede elegir cualquiera de esas opciones, ingresa un par de números 
# desde el teclado y el resultado se muestra en la terminal.

# Instrucciones de uso: 
# 1.- Ejecutar el archivo calculadora.py 
# 2.- Seleccionar una opció del menú (1-4)
# 3.- Ingresar el primer número 
# 4.- Ingresar el segundo número 
# 5.- Ver el resultado en pantalla
# 6.- Repetir o cerrar el programa 



print("========= CALCULADORA EN PYTHON =========")     # Título de la aplicación, mostrado en la cosola 
                                    
print("Seleccione una operación:")                     # Menú de opciones
print("1. Suma") 
print("2. Resta") 
print("3. Multiplicación") 
print("4. División")

while True:                                                        # Ingreso de datos por el parte del usuario
    opcion = input("Ingresa opción (1-4) : ")                      # Ingreso del número de operación elegida por el usuario.
    num1 = float(input("Ingresa el primer número: "))              # Ingreso del primer número. 
    num2 = float(input("Ingresa el segundo número: "))             # Ingreso del segundo número.


    # Definición de la operación suma
    if opcion == '1': 
        resultado = num1 + num2
        operacion = "Suma"
    
    # Definición de la operación resta
    elif opcion == '2':
        resultado = num1 - num2 
        operacion = "Resta"
    
    # Definición de la operación multiplicación
    elif opcion == '3':
        resultado = num1 * num2 
        operacion = "Multiplicación"
    
    # Definición de la operación División 
    elif opcion == '4':
        if num2 != 0:
            restultado = num1 / num2
            operacion = "División"
        else:
            print("Error: No se puede dividir entre 0.")
            exit()

    else: 
        print("Opción no válida.")
        exit()
        break
    
    # Impresión del resultado
    print(f"n\{operacion}: {num1} y {num2} = {resultado}")          #  Acá había otro error. 


# Incluir un bucle para que el programa se repita hasta que el usuario decida salir 
# Agregar más operaciones como potencias, raices, modulo 
# Crear una interfaz gráfica usando Tkinter, para que tenga botones 