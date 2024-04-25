from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, nodo_actual, clave):
        if clave < nodo_actual.clave:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(clave)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, clave)
        elif clave > nodo_actual.clave:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(clave)
            else:
                self._insertar_recursivo(nodo_actual.derecho, clave)

    def inorden(self):
        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            return self._inorden_recursivo(nodo.izquierdo) + [nodo.clave] + self._inorden_recursivo(nodo.derecho)
        else:
            return []

    def __str__(self):
        return ", ".join(self.inorden())
