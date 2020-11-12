class Atacar:
    """Ataque al enemigo"""
    def execute(self, jugador):
        print("{} ha atacado al enemigo con un ataque de {} puntos".format(jugador.nombre, jugador.ataque))
        jugador.enemigo.recibirAtaque(jugador)

    def __str__(self):
        return "Atacar al enemigo"