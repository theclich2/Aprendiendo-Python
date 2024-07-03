###Tuplas###
## Definición de tupla de dos diferentes formas.

my_tuple = tuple()

my_other_tuple = (30,60,30)

my_tuple = (35, 1.8, "Diego", "Benito","Diego")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])

print(my_tuple[2])




print(my_tuple.count("Diego"))

print(my_tuple.index("Benito"))

print(my_tuple.index("Diego"))

#my_tuple[1] = 1.82 'tuple' object does not support item assignment error debido a que las tuplas son constantes y no variables como en las listas.
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[2:4])

my_tuple= list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"

my_tuple.insert(1,"Azul")

my_tuple = tuple(my_tuple)

print(my_tuple)

print(type(my_tuple))

#del my_tuple # El del en las tuplas elimina la tupla no limpia su contenido como en las listas.
print(my_tuple)
