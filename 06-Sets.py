##Sets##

my_set  = set()

my_other_set = {}

print(type(my_set))

print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {35, 1.8, "Diego", "Benito"}

print(type(my_other_set))

print(len(my_other_set))


my_other_set.add("theclich2")

print(my_other_set) #Los set no son estructuras ordenadas.


my_other_set.add("theclich2") #Un set no admite repetidos.


print(my_other_set)

print("Diego" in my_other_set) ##Realización de hacer busquedas.

print("Dieg" in my_other_set)

my_other_set.remove("Diego")

print(my_other_set)

my_other_set.add("Diego")

print(my_other_set)


my_other_set.clear() ##Limpia los elementos del set.

print(my_other_set)

print(len(my_other_set))


my_set =  {"Diego","Benito", 19}
my_list= list(my_set)
print(my_list)

print(my_list[1])

my_other_set = {"CSS","HTML","JavaScript"}

my_new_set = my_set.union(my_other_set)

print(my_new_set.union(my_new_set))







