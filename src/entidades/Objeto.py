from command.Comprar import Comprar_paralisis, Comprar_pasar_nivel, Comprar_cura


class Cura:
    def __int__(self):
        pass

    def __init__(self, precio):
        self.precio = precio

    def get_accion_curar(self):
        return Comprar_cura()

    def __str__(self):
        return "Aplicar cura"

class Pasar_nivel:
    def __int__(self):
        pass

    def __init__(self, precio):
        self.precio = precio

    def get_accion_comprar(self):
        return Comprar_pasar_nivel()

    def __str__(self):
        return "Aplicar pasar nivel"

class Paralisis:
    def __int__(self):
        pass

    def __init__(self, precio):
        self.precio = precio

    def get_accion_comprar(self):
        return Comprar_paralisis()

    def __str__(self):
        return "Aplicar parálisis al enemigo"
