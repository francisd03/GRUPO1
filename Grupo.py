lista = []  # Creando una lista en blanco
lista.append("celular")  # agregando un elemento
print(lista)

# agregando un elemento en la primera posicion
lista = ["cuaderno", "libro"]
lista.insert(0, "lapiz")
print(lista)

# agregar un elemento en la ultima posicion
lista = ["ventana", "puerta"]
lista.append("techo")
print(lista)

lista = ["escritorio", "engrapadora", "tijera"]
# Buscamos la posicion o el indice de la engrapadora
posicion = lista.index("engrapadora")
# Agregamos un elemento luego de la posicion dada, por eso el + 1
lista.insert(posicion + 1, "saca grapa")

print(lista)
