from command.Comprar import Comprar_cura

class Cura:
    """Aplicar cura"""
    def execute(self, jugador):
        jugador.vida = jugador.calcular_vida()
        jugador.usar_objeto('cura')
        print("{} tiene toda la vida de nuevo habiendo aplicado el objeto cura. Ahora tiene {} puntos de vida".format(jugador.nombre, jugador.vida))

    def __str__(self):
        return "Aplicar cura"

    def get_accion_comprar(self):
        return Comprar_cura()