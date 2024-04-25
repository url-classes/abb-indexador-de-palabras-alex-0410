from binary_tree import ArbolBinario

if __name__ == "__main__":
    palabras = ["manzana", "banano", "naranja", "limon", "kiwi", "mango", "durazno", "uva"]
    arbol = ArbolBinario()

    for palabra in palabras:
        arbol.insertar(palabra)

    print("Las palabras ordenadas en el árbol binario son:")
    print(arbol)
