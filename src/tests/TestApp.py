import unittest
from command.Atacar import Atacar
from command.Comprar import Comprar_paralisis
from command.Paralisis import Paralisis
from command.Cura import Cura
from command.Pasar_nivel import Pasar_nivel
from command.Peste import Peste
from entidades.Jugador import Jugador_normal, Jugador_herido
from interprete.interprete import establecer_objetos_tienda, crear_enemigos

class TestUM(unittest.TestCase):

    def setUp(self):
        objetos_tienda = establecer_objetos_tienda()
        enemigos = crear_enemigos()
        self.jugador = Jugador_normal('Adi', enemigos.pop(), objetos_tienda)


    def test_inicializacion(self):
        self.assertEqual(self.jugador.defensa, 50)
        self.assertEqual(self.jugador.ataque, 5)
        self.assertEqual(self.jugador.nivel, 1)
        self.assertEqual(self.jugador.dinero, 100)
        self.assertEqual(self.jugador.nombre, 'Adi')
        acciones_posibles = self.jugador.get_acciones_posibles()
        self.assertEqual(len(acciones_posibles), 2)
        self.assertTrue(isinstance(acciones_posibles[0], Atacar))
        self.assertTrue(isinstance(acciones_posibles[1], Comprar_paralisis))


    def test_matar_enemigo(self):
        dinero_inicial = self.jugador.dinero
        self.jugador.accion(Atacar())
        self.assertEqual(0.0, self.jugador.enemigo.vida)
        self.assertGreater(self.jugador.dinero, dinero_inicial)


    def test_comprar(self):
        numero_paralisis = self.jugador.objetos['paralisis'] + 1
        self.jugador.accion(Comprar_paralisis())
        self.assertEqual(0, self.jugador.dinero)
        self.assertEqual(self.jugador.objetos['paralisis'], numero_paralisis)


    def test_recargar_dinero(self):
        self.jugador.recargar_dinero(1000)
        self.assertEqual(1100, self.jugador.dinero)
        self.jugador.recargar_dinero(-1000)
        self.assertEqual(100, self.jugador.dinero)


    def test_atacar_enemigo(self):
        vida_inicial = self.jugador.vida
        self.jugador.enemigo.atacar(self.jugador)
        self.assertGreater(vida_inicial, self.jugador.vida)


    def test_paralizado(self):
        self.jugador.accion(Paralisis())
        self.assertGreater(self.jugador.enemigo.turnosParalizado, 0)


    def test_cura(self):
        self.jugador.vida = 1
        self.jugador.accion(Cura())
        self.assertEqual(self.jugador.vida, self.jugador.defensa * self.jugador.nivel)


    def test_pasar_nivel(self):
        self.jugador.accion(Pasar_nivel())
        self.assertEqual(self.jugador.enemigo.vida, 0)


    def test_cambiar_estado(self):
        self.assertTrue(isinstance(self.jugador, Jugador_normal))
        self.jugador.vida = 10
        self.jugador.comprueba_tipo_usuario()
        self.assertTrue(isinstance(self.jugador, Jugador_herido))
        self.jugador.vida = 500
        self.jugador.comprueba_tipo_usuario()
        self.assertTrue(isinstance(self.jugador, Jugador_normal))


    def test_comprar_jugador_herido(self):
        self.jugador.__class__ = Jugador_herido
        self.jugador.incrementar_objetos('pasar_nivel')
        self.jugador.incrementar_objetos('paralisis')
        self.jugador.incrementar_objetos('cura')
        self.assertTrue(self.jugador.objetos['pasar_nivel'], 2)
        self.assertTrue(self.jugador.objetos['paralisis'], 2)
        self.assertTrue(self.jugador.objetos['cura'], 2)


    def test_ataque_defensa_jugador_herido(self):
        ataque_inicial = self.jugador.ataque
        defensa_inicial = self.jugador.defensa
        self.jugador.__class__ = Jugador_herido
        self.jugador.recalcular_herido()
        ataque_final = self.jugador.ataque
        defensa_final = self.jugador.defensa
        self.assertTrue(ataque_final == ataque_inicial * 2)
        self.assertTrue(defensa_final == defensa_inicial * 2)


    def test_peste(self):
        self.assertFalse('peste' in self.jugador.__dir__())
        self.jugador.nivel = 4
        self.jugador.ataque_peste()
        self.assertTrue('peste' in self.jugador.__dir__())
        nivel = self.jugador.nivel +1
        self.jugador.accion(Peste())
        self.assertEqual(nivel, self.jugador.nivel)



    def recibir_ataque(self):
        vida_inicial = self.jugador.vida
        self.jugador.enemigo.atacar(self.jugador)
        self.assertGreater(vida_inicial, self.jugador.vida)