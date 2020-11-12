from entidades.Ataque import Cabezazo, Manotazo, Coronavirus, Mordisco
from entidades.Personaje import Personaje
import random


class Enemigo(Personaje):
    """Clase Enemigo"""
    def __init__(self, defensa, ataque, nivel, nombre):
        super().__init__(defensa, ataque, nivel, nombre)
        self.ataques = [Manotazo(self.ataque), Cabezazo(self.ataque), Mordisco(self.ataque), Coronavirus(self.ataque)]
        self.turnosParalizado = 0

    def puedeAtacar(self):
        return self.turnosParalizado == 0

    def calcular_vida(self):
        """
        Calcula la vida del enemigo.
        :return: vida del jugador (int)
        """
        return self.defensa * self.nivel / 2

    def atacar(self, jugador):
        if(self.puedeAtacar()):
            ataque = self.ataques[random.randint(0, len(self.ataques) - 1)]
            print("{} realiza un ataque de {} puntos".format(self.nombre, ataque.puntuacion))
            jugador.recibirAtaque(ataque)
            jugador.comprueba_tipo_usuario()
        if self.turnosParalizado:
            print("{} no puede atacar porque está paralizado\n\n".format(self.nombre))
            self.turnosParalizado -= 1

    def recibirParalisis(self, turnosParalizado: int):
        self.turnosParalizado += turnosParalizado

    def morir(self, jugador):
        print("{} ha muerto".format(self.nombre))
        self.vida = 0
        jugador.recalcular_nivel()
        jugador.recargar_dinero(jugador.nivel * 100)

    def recibirAtaque(self, jugador):
        self.vida -= jugador.ataque
        if not self.is_muerto():
            print("{} ha recibido un ataque de {} puntos. Le quedan {} puntos de vida\n\n".format(self.nombre, jugador.ataque, self.vida))
        else:
            jugador.recalcular_nivel()
            jugador.recargar_dinero(jugador.nivel * 100)
            print("{} ha recibido un ataque de {} puntos. {} ha muerto.\n{} ha ascendido de nivel".format(self.nombre, jugador.ataque, self.nombre, jugador.nombre))


