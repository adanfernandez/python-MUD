class Paralisis:
    """Aplicar parálisis"""
    def execute(self, jugador):
        jugador.enemigo.recibirParalisis(3)
        jugador.usar_objeto('paralisis')
        print("Se ha paralizado al enemigo\n\n")

    def __str__(self):
        return "Aplicar paralisis al enemigo"

