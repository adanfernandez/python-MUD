from entidades.Enemigo import Enemigo
from entidades.Jugador import Jugador_normal
from command.Comprar import Cura, Pasar_nivel, Paralisis
from interprete.ReadFile import ReadFile

reader = ReadFile()


def interprete():
    # Obtenemos los enemigos
    enemigos = crear_enemigos()
    # Creamos los objetos que se pueden comprar
    objetos_tienda = establecer_objetos_tienda()
    #print("Bienvenido.")
    print("¿Cómo quieres que se llame tu jugador?")
    nombre = input()
    jugador = Jugador_normal(nombre, enemigos.pop(), objetos_tienda)
    print("¿Cómo quieres jugar:?\n1) Interactivamente\n2) Por medio de un fichero de texto")
    modo = input()
    while modo != str(1) and modo != str(2):
        print("Eliga una opción correcta")
        print("¿Cómo quieres jugar:?\n1) Interactivamente\n2) Por medio de un fichero de texto")
        modo = input()

    if(modo == str(2)):
        reader.read_file("./interprete/comandos.txt")
        while(len(reader.commands) > 0):
            if(jugador.turno):
                action = reader.get_command()
                acciones_posibles = map(lambda x: x.__str__(), jugador.get_acciones_posibles())
                if(action not in acciones_posibles):
                    print("El usuario no puede realizar la acción {}. Revise el fichero".format(action.__str__()))
                    print("Dinero disponible: {}".format(jugador.dinero))
                    print("Vida: {}".format(jugador.vida))
                    print("Nivel: {}".format(jugador.nivel))
                    raise Exception("Fichero incorrecto")
                else:
                    action = [x for x in  jugador.get_acciones_posibles() if action == x.__str__()][0]
                    jugador.accion(action)
                    if (jugador.enemigo.is_muerto()):
                        if len(enemigos) == 0:
                            print("HAS GANADO EL JUEGO. ¡ENHORABUENA!\n\n")
                            break
                        else:
                            jugador.enemigo = enemigos.pop()
                    else:
                        jugador.cambiarTurno()
            else:
                jugador.enemigo.atacar(jugador)
                jugador.cambiarTurno()
                if (jugador.is_muerto()):
                    print("¡Has muerto!\n\n")
                    break
        print("LISTA DE MOVIMIENTOS USADOS")
        for x in jugador.acciones:
            print(x.__doc__)
        if len(reader.commands) == 0:
            print("Se han terminado los movimientos")

    else:
        while True:
            if jugador.turno:
                acciones = jugador.get_acciones_posibles()
                print("Dinero disponible: {} €\nVida restante: {}\nVida restante del enemigo: {}\nAtaque: {}\n\n\n".format(jugador.dinero, jugador.vida, jugador.enemigo.vida, jugador.ataque))
                for i in range(len(acciones)):
                    print("{}) {}".format(i, acciones[i].__str__()))
                numero_accion = int(input())
                while not(numero_accion >= 0 and numero_accion <= len(acciones)):
                    if(numero_accion == len(acciones)):
                        break
                    print("Comando incorrecto")
                    numero_accion = input()
                if(numero_accion == len(acciones)):
                    print("Saliendo del juego...")
                else:
                    accion_aplicar = acciones[numero_accion]
                    jugador.accion(accion_aplicar)
                    if(jugador.enemigo.is_muerto()):
                        if len(enemigos) == 0:
                            print("HAS GANADO EL JUEGO. ¡ENHORABUENA!\n\n")
                            break
                        else:
                            jugador.enemigo = enemigos.pop()
                    else:
                        jugador.cambiarTurno()
            else:
                jugador.enemigo.atacar(jugador)
                jugador.cambiarTurno()
                if(jugador.is_muerto()):
                    print("¡Has muerto!\n\n")
                    break
        print("LISTA DE MOVIMIENTOS USADOS")
        for x in jugador.acciones:
            print(x.__doc__)


def crear_enemigos():
    lista_nombres = ["Pedro Sánchez", "Xoxé María Aznar", "Pablo Iglesias", "Federico Jiménez Losantos", "Gabriel Rufián", "Arturo Pérez Reverte", "José Ángel Fernández Villa", "El caballo de Abascal", "Vicente Álvarez Areces", "Jesús Gil"]
    enemigos = []
    for i in range(len(lista_nombres)):
        nivel = i +1
        enemigo = Enemigo(nivel * 10, nivel, nivel, lista_nombres[i])
        enemigos.append(enemigo)
    enemigos.reverse()
    return enemigos

def establecer_objetos_tienda():
    cura = Cura(200)
    paralisis = Paralisis(100)
    pasar_nivel = Pasar_nivel(600)
    return [cura, paralisis, pasar_nivel]