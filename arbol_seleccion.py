class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

class Nodo:
    def __init__(self, pregunta):
        self.pregunta = pregunta
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):

        if valor.pregunta < nodo.pregunta.pregunta:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor.pregunta > nodo.pregunta.pregunta:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.pregunta == valor:
            return True
        if valor < nodo.pregunta:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    def insertar_nodo(self):
        self._insertar_nodo_recursivo(self.raiz)

    def _insertar_nodo_recursivo(self, raiz):
        if raiz is None:
            print('No pude adiviarlo.')
            dato = input('Ingresa la nueva pregunta\n|:')
            respuesta = input('Ingresa la nueva respuesta\n|:')
            return Nodo(Pregunta(dato, respuesta))
        direccion = input(f"{raiz.pregunta.pregunta} si, no \n|:")
        if direccion == 'si':
            print(f'Es un {raiz.pregunta.respuesta}')
            select = input('si o no?\n|:')
            if select == 'si':
                print('Aja! lo sabia!')
                return raiz
            else:
                print('Rayos!')
                raiz.izquierda = self._insertar_nodo_recursivo(raiz.izquierda)
        elif direccion == 'no':
            raiz.derecha = self._insertar_nodo_recursivo(raiz.derecha)
        else:
            print("Dirección inválida, intenta de nuevo.")
        return raiz



    def obtener_pre_orden(self):
        self.lista = []
        self.pre_orden(self.raiz)
        return self.lista

    def pre_orden(self, nodo):
        if nodo is not None:
            self.lista.append(nodo.pregunta.pregunta)
            self.lista.append(nodo.pregunta.respuesta)
            self.pre_orden(nodo.izquierda)
            self.pre_orden(nodo.derecha)

    def obtener_in_orden(self):
        self.lista = []
        self.in_orden(self.raiz)
        return self.lista

    def in_orden(self, nodo):
        if nodo is not None:
            self.in_orden(nodo.izquierda)
            self.lista.append(nodo.pregunta.pregunta)
            self.lista.append(nodo.pregunta.respuesta)
            self.in_orden(nodo.derecha)

    def obtener_pos_orden(self):
        self.lista = []
        self.pos_orden(self.raiz)
        return self.lista

    def pos_orden(self, nodo):
        if nodo is not None:
            self.in_orden(nodo.izquierda)
            self.lista.append(nodo.pregunta.pregunta)
            self.lista.append(nodo.pregunta.respuesta)
            self.in_orden(nodo.derecha)
def post_orden(nodo):
    if nodo is not None:
        post_orden(nodo.izquierda)
        post_orden(nodo.derecha)
        print(nodo.valor, end=' ')

def in_orden(nodo):
    if nodo is not None:
        in_orden(nodo.izquierda)
        print(nodo.valor, end=' ')
        in_orden(nodo.derecha)