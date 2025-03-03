import os
from pelicula import Pelicula

class CatalogoPelicula:
    def __init__(self, nombre_catalogo):
        self.nombre = nombre_catalogo
        self.ruta_archivo = f"{self.nombre}.txt"

    def agregar(self, pelicula):
        """Agrega una película al archivo"""
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(pelicula.get_nombre() + "\n")
        print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")

    def listar(self):
        """Lista las películas almacenadas en el archivo"""
        if not os.path.exists(self.ruta_archivo):
            print("El catálogo está vacío o no existe.")
            return
        
        print("\nPelículas en el catálogo:")
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            peliculas = archivo.readlines()
            for i, pelicula in enumerate(peliculas, 1):
                print(f"{i}. {pelicula.strip()}")

    def eliminar(self):
        """Elimina el archivo del catálogo"""
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"El catálogo '{self.nombre}' ha sido eliminado.")
        else:
            print("El catálogo no existe.")