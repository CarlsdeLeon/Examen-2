from arbol_seleccion import ArbolBinario
import guardado


class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

def guardar():
    lista = []
    nombre = input('ingrese el nombre del archivo')
    guardado.guardar_lista(lista, nombre)

def main():
    raiz = None
    arbol1 = ArbolBinario()
    arbol1.insertar(Pregunta('¿Es color cafe?', 'Es un chocolate caliente!'))
    arbol1.insertar(Pregunta('¿Es color rojo?', 'Es un loro!'))
    arbol1.insertar(Pregunta('¿Es color negro?', 'Es un cafe!'))
    selct = input('¿Desea cargar un archivo?')

    while True:
        arbol1.insertar_nodo()
        select = input('¿Desea volver a intentar? si, no\n|:')
        if select == 'no':
            print('¿Deseas guardarlo?')
            break

main()
