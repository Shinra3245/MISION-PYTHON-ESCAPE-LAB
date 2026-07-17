# --------------------------
# ETAPA 1
# SALIDA POR CONSOLA
# --------------------------
print("=" * 50)
print("BIENVENIDOS A ESCAPE LAB")
print("=" * 50)


print()
print("Has despertado dentro de un laboratorio secreto, sin recordar cómo llegaste allí.")
print("Tu objetivo es escapar del laboratorio resolviendo acertijos y encontrando pistas.")
print("Tendrás que tomar decisiones y explorar diferentes áreas para avanzar.")
print()

# -----------------
# ETAPA 2
# VARIABLES:RECORDAR INFORMACION
# -----------------

nombre = input("Antes de comenzar, ¿cómo te llamas? ")
print(f"¡Bienvenido, {nombre}! Prepárate para la aventura.")
print("Tu mision es escapar del laboratorio resolviendo acertijos y encontrando pistas.")


# -----------------
# ETAPA 3
# TIPO DE DATOS
# -----------------

print("Selecciona la dificultad del juego:")
print("1. Fácil")
print("2. Normal")
print("3. Difícil")
dificultad = int(input("Ingresa el número correspondiente a la dificultad: "))
print()


# -----------------
# ETAPA 4
# TOMA DE DECISIONES: SELECCION DE RUTA
# -----------------

if dificultad == 1:
    print("Has elegido la dificultad Fácil. Tendrás más pistas y acertijos más sencillos.")
    
elif dificultad == 2:
    print("Has elegido la dificultad Normal. Los acertijos serán desafiantes pero manejables.")
    
elif dificultad == 3:
    print("Has elegido la dificultad Difícil. Prepárate para acertijos complejos y menos pistas.")
    
else:
    print("Opción inválida. Se seleccionará la dificultad Normal por defecto.")
    dificultad = 2
print()
    
# -----------------
# ETAPA 5
# VARIABLES BOOLEANAS
# -----------------

juego_activo = True
llave = False
targeta = False
codigo_descubierto = False


#Estado inicial del juego
print("El laboratiorio esta listo para que comiences tu aventura. Explora y encuentra la manera de escapar.")
print()

# -----------------
# ETAPA 6
# LISTAS
# -----------------
inventario = [] #inventario vacio
print("Tu inventario está vacío. A medida que explores, encontrarás objetos que te ayudarán a escapar.")
print(inventario)

# -----------------
# ETAPA 7
# Darle la capacidad al videojuego de reiniciar y no termine hasta decidirlo
# -----------------

while juego_activo == True:

    print()
    print("=" * 50)
    print("LABORATORIO - RECEPCIÓN")
    print("=" * 50)
    
    print("1. Explorar la recepción")
    print("2. Ver tu inventario")
    print("3. Intentar abrir la puerta de salida")
    print("4. Salir del juego")
    
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        print()
        print("Exploras la recepción y encuentras una llave en el escritorio.")
        
        if not llave:
            print("Encuentras una llave y la agregas a tu inventario.")
            llave = True
            inventario.append("Llave") # Agregamos la llave al inventario
            
        elif not targeta:
            print("Encuentras una tarjeta de acceso en un cajón y la agregas a tu inventario.")
            targeta = True
            inventario.append("Tarjeta de acceso")
            
        elif not codigo_descubierto:
            print("Encuentras un papel con un código secreto escrito en él y lo agregas a tu inventario.")
            codigo_descubierto = True
            inventario.append("Código secreto")
        
        else:
            print("No hay más objetos para encontrar en la recepción.")
    
    elif opcion == 2:
        print()
        print(f"Tu inventario contiene: {inventario}")
        if len(inventario) == 0:
            print("Tu inventario está vacío. Explora para encontrar objetos.")
        else:
            for objeto in inventario:
                print(f"- {objeto}")
    
    elif opcion == 3:
        print()
        print("Intentas abrir la puerta de salida...")
        if not llave:
            print("Necesitas una llave para abrir la puerta.")
        elif not targeta:
            print("Necesitas una tarjeta de acceso para abrir la puerta.")
        elif not codigo_descubierto:
            print("Necesitas un código secreto para abrir la puerta.")
        
        if llave == True and targeta == True and codigo_descubierto == True:
            print("¡Felicidades! Has utilizado la llave, la tarjeta de acceso y el código secreto para abrir la puerta de salida.")
            print("Has escapado del laboratorio con éxito. ¡Fin del juego!")
            juego_activo = False
            
    elif opcion == 4:
        print("Has decidido salir del juego. ¡Hasta la próxima!")
        juego_activo = False
            
    
    