# Listas de paquetes turísticos con nombre, descripción y precio
nombres_paquetes = [
    "Magia del Amazonas",
    "Rutas del Café en el Eje Cafetero",
    "Misterios de Ciudad Perdida",
    "Aventura en el Desierto de la Tatacoa",
    "Paraíso Submarino en San Andrés y Providencia"
]

descripciones_paquetes = [
    "Explora el ecosistema amazónico, navega por el río, conoce comunidades indígenas y admira fauna exótica como delfines rosados y aves multicolores.",
    "Vive la experiencia cafetera desde la cosecha hasta la taza. Recorre pintorescos pueblos y disfruta de las mejores variedades de café.",
    "Realiza un trekking por la Sierra Nevada hacia este antiguo asentamiento indígena, cruzando ríos y selvas mientras descubres la historia de los Tayrona.",
    "Disfruta de caminatas por paisajes áridos, relájate en piscinas naturales y contempla un cielo estrellado incomparable.",
    "Practica buceo o snorkel en uno de los mayores arrecifes de coral y sumérgete en la cultura isleña, su gastronomía y ambiente relajado."
]

precios_paquetes = [
    800000,  # Precio de Magia del Amazonas
    750000,  # Precio de Rutas del Café
    900000,  # Precio de Misterios de Ciudad Perdida
    350000,  # Precio de Aventura en el Desierto de la Tatacoa
    700000   # Precio de Paraíso Submarino
]

vuelos_disponibles = [
    {"nombre": "Vuelo A", "origen": "Bogotá", "destino": "Leticia", "precio": 300000},  # Magia del Amazonas
    {"nombre": "Vuelo B", "origen": "Medellín", "destino": "Manizales", "precio": 450000},  # Rutas del Café en el Eje Cafetero
    {"nombre": "Vuelo C", "origen": "Cali", "destino": "Santa Marta", "precio": 250000},  # Misterios de Ciudad Perdida
    {"nombre": "Vuelo D", "origen": "Bucaramanga", "destino": "Neiva", "precio": 400000},  # Aventura en el Desierto de la Tatacoa
    {"nombre": "Vuelo E", "origen": "Cartagena", "destino": "San Andrés", "precio": 350000}  # Paraíso Submarino
]

# Diccionario para guardar las reservas de paquetes de cada cliente 
reservas = {} 
# Diccionario para clientes en el sistema
clientes = {}
idRes = 1

# Agregar clientes
def agregar_clientes():
    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese su teléfono: ")
    direccion = input("Ingrese su dirección: ")
    identificacion = input("Ingrese su documento de identidad: ")
    clientes[identificacion] = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion
    }

# Mostrar opciones de paquetes
def mostrar_paquetes():
    global idRes
    print("\nPaquetes Turísticos Disponibles:\n")
    for i in range(len(nombres_paquetes)):
        print(f"{i + 1}. {nombres_paquetes[i]}")
        print(f"   Descripción: {descripciones_paquetes[i]}")
        print(f"   Precio: ${precios_paquetes[i]}\n")

    while True:
        seleccion = int(input("Seleccione el número del paquete que desea (1-5), o 0 para salir: "))
        user = input("Ingrese su identificación para elegir el paquete: ")
    
        if not clientes:
            print("No hay clientes registrados en el sistema")
            return
        else:
            if user not in clientes.keys():
                print(f"Usuario con identificación {user} no está registrado...")
                return
            else:
                if seleccion == 0:
                    print("Gracias por usar nuestros servicios. ¡Hasta pronto!")
                    return
                elif 1 <= seleccion <= len(nombres_paquetes):
                    print(f'El cliente con identificación {user} y de nombre {clientes[user]["nombre"]} ha seleccionado el paquete: {nombres_paquetes[seleccion - 1]}')
                    print(f"Descripción: {descripciones_paquetes[seleccion - 1]}")
                    print(f"Precio: ${precios_paquetes[seleccion - 1]}")
                    reservas.update({
                        "reserva " + str(idRes): {
                            "Usuario": user, 
                            "Nombre": clientes[user]["nombre"], 
                            "paquete": nombres_paquetes[seleccion - 1], 
                            "precio del paquete": precios_paquetes[seleccion - 1]
                        }
                    })
                    idRes += 1
                    print(reservas)
                    print("\nSu paquete ha sido seleccionado exitosamente.\n")
                    return
                else:
                    print("Selección no válida, por favor intenta de nuevo.")

def reservaHoteles():
    global idRes
    import time
    import random
    from datetime import datetime, timedelta

    # Lista de hoteles con sus calificaciones en estrellas
    hoteles = [
        {"nombre": "Hotel Plaza", "calificacion": 5, "precio por reserva": 500000},
        {"nombre": "Grand Palace Hotel", "calificacion": 4, "precio por reserva": 400000},
        {"nombre": "Ocean View Resort", "calificacion": 5, "precio por reserva": 600000},
        {"nombre": "City Center Inn", "calificacion": 3, "precio por reserva": 350000},
        {"nombre": "Mountain Retreat", "calificacion": 4, "precio por reserva": 430000},
        {"nombre": "Budget Stay Hotel", "calificacion": 2, "precio por reserva": 200000},
        {"nombre": "Lakeside Cabins", "calificacion": 4, "precio por reserva": 425000},
        {"nombre": "Luxury Suites", "calificacion": 5, "precio por reserva": 650000},
        {"nombre": "Cozy Cottage Inn", "calificacion": 2, "precio por reserva": 240000},
        {"nombre": "Urban Hotel", "calificacion": 3, "precio por reserva": 320000},
    ]

    # Tipos de habitaciones
    habitaciones = [
        {"numero": "Suite Junior", "incremento": 0},
        {"numero": "Suite Ejecutiva", "incremento": 80000},
        {"numero": "Suite Presidencial", "incremento": 120000},
    ]

    # Función para mostrar los hoteles disponibles y permitir elegir uno
    def mostrar_y_elegir_hotel():
        global reservas
        print("\n-- Hoteles disponibles --")
        print(f"id Reserva: {idRes}" )
        for indice, hotel in enumerate(hoteles, 1):
            print(f"{indice}. {hotel['nombre']} - {hotel['calificacion']} estrellas")
        
        while True:
            documento = input("Ingrese su número de documento para realizar la reserva del hotel: ")
            if not clientes:
                print("No hay clientes registrados en el sistema")
                return
            else:
                if documento not in clientes.keys():
                    print(f"Usuario con identificación {documento} no está registrado...")
                    return
                else:
                    try:
                        seleccion = int(input("\n > Ingrese el número del hotel en el cual desea hospedarse: "))
                        if 1 <= seleccion <= len(hoteles):
                            hotel_seleccionado = hoteles[seleccion - 1]
                            print(f"\n > Ha seleccionado el hotel: {hotel_seleccionado['nombre']} ({hotel_seleccionado['calificacion']} estrellas)\n")

                            # Actualizar la reserva donde el usuario coincide
                            for reserva in reservas.values():
                                if reserva["Usuario"] == documento:
                                    reserva.update({
                                        "hotel": hotel_seleccionado['nombre'],
                                        "precio del hotel": hotel_seleccionado['precio por reserva']
                                    })
                                    print(f"Reserva actualizada para el usuario con documento #: {documento}")
                                    break  # Salir del bucle si se encontró y actualizó la reserva
                            else:
                                print(f"No se encontró la reserva para el usuario con documento #: {documento}")
                            return
                        else:
                            print("Opción inválida. Por favor, elija un número válido.")
                    except ValueError:
                        print("Error. Por favor ingrese un número válido.")

    # Función para mostrar los tipos de habitaciones disponibles
    def mostrar_habitaciones():
        print("\n-- Tipos de habitaciones disponibles --")
        for indice, habitacion in enumerate(habitaciones, 1):
            print(f"> {indice}. {habitacion['numero']}")

        while True:
            documento = input("Ingrese su número de documento para realizar la reserva del hotel: ")
            if not clientes:
                print("No hay clientes registrados en el sistema")
                return
            else:
                if documento not in clientes.keys():
                    print(f"Usuario con identificación {documento} no está registrado...")
                    return
                else:
                    try:
                        seleccion = int(input("\n > Ingrese el número de habitación en la cual desea quedarse: "))
                        numHab = habitaciones[seleccion - 1]['numero']
                        incremento = habitaciones[seleccion - 1]['incremento']
                        costo_total_habitacion = hoteles[0]['precio por reserva'] + incremento  # Suponiendo que el primer hotel es el elegido
                        print(f"\n > Ha seleccionado la habitación: {numHab} con un costo adicional de ${incremento}.")
                        
                        # Actualizar la reserva donde el usuario coincide
                        for reserva in reservas.values():
                            if reserva["Usuario"] == documento:
                                reserva.update({
                                    "habitacion": numHab,
                                    "precio de habitaciones": costo_total_habitacion
                                })
                                print(f"Reserva de habitación actualizada para el usuario: {documento}")
                                return
                        else:
                            print(f"No se encontró la reserva para el usuario: {documento}")
                        return
                    except (ValueError, IndexError):
                        print("Error. Por favor ingrese un número válido.")

    mostrar_y_elegir_hotel()
    mostrar_habitaciones()

def seleccionar_origen():
    # Lista de opciones de lugar de origen
    origenes = [
        "Bogotá", 
        "Medellín", 
        "Cali"
    ]
    while True:
        print("Lugares de origen:")
        for i in range(len(origenes)):
            print(f"{i + 1}. {origenes[i]}")
        seleccion_origen = int(input("Seleccione el número de su lugar de origen o 0 para salir: ")) - 1
        
        if seleccion_origen == -1:
            print("Gracias por usar nuestros servicios. ¡Hasta pronto!")
            return None
        elif 0 <= seleccion_origen < len(origenes):
            return origenes[seleccion_origen]
        else:
            print("Selección no válida, por favor intenta de nuevo.")

# Lista de destinos
destinos = [
    "Leticia, Amazonas", 
    "Armenia, Rutas del Café", 
    "Santa Marta, Ciudad Perdida", 
    "Neiva, Desierto de la Tatacoa", 
    "San Andrés y Providencia, Paraíso Submarino"
]

# Lista de precios de los vuelos
precios_vuelos = {
    "Bogotá-Leticia, Amazonas": 1200,
    "Bogotá-Armenia, Rutas del Café": 800,
    "Bogotá-Santa Marta, Ciudad Perdida": 600,
    "Bogotá-Neiva, Desierto de la Tatacoa": 700,
    "Bogotá-San Andrés y Providencia": 500,
    "Medellín-Leticia, Amazonas": 1150,
    "Medellín-Armenia, Rutas del Café": 850,
    "Medellín-Santa Marta, Ciudad Perdida": 650,
    "Medellín-Neiva, Desierto de la Tatacoa": 750,
    "Medellín-San Andrés y Providencia": 1150,
    "Cali-Leticia, Amazonas": 1290,
    "Cali-Armenia, Rutas del Café": 900,
    "Cali-Santa Marta, Ciudad Perdida": 700,
    "Cali-Neiva, Desierto de la Tatacoa": 800,
    "Cali-San Andrés y Providencia": 1200
}

def seleccionar_destino(lugar_origen):
    while True:
        print("\nDestinos y sus costos desde tu ciudad de origen seleccionada:")
        for i in range(len(destinos)):
            destino = destinos[i]
            precio = precios_vuelos.get(f"{lugar_origen}-{destino}")
            print(f"{i + 1}. {destino} - Precio: ${precio}")
        
        seleccion_destino = int(input("Seleccione el número de su destino o 0 para salir: ")) - 1
        
        if seleccion_destino == -1:
            print("Gracias por usar nuestros servicios. ¡Hasta pronto!")
            return None
        elif 0 <= seleccion_destino < len(destinos):
            return destinos[seleccion_destino]
        else:
            print("Selección no válida, por favor intenta de nuevo.")

def reservaVuelos():
    global idRes
    lugar_origen = seleccionar_origen()
    if lugar_origen is None:
        return

    destino_seleccionado = seleccionar_destino(lugar_origen)
    if destino_seleccionado is None:
        return

    cantidad_personas = int(input("Cantidad de personas que viajan: "))
    
    # Calcular el costo total del vuelo
    ruta = f"{lugar_origen}-{destino_seleccionado}"
    costo_vuelo_base = precios_vuelos.get(ruta, 0)  # Precio base si no está en el diccionario
    costo_total_vuelo = costo_vuelo_base * cantidad_personas

    # Obtener documento del cliente
    documento = input("Ingrese su número de documento para realizar la reserva del vuelo: ")
    if documento not in clientes.keys():
        print("Usuario con identificación no está registrado.")
        return

    # Actualizar la reserva donde el usuario coincide
    for reserva in reservas.values():
        if reserva["Usuario"] == documento:
            reserva.update({
                "vuelo": destino_seleccionado,
                "precio del vuelo": costo_total_vuelo
            })
            print(f"Reserva actualizada para el usuario: {documento}")
            print(f"Total del vuelo: ${costo_total_vuelo}")
            return

    print(f"No se encontró la reserva para el usuario: {documento}")

def datosPago():
    global reservas
    print("\nDATOS DE PAGO DE LAS RESERVAS")
    doc = input("Ingrese su documento para consultar los valores de la reserva: ")
    if doc not in clientes.keys():
        print("El usuario no tiene reservas.")
    else:
        print(f"El usuario con identificación {doc} tiene las siguientes reservas:")
        suma = 0
        for val in reservas.values():
            if val['Usuario'] == doc:
                suma += val.get("precio del paquete", 0) + val.get("precio del hotel", 0) + val.get("precio de habitaciones", 0) + val.get("precio del vuelo", 0)
        
        print(f"Total a pagar por las reservas: ${suma}")

# Funcion de ejecucion principal de la aplicacion
def main():
    while True:
        print("\n--------- BIENVENIDO A TRAVEL 360 ---------")
        print("1. Agregar cliente")
        print("2. Reservar paquetes turísticos")
        print("3. Reservar hotel")
        print("4. Reservar vuelo")
        print("5. Consultar datos de pago")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_clientes()
        elif opcion == '2':
            mostrar_paquetes()
        elif opcion == '3':
            reservaHoteles()
        elif opcion == '4':
            reservaVuelos()
        elif opcion == '5':
            datosPago()
        elif opcion == '0':
            print("Gracias por usar nuestros servicios. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
