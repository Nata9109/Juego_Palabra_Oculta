import random

# Decorador para mostrar mensajes antes y después de una función
def mensaje_inicio_fin(func):
    def wrapper(*args, **kwargs):
        print("\n--- Iniciando el juego ---")
        resultado = func(*args, **kwargs)
        print("\n--- Fin del juego ---")
        return resultado
    return wrapper

def elegir_palabra():
    palabras = ['alemania', 'argentina', 'colombia', 'españa', 'bolivia', 'peru', 'ecuador', 'chile']
    return random.choice(palabras)

# Usamos un generador en lugar de una lista
def mostrar_palabra_oculta(palabra, letras_adivinadas):
    return (letra if letra in letras_adivinadas else '_' for letra in palabra)

@mensaje_inicio_fin
def juego():
    palabra = elegir_palabra()
    letras_adivinadas = set()
    vidas = 6
    letras_incorrectas = []

    print(f"La palabra tiene {len(palabra)} letras.")

    while vidas > 0:
        # Convertimos el generador en un string para mostrar la palabra
        print("Palabra:", ''.join(mostrar_palabra_oculta(palabra, letras_adivinadas)))
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        print(f"Tienes {vidas} vidas restantes.")

        letra = input("Introduce una letra: ")

        if len(letra) != 1 or not letra.isalpha():
            print("Error! Ingresa solo una letra.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya has intentado esa letra. Intenta otra.")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            print(f"¡Bien! La letra {letra} está en la palabra.")
        else:
            letras_incorrectas.append(letra)
            vidas -= 1
            print(f"¡Oops! La letra {letra} no está en la palabra.")

        if set(palabra) == letras_adivinadas:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            break

    if vidas == 0:
        print(f"Te quedaste sin vidas. La palabra era: {palabra}")

    jugar_nuevamente = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_nuevamente == 's':
        juego()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

juego()