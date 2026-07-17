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



