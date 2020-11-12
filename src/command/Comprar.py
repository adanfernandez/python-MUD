class Comprar_cura:
    """Compra de cura"""
    def execute(self, jugador):
        jugador.incrementar_objetos('cura')
        precio_cura = list(filter(lambda x: isinstance(x, Cura), jugador.objetos_tienda))[0].precio
        jugador.recargar_dinero(precio_cura * -1)
        print("{} ha comprado una cura\n\n".format(jugador.nombre))

    def __str__(self):
        return "Comprar objeto cura"


class Comprar_paralisis:
    """Compra de parálisis"""
    def execute(self, jugador):
        jugador.incrementar_objetos('paralisis')
        precio_paralisis = list(filter(lambda x: isinstance(x, Paralisis), jugador.objetos_tienda))[0].precio
        jugador.recargar_dinero(precio_paralisis*-1)
        print("{} ha comprado una parálisis\n\n".format(jugador.nombre))

    def __str__(self):
        return "Comprar objeto paralisis"


class Comprar_pasar_nivel:
    """Compra de Pasar Nivel"""
    def execute(self, jugador):
        jugador.incrementar_objetos('pasar_nivel')
        precio_pasar_nivel = list(filter(lambda x: isinstance(x, Pasar_nivel), jugador.objetos_tienda))[0].precio
        jugador.recargar_dinero(precio_pasar_nivel * -1)
        print("{} ha comprado un pasar nivel\n\n".format(jugador.nombre))

    def __str__(self):
        return "Comprar objeto pasar nivel"


class Cura:
    def __int__(self):
        pass

    def __init__(self, precio):
        self.precio = precio

    def get_accion_comprar(self):
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
        return "Aplicar paralisis"