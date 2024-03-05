a = (1,2,3,3)
print(a[0])

#Cuenta cuantas veces aparece un elemento en la tupla
print(a.count(3))

#encontrar indice de elemento en una tupla
print(a.index(2))

#Los sets son parecidas a las listas, no aceptan datos repetidos
a = set ([1, 2, 3])
b = {3, 4, 5}
print(type(a))
print(type(b))

#Ya existe el 3, no modifica el set
a.add(3)
print(a)

# modifica el set
a.add(4)
print(a)

#  muestra los elementos repetidos
print(a.intersection(b))

# unir dos listas sin datos repetidos
print(a.union(b))

# los elementos que esten en uno y no en el otro set(como si fuera un conjunto)
print(a.difference(b))

#elimina
a.remove(2)
print(a)


