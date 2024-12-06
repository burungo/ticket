import random
import pickle
import os


archivo_tickets = "tickets.dat"


if os.path.exists(archivo_tickets):
    with open(archivo_tickets, "rb") as archivo:
        tickets = pickle.load(archivo)
else:
    tickets = {}

def alta_ticket():
    print("Alta de ticket")
    nombre = input("Ingrese su nombre: ")
    asunto = input("Ingrese el asunto del ticket: ")
    sector = input("Ingrese el sector al que pertenece: ")
    problema = input("Ingrese el problema que está experimentando: ")

    # Generar número de ticket aleatorio
    numero_ticket = random.randint(1000, 9999)

    # Crear ticket
    ticket = {
        "nombre": nombre,
        "asunto": asunto,
        "sector": sector,
        "problema": problema
    }

    # Almacenar ticket en la base de datos
    tickets[numero_ticket] = ticket

    # Guardar tickets en archivo
    with open(archivo_tickets, "wb") as archivo:
        pickle.dump(tickets, archivo)

    # Mostrar ticket en pantalla
    print(f"Ticket {numero_ticket}:")
    print(f"Nombre: {nombre}")
    print(f"Asunto: {asunto}")
    print(f"Sector: {sector}")
    print(f"Problema: {problema}")
    print("Recuerde anotar el número de ticket para futuras consultas.")

    # Preguntar si se desea crear otro ticket
    respuesta = input("¿Desea crear otro ticket? (s/n): ")
    if respuesta.lower() == "s":
        alta_ticket()
    else:
        menu_principal()

def leer_ticket():
    print("Leer ticket")
    numero_ticket = int(input("Ingrese el número de ticket: "))

    # Verificar si el ticket existe
    if numero_ticket in tickets:
        ticket = tickets[numero_ticket]
        print(f"Ticket {numero_ticket}:")
        print(f"Nombre: {ticket['nombre']}")
        print(f"Asunto: {ticket['asunto']}")
        print(f"Sector: {ticket['sector']}")
        print(f"Problema: {ticket['problema']}")
    else:
        print("El ticket no existe.")

    # Preguntar si se desea leer otro ticket
    respuesta = input("¿Desea leer otro ticket? (s/n): ")
    if respuesta.lower() == "s":
        leer_ticket()
    else:
        menu_principal()

def salir():
    print("¿Está seguro de que desea salir? (s/n): ")
    respuesta = input()
    if respuesta.lower() == "s":
        print("Hasta luego.")
        exit()
    else:
        menu_principal()

def menu_principal():
    print("Menú principal")
    print("1. Alta de ticket")
    print("2. Leer ticket")
    print("3. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        alta_ticket()
    elif opcion == "2":
        leer_ticket()
    elif opcion == "3":
        salir()
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        menu_principal()

menu_principal()
