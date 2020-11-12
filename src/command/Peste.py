class Peste:
    """Aplicar Peste"""
    def execute(self, jugador):
        print("{} ha atacado al enemigo con la peste".format(jugador.nombre))
        jugador.enemigo.morir(jugador)
        jugador.__delattr__('peste')
        print("El jugador ya no tiene la peste")

    def __str__(self):
        return "Atacar con la peste"