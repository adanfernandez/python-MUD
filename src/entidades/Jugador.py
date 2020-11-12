from command.Atacar import Atacar
from command.Cura import Cura
from command.Pasar_nivel import Pasar_nivel
from command.Paralisis import Paralisis
from command.Peste import Peste
from entidades.Personaje import Personaje


class Jugador(Personaje):
    """Clase jugador"""
    def __init__(self, nombre, enemigo, objetos_tienda):
        super().__init__(50, 5, 1, nombre)
        self.dinero: int = 100
        self.objetos = dict()
        self.objetos_iniciales()
        self.enemigo = enemigo
        self.turno = True
        self.objetos_tienda = objetos_tienda

    def objetos_iniciales(self):
        """
        Carga los objetos iniciales del jugador.
        Inicialmente no tendrá ningún objeto cargado.
        :return: void
        """
        self.objetos['cura']: int = 0
        self.objetos['pasar_nivel']: int = 0
        self.objetos['paralisis']: int = 0


    def recargar_dinero(self, dinero):
        """
        Al jugador se le añade dinero al que previamente tenía
        :param dinero: dinero a añadir
        :return: void
        """
        self.dinero += dinero


    def cura(self):
        """
        Si el jugador tiene algún objeto cura, se le aplicará para volver a tener la vida completa.
        :return: void
        """
        if self.objetos['cura'] > 0:
            self.vida = self.calcular_vida()
            self.objetos['cura'] -= 1


    def comprueba_tipo_usuario(self):
        if(self.vida <= 20):
            self.__class__ = Jugador_herido
            print("El jugador {} está gravemente herido. Ahora los ataques le afectarán la mitad y tendrá 2 por 1 en las tiendas.".format(self.nombre))
        else:
            self.__class__ = Jugador_normal
            print("El jugador {} está en un estado de un jugador normal.".format(self.nombre))


    def ataque_peste(self):
        if self.nivel == 4 or self.nivel == 8:
            self.__setattr__('peste', True)
            print("Capacidad de utilizar la 'peste' añadida")


    def accion(self, orden):
        #Mangling
        attrs = [x for x in orden.__dir__() if 'execute' in x]
        if(attrs[0]):
            self.insertar_acciones(orden.__class__)
            orden.execute(self)
            self.ataque_peste()


    def recalcular_herido(self):
        self.defensa *= 2
        self.ataque *= 2

    def recalcular_nivel(self):
        self.nivel +=1
        self.calcular_vida()

    def get_acciones_posibles(self):
        acciones = [Atacar()]
        if(self.objetos['cura']):
            acciones.append(Cura())
        if (self.objetos['paralisis']):
            acciones.append(Paralisis())
        if (self.objetos['pasar_nivel']):
            acciones.append(Pasar_nivel())
        if('peste' in self.__dir__()):
            acciones.append(Peste())
        for objeto in self.objetos_tienda:
            if self.dinero >= objeto.precio:
                acciones.append(objeto.get_accion_comprar())
        return acciones

    def cambiarTurno(self):
        self.turno = not self.turno

    def usar_objeto(self, objeto):
        self.objetos[objeto] -= 1



class Jugador_herido (Jugador):

    """Clase de un jugador herido"""

    def incrementar_objetos(self, objeto):
        self.objetos[objeto] += 2

    def recibirAtaque(self, ataque):
        ataque_puntuacion = ataque.puntuacion
        self.vida -= ataque_puntuacion/2
        if not self.is_muerto():
            print("{} ha recibido un ataque de {} puntos. Le quedan {} puntos de vida\n\n".format(self.nombre, ataque_puntuacion, self.vida))
        else:
            print("{} ha recibido un ataque de {} puntos. {} ha muerto".format(self.nombre, ataque_puntuacion, self.nombre))
        return self.is_muerto()







class Jugador_normal(Jugador):
    """Clase de un jugador normal"""
    def incrementar_objetos(self, objeto):
        self.objetos[objeto] += 1
    def recibirAtaque(self, ataque):
        ataque_puntuacion = ataque.puntuacion
        self.vida -= ataque_puntuacion
        if not self.is_muerto():
            print("{} ha recibido un ataque de {} puntos. Le quedan {} puntos de vida\n\n".format(self.nombre, ataque_puntuacion, self.vida))
        else:
            print("{} ha recibido un ataque de {} puntos. {} ha muerto".format(self.nombre, ataque_puntuacion, self.nombre))
        return self.is_muerto()