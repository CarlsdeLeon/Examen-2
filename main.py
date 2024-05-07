from arbol_seleccion import ArbolBinario
from Guardados import guardado


class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

def guardar(arbol1):

    lista1 = arbol1.obtener_pre_orden()
    lista2 = arbol1.obtener_in_orden()
    lista3 = arbol1.obtener_pos_orden()
    nombre1 = input('ingrese el nombre del archivo inorden')
    nombre2 = input('ingrese el nombre del archivo posorden')
    nombre3 = input('ingrese el nombre del archivo preorden')
    guardado.guardar_lista(lista2, nombre1)
    guardado.guardar_lista(lista3, nombre2)
    guardado.guardar_lista(lista1, nombre3)

def main():
    raiz = None
    arbol1 = ArbolBinario()
    arbol1.insertar(Pregunta('¿Es color cafe?', 'Es un chocolate caliente!'))
    arbol1.insertar(Pregunta('¿Es color rojo?', 'Es un loro!'))
    arbol1.insertar(Pregunta('¿Es color negro?', 'Es un cafe!'))

    while True:
        arbol1.insertar_nodo()
        select = input('¿Desea volver a intentar? si, no\n|:')
        if select == 'no':
            break

main()
