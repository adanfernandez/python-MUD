from entidades.Ataque import Ataque


class Personaje:
    """Clase Personaje, de donde heredarán las clases Jugador y Enemigo"""
    def __init__(self, defensa, ataque, nivel, nombre):
        self.defensa: int = defensa
        self.ataque: int = ataque
        self.nivel: int = nivel
        self.nombre = nombre
        self.vida = self.calcular_vida()
        self.acciones = []

    def is_muerto(self):
        return self.vida <= 0

    def calcular_vida(self):
        """
        Calcula la vida de un jugador sin estar herido, que será el producto de la defensa por el nivel.
        :return: vida del jugador (int)
        """
        return self.defensa * self.nivel

    def insertar_acciones(self, clase):
        self.acciones.append(clase)
