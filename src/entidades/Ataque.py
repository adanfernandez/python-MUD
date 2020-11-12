class Ataque:
    """Clase Ataque de un enemigo"""
    def __init__(self):
        self.puntuacion = 0

    def __str__(self):
        return "Atacar al jugador"



class Manotazo (Ataque):
    """Clase Manotazo"""
    def __init__(self, ataque):
        super().__init__()
        self.puntuacion = ataque * 0.4

class Cabezazo (Ataque):
    """Clase Cabezazo"""
    def __init__(self, ataque):
        super().__init__()
        self.puntuacion = ataque * 0.6

class Mordisco (Ataque):
    """Clase Mordisco"""
    def __init__(self, ataque):
        super().__init__()
        self.puntuacion = ataque * 0.8

class Coronavirus (Ataque):
    """Clase Coronavirus"""
    def __init__(self, ataque):
        super().__init__()
        self.puntuacion = ataque