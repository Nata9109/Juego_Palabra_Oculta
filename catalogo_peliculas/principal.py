from catalogo import CatalogoPelicula
from pelicula import Pelicula

def menu():
    nombre_catalogo = input("Ingrese el nombre del catálogo: ")
    catalogo = CatalogoPelicula(nombre_catalogo)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar(pelicula)

        elif opcion == "2":
            catalogo.listar()

        elif opcion == "3":
            catalogo.eliminar()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()