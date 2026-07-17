# ==================================================
# ESCAPE LAB - VERSION 2.0
# Mismos fundamentos: variables, while, if/else, listas.
# Ahora con mas habitaciones, mas objetos y mas acertijos.
# ==================================================

# --------------------------
# ETAPA 1
# SALIDA POR CONSOLA
# --------------------------
print("=" * 55)
print("BIENVENIDOS A ESCAPE LAB 2.0")
print("=" * 55)

print()
print("Has despertado dentro de un laboratorio secreto, sin recordar cómo llegaste allí.")
print("Las luces parpadean y todas las puertas están bloqueadas.")
print("Tu objetivo es escapar recorriendo las instalaciones y resolviendo acertijos.")
print()

# -----------------
# ETAPA 2
# VARIABLES: RECORDAR INFORMACION
# -----------------

nombre = input("Antes de comenzar, ¿cómo te llamas? ")
print(f"¡Bienvenido, {nombre}! Prepárate para la aventura.")
print()

# -----------------
# ETAPA 3
# TIPO DE DATOS Y DIFICULTAD
# -----------------

print("Selecciona la dificultad del juego:")
print("1. Fácil    (5 intentos por acertijo y con pistas)")
print("2. Normal   (3 intentos por acertijo, sin pistas)")
print("3. Difícil  (1 intento por acertijo, sin pistas)")
dificultad = input("Ingresa el número correspondiente a la dificultad: ")
print()

# -----------------
# ETAPA 4
# TOMA DE DECISIONES: CONFIGURACION SEGUN LA RUTA
# -----------------

if dificultad == "1":
    print("Has elegido la dificultad Fácil. Tendrás más pistas y más intentos.")
    intentos_por_acertijo = 5
    hay_pistas = True

elif dificultad == "2":
    print("Has elegido la dificultad Normal. Los acertijos serán desafiantes pero manejables.")
    intentos_por_acertijo = 3
    hay_pistas = False

elif dificultad == "3":
    print("Has elegido la dificultad Difícil. Un solo intento por acertijo. Suerte.")
    intentos_por_acertijo = 1
    hay_pistas = False

else:
    print("Opción inválida. Se seleccionará la dificultad Normal por defecto.")
    intentos_por_acertijo = 3
    hay_pistas = False

print()

# -----------------
# ETAPA 5
# VARIABLES BOOLEANAS: ESTADO DEL JUEGO
# -----------------

juego_activo = True
escapaste = False

# Objetos que el jugador puede conseguir
linterna = False
destornillador = False
llave = False
tarjeta = False
codigo_descubierto = False

# Acertijos ya resueltos (para no repetirlos)
acertijo_quimica_resuelto = False
acertijo_servidores_resuelto = False
acertijo_oficina_resuelto = False

# El código secreto que abre la puerta final
codigo_secreto = "1974"

# Dónde está parado el jugador
ubicacion = "recepcion"

# -----------------
# ETAPA 6
# LISTAS: INVENTARIO
# -----------------

inventario = []
print("Tu inventario está vacío. A medida que explores, encontrarás objetos que te ayudarán a escapar.")
print()

# -----------------
# ETAPA 7
# CICLO PRINCIPAL DEL JUEGO
# -----------------

while juego_activo == True:

    # ==========================================
    # HABITACION: RECEPCION (el punto central)
    # ==========================================
    if ubicacion == "recepcion":
        print()
        print("=" * 55)
        print("LABORATORIO - RECEPCIÓN")
        print("=" * 55)
        print("Desde aquí puedes llegar a todas las demás áreas.")
        print()
        print("1. Ir al Laboratorio de Química")
        print("2. Ir a la Sala de Servidores")
        print("3. Ir al Almacén")
        print("4. Ir a la Oficina del Director")
        print("5. Ver tu inventario")
        print("6. Intentar abrir la puerta de salida")
        print("7. Salir del juego")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ubicacion = "quimica"

        elif opcion == "2":
            ubicacion = "servidores"

        elif opcion == "3":
            ubicacion = "almacen"

        elif opcion == "4":
            ubicacion = "oficina"

        elif opcion == "5":
            ubicacion = "inventario"

        elif opcion == "6":
            ubicacion = "salida"

        elif opcion == "7":
            print()
            print("Has decidido salir del juego. ¡Hasta la próxima!")
            juego_activo = False

        else:
            print()
            print("Opción inválida. Por favor, selecciona una opción válida.")

    # ==========================================
    # INVENTARIO
    # ==========================================
    elif ubicacion == "inventario":
        print()
        print("-" * 55)
        print("TU INVENTARIO")
        print("-" * 55)

        if len(inventario) == 0:
            print("Tu inventario está vacío. Explora para encontrar objetos.")
        else:
            for objeto in inventario:
                print(f"- {objeto}")

        print()
        print(f"Llevas {len(inventario)} objeto(s).")
        input("Presiona ENTER para volver a la recepción...")
        ubicacion = "recepcion"

    # ==========================================
    # HABITACION: LABORATORIO DE QUIMICA
    # ==========================================
    elif ubicacion == "quimica":
        print()
        print("=" * 55)
        print("LABORATORIO DE QUÍMICA")
        print("=" * 55)
        print("Frascos rotos por todas partes. Huele a algo que prefieres no saber qué es.")
        print("Sobre una mesa hay una caja fuerte pequeña con un teclado.")
        print()

        if acertijo_quimica_resuelto == True:
            print("La caja fuerte ya está abierta. Aquí no queda nada más.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        else:
            print("Una nota pegada a la caja dice:")
            print()
            print('   "Mientras más le quitas, más grande se vuelve.')
            print('    ¿Qué es?"')
            print()

            if hay_pistas == True:
                print("PISTA: Piensa en algo que se hace cavando en la tierra.")
                print()

            intentos = intentos_por_acertijo
            resuelto = False

            while intentos > 0 and resuelto == False:
                respuesta = input("Tu respuesta: ")
                respuesta = respuesta.lower().strip()

                if respuesta == "hoyo" or respuesta == "agujero" or respuesta == "un hoyo" or respuesta == "un agujero":
                    resuelto = True
                else:
                    intentos = intentos - 1
                    if intentos > 0:
                        print(f"Incorrecto. Te quedan {intentos} intento(s).")
                    else:
                        print("Incorrecto. Te quedaste sin intentos.")

            print()

            if resuelto == True:
                print("La caja fuerte se abre con un click.")
                print("Dentro encuentras una LLAVE oxidada.")
                acertijo_quimica_resuelto = True
                llave = True
                inventario.append("Llave")
            else:
                print("La caja fuerte sigue cerrada. Puedes volver a intentarlo más tarde.")

            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

    # ==========================================
    # HABITACION: SALA DE SERVIDORES
    # ==========================================
    elif ubicacion == "servidores":
        print()
        print("=" * 55)
        print("SALA DE SERVIDORES")
        print("=" * 55)
        print("El zumbido de las máquinas es ensordecedor. Hay un panel atornillado a la pared.")
        print()

        if acertijo_servidores_resuelto == True:
            print("El panel ya está abierto y la pantalla está apagada.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        elif destornillador == False:
            print("El panel está sujeto con tornillos. Necesitas un DESTORNILLADOR para abrirlo.")
            print("Quizás haya uno en el almacén.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        else:
            print("Usas el destornillador y abres el panel.")
            print("Detrás hay una pantalla parpadeando con una secuencia:")
            print()
            print("   2  -  4  -  8  -  16  -  ?")
            print()
            print("Debes escribir el número que sigue.")
            print()

            if hay_pistas == True:
                print("PISTA: Cada número es el doble del anterior.")
                print()

            intentos = intentos_por_acertijo
            resuelto = False

            while intentos > 0 and resuelto == False:
                respuesta = input("Tu respuesta: ")
                respuesta = respuesta.strip()

                if respuesta == "32":
                    resuelto = True
                else:
                    intentos = intentos - 1
                    if intentos > 0:
                        print(f"Incorrecto. Te quedan {intentos} intento(s).")
                    else:
                        print("Incorrecto. Te quedaste sin intentos.")

            print()

            if resuelto == True:
                print("La pantalla cambia y muestra un mensaje del sistema:")
                print()
                print(f"   CÓDIGO DE EMERGENCIA DE LA PUERTA: {codigo_secreto}")
                print()
                print("Memorizas el código y lo anotas.")
                acertijo_servidores_resuelto = True
                codigo_descubierto = True
                inventario.append("Código secreto")
            else:
                print("La pantalla se bloquea. Tendrás que volver a intentarlo.")

            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

    # ==========================================
    # HABITACION: ALMACEN
    # ==========================================
    elif ubicacion == "almacen":
        print()
        print("=" * 55)
        print("ALMACÉN")
        print("=" * 55)
        print("Estantes llenos de cajas polvorientas.")
        print()

        if linterna == False:
            print("Entre las cajas encuentras una LINTERNA. Todavía tiene pila.")
            linterna = True
            inventario.append("Linterna")

        elif destornillador == False:
            print("Revisando una caja de herramientas encuentras un DESTORNILLADOR.")
            destornillador = True
            inventario.append("Destornillador")

        else:
            print("Ya revisaste todo el almacén. No queda nada útil.")

        print()
        input("Presiona ENTER para volver a la recepción...")
        ubicacion = "recepcion"

    # ==========================================
    # HABITACION: OFICINA DEL DIRECTOR
    # ==========================================
    elif ubicacion == "oficina":
        print()
        print("=" * 55)
        print("OFICINA DEL DIRECTOR")
        print("=" * 55)

        if linterna == False:
            print("Está completamente a oscuras. No ves absolutamente nada.")
            print("Necesitas una LINTERNA para entrar aquí.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        elif acertijo_oficina_resuelto == True:
            print("El cajón del escritorio ya está abierto y vacío.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        else:
            print("Enciendes la linterna. Un escritorio enorme domina la habitación.")
            print("El cajón tiene una cerradura con un acertijo grabado:")
            print()
            print('   "Tengo llaves pero no abro cerraduras.')
            print('    Tengo espacio pero no tengo habitaciones.')
            print('    ¿Qué soy?"')
            print()

            if hay_pistas == True:
                print("PISTA: Lo estás usando ahora mismo para escribir.")
                print()

            intentos = intentos_por_acertijo
            resuelto = False

            while intentos > 0 and resuelto == False:
                respuesta = input("Tu respuesta: ")
                respuesta = respuesta.lower().strip()

                if respuesta == "teclado" or respuesta == "un teclado":
                    resuelto = True
                else:
                    intentos = intentos - 1
                    if intentos > 0:
                        print(f"Incorrecto. Te quedan {intentos} intento(s).")
                    else:
                        print("Incorrecto. Te quedaste sin intentos.")

            print()

            if resuelto == True:
                print("El cajón se destraba.")
                print("Dentro hay una TARJETA DE ACCESO con el logo del laboratorio.")
                acertijo_oficina_resuelto = True
                tarjeta = True
                inventario.append("Tarjeta de acceso")
            else:
                print("El cajón sigue trabado. Puedes volver a intentarlo más tarde.")

            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

    # ==========================================
    # PUERTA DE SALIDA
    # ==========================================
    elif ubicacion == "salida":
        print()
        print("=" * 55)
        print("PUERTA DE SALIDA")
        print("=" * 55)
        print("Una puerta blindada con una cerradura, un lector de tarjetas y un teclado numérico.")
        print()

        if llave == False:
            print("La cerradura no cede. Necesitas una LLAVE.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        elif tarjeta == False:
            print("Giras la llave, pero el lector sigue en rojo. Necesitas una TARJETA DE ACCESO.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        elif codigo_descubierto == False:
            print("La llave gira y el lector se pone verde, pero el teclado pide un código de 4 dígitos.")
            print("No tienes idea de cuál es. Necesitas encontrar el CÓDIGO SECRETO.")
            print()
            input("Presiona ENTER para volver a la recepción...")
            ubicacion = "recepcion"

        else:
            print("Tienes la llave, la tarjeta y el código. Este es el momento.")
            print()

            intentos = intentos_por_acertijo
            correcto = False

            while intentos > 0 and correcto == False:
                respuesta = input("Ingresa el código de 4 dígitos: ")
                respuesta = respuesta.strip()

                if respuesta == codigo_secreto:
                    correcto = True
                else:
                    intentos = intentos - 1
                    if intentos > 0:
                        print(f"El teclado emite un pitido de error. Te quedan {intentos} intento(s).")
                    else:
                        print("El teclado se bloquea temporalmente.")

            print()

            if correcto == True:
                print("La puerta blindada se abre lentamente.")
                escapaste = True
                juego_activo = False
            else:
                print("Tendrás que esperar y volver a intentarlo.")
                print()
                input("Presiona ENTER para volver a la recepción...")
                ubicacion = "recepcion"

    else:
        # Por si alguna ubicación queda mal escrita, el jugador no se pierde
        print("Te desorientas y terminas de vuelta en la recepción.")
        ubicacion = "recepcion"

# -----------------
# FINAL DEL JUEGO
# -----------------

print()
print("=" * 55)

if escapaste == True:
    print("¡HAS ESCAPADO DEL LABORATORIO!")
    print("=" * 55)
    print()
    print(f"Felicidades, {nombre}. La luz del sol te golpea la cara después de horas encerrado.")
    print(f"Escapaste llevando {len(inventario)} objeto(s):")
    for objeto in inventario:
        print(f"- {objeto}")
    print()
    print("Detrás de ti, el laboratorio queda en silencio para siempre.")
else:
    print("FIN DE LA PARTIDA")
    print("=" * 55)
    print()
    print(f"El laboratorio te retuvo esta vez, {nombre}.")
    print("Las puertas siguen cerradas... pero siempre puedes volver a intentarlo.")

print()
print("=" * 55)
print("GRACIAS POR JUGAR!")
print("=" * 55)
