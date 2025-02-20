import random

def elegir_palabra():
    # Lista de palabras para adivinar
    palabras = ['alemania', 'argentina', 'colombia', 'españa', 'bolivia', 'peru', 'ecuador', 'chile']
    # Elegir una palabra aleatoria
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    # Mostrar la palabra con guiones bajos y las letras adivinadas
    return ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def juego():
    # Palabra a adivinar
    palabra = elegir_palabra()
    # Letras adivinadas por el jugador
    letras_adivinadas = set()
    # Número de vidas
    vidas = 6
    # Letras incorrectas
    letras_incorrectas = []

    print("¡Bienvenido al juego de Adivina la Palabra!")
    print(f"La palabra tiene {len(palabra)} letras.")
    
    # Bucle principal del juego
    while vidas > 0:
        # Mostrar la palabra oculta y las letras incorrectas
        print("Palabra:", mostrar_palabra_oculta(palabra, letras_adivinadas))
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        print(f"Tienes {vidas} vidas restantes.")
        
        # Pedir una letra al jugador
        letra = input("Introduce una letra: ")

        # Validar que el jugador ingrese solo una letra
        if len(letra) != 1 or not letra.isalpha():
            print("Error! el dato ingresado no es una letra, por favor solo ingresa letras")
            continue
        
        # Verificar si la letra ya fue adivinada
        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya has intentado esa letra. Intenta otra.")
            continue
        
        # Comprobar si la letra está en la palabra
        if letra in palabra:
            letras_adivinadas.add(letra)
            print(f"¡Bien! La letra {letra} está en la palabra.")
        else:
            letras_incorrectas.append(letra)
            vidas -= 1
            print(f"¡Oops! La letra {letra} no está en la palabra.")
        
        # Verificar si el jugador ha adivinado todas las letras
        if set(palabra) == letras_adivinadas:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break
        
    # Fin del juego
    if vidas == 0:
        print(f"Te quedaste sin vidas. La palabra era: {palabra}")
    
    # Preguntar si quiere jugar nuevamente
    jugar_nuevamente = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_nuevamente == 's':
        juego()  # Reinicia el juego
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# Iniciar el juego
juego()