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
    "Realiza un trekking por la Sierra Nevada hacia este antiguo asentamiento indígena, cruzando ríos y selvas mientras descubres la historia de los Tayrona. ",
    "Disfruta de caminatas por paisajes áridos, relájate en piscinas naturales y contempla un cielo estrellado incomparable. ",
    " Practica buceo o snorkel en uno de los mayores arrecifes de coral y sumérgete en la cultura isleña, su gastronomía y ambiente relajado. "
]

precios_paquetes = [
    800,  # Precio de Magia del Amazonas
    450,  # Precio de Rutas del Café
    900,  # Precio de Misterios de Ciudad Perdida
    350,  # Precio de Aventura en el Desierto de la Tatacoa
    700   # Precio de Paraíso Submarino
]
#diccionario para guardar las reservas de paquetes de cada cliente 
reservas= {} 
#diccionario para clientes en el sistema
clientes = {}
idClient = 1
idRes = 1


#Agregar clientes
def agregar_clientes():

    #global identificacion
    nombre = input("ingrese su nombre: ")
    telefono = input("ingrese su telefeno: ")
    direccion = input("ingrese su direccion: ")
    identificacion = input("ingrese su documento de identidad: ")
    clientes[identificacion] = {}
    clientes[identificacion]["nombre"] = nombre
    clientes[identificacion]["telefono"] = telefono
    clientes[identificacion]["direccion"] = direccion
    
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
        user = input("ingrese su identificacion para elegir el paquete: ")
    
        if not clientes:
            print("No hay clientes registrados en el sistema")
            return
        else:
                if user not in clientes.keys():
                    print(f"usuario con identifiacion {user} no esta registrado...")
                    return
                else:
                    if seleccion == 0:
                        print("Gracias por usar nuestros servicios. ¡Hasta pronto!")
                        return
                    elif 1 <= seleccion <= len(nombres_paquetes):
                        print(f'el cliente con identificacion {user}  y de nombre {clientes[user]["nombre"]} Ha seleccionado el paquete: {nombres_paquetes[seleccion - 1]}')
                        print(f"Descripción: {descripciones_paquetes[seleccion - 1]}")
                        print(f"Precio: ${precios_paquetes[seleccion - 1]}")
                        reservas.update({
                            "reserva " + str(idRes): {
                                "Usuario": user, 
                                "Nombre": clientes[user]["nombre"], 
                                "paquete": nombres_paquetes[seleccion - 1], 
                                "precio del paquete": precios_paquetes[seleccion - 1]}
                        })
                        idRes += 1
                        print(reservas)
                        print("\nSu paquete ha sido seleccionado exitosamente.\n")

                        return
                    else:
                        print("Selección no válida, por favor intenta de nuevo.")
                        break

def reservaHoteles():
    #global reservas
    global idRes
    import time #genera retrazos en la ejecucion del codigo
    import random # genera numeros aleatorios
    from datetime import datetime, timedelta # Obtiene la fecha y hora actuales

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
        {"numero": "Suite Presidencial", "inremento": 120000},
    ]

    # Función para generar una lista de fechas aleatorias
    def fechas_disponibles(cantidad=5):
        fechas = []
        fecha_inicio = datetime.now()
        for _ in range(cantidad):
            dias_a_sumar = random.randint(1, 30)  # Generar un número aleatorio de días entre 1 y 30
            nueva_fecha = fecha_inicio + timedelta(days=dias_a_sumar)
            fechas.append(nueva_fecha.strftime("%d-%m-%Y"))  # Formato de fecha DD-MM-YYYY
        return fechas

    # Función para mostrar los hoteles disponibles y permitir elegir uno
    def mostrar_y_elegir_hotel():
        global reservas
        print("\n-- Hoteles disponibles --")
        print(f"id Reserva: {idRes}" )
        for indice, hotel in enumerate(hoteles, 1):
            print(f"{indice}. {hotel['nombre']} - {hotel['calificacion']} estrellas")
        
        # Ahora se pregunta directamente al cliente en qué hotel desea hospedarse
        while True:
            documento = input("ingrese su numero de documento para realizar la reserva del hotel...")
            if not clientes:
                print("No hay clientes registrados en el sistema")
                return
            else:
                if documento not in clientes.keys():
                    print(f"usuario con identificacion {documento} no esta registrado...")
                    return
                else:
                    try:
                        seleccion = int(input("\n > Ingrese el número del hotel en el cual desea hospedarse: "))
                        if 1 <= seleccion <= len(hoteles):
                            hotel_seleccionado = hoteles[seleccion - 1]
                            print(f"\n > Ha seleccionado el hotel: {hotel_seleccionado['nombre']} ({hotel_seleccionado['calificacion']} estrellas)\n")

                            # Actualizar la reserva donde el usuario coincide
                            reserva_key = "reserva" + str(idRes-1)
                            for reserva in reservas.values():
                                if reserva["Usuario"] == documento:
                                    reserva.update({
                                        "hotel": hotel_seleccionado['nombre'],
                                        "precio del hotel": hotel_seleccionado['precio por reserva']
                                    })
                                    print(f"Reserva actualizada para el usuario: {documento}")
                                
                                    break  # Salir del bucle si se encontró y actualizó la reserva
                            
                            else:
                                print(f"No se encontró la reserva para el usuario: {documento}")
                            return
                        else:
                            print("Opción inválida. Por favor, elija un número válido.")
                    except ValueError:
                        print("Error. Por favor ingrese un número válido.")

    #Función para mostrar los tipos de habitaciones disponibles
    def mostrar_habitaciones():
        print("\n-- Tipos de habitaciones disponibles --")
        for indice, habitacion in enumerate(habitaciones, 1):
            print(f"> {indice}. {habitacion['numero']}")

        # Se le pregunta al cliente en qué tipo de habitación desea quedarse
        while True:
            try:
                seleccion = int(input("\n > Ingrese el número de habitación en la cual desea quedarse: "))
                if 1 <= seleccion <= len(habitaciones):
                    habitacion_seleccionada = habitaciones[seleccion - 1]
                    print(f"\n > Ha seleccionado la habitacion: {habitacion_seleccionada['numero']}\n")
                    break
                else:
                    print("Opción inválida. Por favor, elija un número válido.")
            except ValueError:
                print("Error. Por favor ingrese un número válido.")

    # Función para mostrar las fechas disponibles para cada hotel
    def mostrar_fechas():
        print("\n-- Fechas disponibles --")
        for hotel in hoteles:
            print(f"{hotel['nombre']} ({hotel['calificacion']} estrellas):")
            fechas = fechas_disponibles()
            for fecha in fechas:
                print(f"  - {fecha}")
            print()  # Espacio entre hoteles
            

    # Menú principal fuera del bucle
    def mostrar_menu():
        print("\n-------------- RESERVA DE HOTELES ---------------\n")
        print("1. Mostrar y elegir un hotel.")
        print("2. Mostrar tipos de habitaciones.")
        print("3. Mostrar fechas disponibles.")
        print("4. Salir.")
        print("-------------------------------------------")


    # Menú de reserva
    def menu_reserva():
        mostrar_menu()
        while True:
            opcion = input("> Ingrese el número de la opción con la cual desea continuar: ")
            if opcion == "1":
                print("\n Redirigiendo...")
                time.sleep(1)
                mostrar_y_elegir_hotel()  # Llama directamente a la función que muestra y pregunta
                break
            elif opcion == "2":
                print("\n Redirigiendo...")
                time.sleep(1)
                #mostrar_habitaciones()
                #mostrar_menu()  # Vuelve a mostrar el menú después de ver habitaciones
                break
            elif opcion == "3":
                print("\n Redirigiendo...")
                time.sleep(1)
                mostrar_fechas()
                #mostrar_menu()  # Vuelve a mostrar el menú después de ver fechas
                break
            elif opcion == "4":
                print("Gracias por utilizar nuestros servicios. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")

    # Llamada al menú principal
    menu_reserva()





#datos del total a pagar por las reservas
def datosPago():
    global reservas
    print("\nDATOS DE PAGO DE LAS RESERVAS")
    doc = input("ingrese su documento para consultar los valores de la reserva: ")
    if doc not in clientes.keys():
        print("el usuario no tiene reservas")
    else:
        print(f"el usuario con identificacion {doc} tiene las siguientes reservas")
        #print(f"el valor total de la reserva es: ${sum(reservas.values())}")
        print(reservas)
        suma = 0
        for val in reservas.values():
            if val['Usuario'] == doc:
                suma += val["precio del paquete"] + val["precio del hotel"]
        print(f"el valor total de la reserva es: ${suma}")
       
    

#-------------------------------------------------------- MENU PRINCIPAL DE LA APLICACION --------------------------------------------------- 
while True:

    print("------------- BIENVENIDO A TRAVEL 360 -------------")
    print("1. Agregar cliente")
    print("2. Elegir Paquete")
    print("3. Realizar Reserva de hotel")
    print("4. Realizar Reserva de vuelo")
    print("5. Consultar precio a pagar por las reservas")


    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        continue

    if opcion == 1:
        agregar_clientes()
    
    elif opcion == 2:
        mostrar_paquetes()

    elif opcion == 3: 
        reservaHoteles()

    elif opcion == 4: 
        pass #implementar reserva de vuelo
    
    elif opcion == 5:
        datosPago()