class Pasar_nivel:
    """Aplicar Pasar Nivel"""
    def execute(self, jugador):
        jugador.enemigo.morir(jugador)
        jugador.usar_objeto('pasar_nivel')
        print("{} ha pasado de nivel\n\n".format(jugador.nombre))

    def __str__(self):
        return "Aplicar pasar nivel"
