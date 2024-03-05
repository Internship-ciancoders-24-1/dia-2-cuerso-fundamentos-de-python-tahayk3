#Diccionarios, son clave valor
rea = {}
rea['pizza'] = 'La comida mas deliciosa del mundo'
print(rea)
#se puede ingresar al contenido por medio de su clave
print(rea['pizza'])
print(rea.keys())
print(rea.items())

#iterar
for key in rea.keys():
    print(key)

for key in rea.values():
    print(key)

for key in rea.items():
    print(key)




