# ============================================
# SISTEMA DE TICKETS - SOPORTE TÉCNICO TI 
# 19/ 05/ 2026, Leonardo Luna

# Base de conocimientos offline

# Estas son algunas de las situaciones más comunes por las cuales el internet está lento, también incluí el hecho de que la computadora puede influir en la velocidad del internet
# Acá en los problemas de internet lento, puedo considerar el hecho de que existe más de una forma de conectarse a internet, en este caso
# estoy considerando solamente Wifi y un cable ethernet, y tomando eso en cuenta, separar las soluciones para conexión Wifi y conexión mediante clabe ethernet
# De momento voy a considerar todas las posibles soluciones para ambos casos de conexión.

# Documentación offline que el usuario puede revisar antes o después de generar un ticket
documentacion = {
    "internet": """
 SOLUCIÓN PARA PROBLEMAS DE INTERNET 
                                     
1. Reinicie el módem y el router.
2. Verifique si el cable de red ethernet esté bien conectado al módem y a la computadora.
3. Verifique si el cable de red ethernet no está dañado.
3. Compruebe si el WiFi está activado.
4. En una terminal del cmd de windows ejecute el comando:
   ipconfig /flushdns
   
5. Verificar controladores del períferico del cable ethernet. 
6. Reinicie la computadora.
""",

    "computadora_lenta": """
 SOLUIONES PARA PC LENTA 

1. Cierra programas innecesarios.
2. Elimina archivos temporales.
3. Revisa si hay virus.
4. Reinicia la computadora.
5. Libera espacio en disco.
"""

}

# Lista para guardar tickets, se muestra al usuario
tickets = []                # Esto guarda los tickets como un arreglo
print(" SISTEMA DE TICKETS DE SOPORTE TI")
# Uso del condifional " True "
while True:
    # Opciones para el usuario 
    print("\n1. Crear ticket")
    print("2. Ver tickets")
    print("3. Consultar documentación offline")
    print("4. Salir")
    opcion = input("\nSelecciona una opción: ")       # Primer input del usuario para seleccionar alguna opción 

    # CREAR TICKET
    if opcion == "1":
        nombre = input("Nombre del usuario: ")
        problema = input("Describe el problema: ")       # Innput sobre el tipo de problema que tiene el usuario, en este caso internet o compuradora lenta 

        ticket = {
            "usuario": nombre,
            "problema": problema
        }

        tickets.append(ticket)
        print("\n Ticket creado correctamente.")

    # VER TICKETS
    elif opcion == "2":

        if len(tickets) == 0:
            print("\nNo hay tickets registrados.")

        else:
            print("\n        LISTA DE TICKETS        ")

            for i, ticket in enumerate(tickets, start=1):
                print(f"\nTicket #{i}")
                print(f"Usuario : {ticket['usuario']}")
                print(f"Problema: {ticket['problema']}")

    # DOCUMENTACIÓN OFFLINE
    elif opcion == "3":
        print("\nCategorías disponibles:")
        print("- internet")
        print("- computadora_lenta")
        categoria = input("\nEscribe la categoría: ")

        if categoria in documentacion:
            print(documentacion[categoria])

        else:
            print("\n No existe documentación para esa categoría.")

    # SALIR
    elif opcion == "4":
        print("\nSaliendo del sistema...")
        break

    else:
        print("\n Opción inválida.")