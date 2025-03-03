class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado

    def get_nombre(self):
        return self.__nombre  # Método para obtener el nombre

    def __str__(self):
        return self.__nombre