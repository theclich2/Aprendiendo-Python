####### Diccionarios #######

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Diego","Apellido":"Benito","Edad":19, 1:"Python"}

my_dict = {
    "Nombre": "Diego",
    "Apellido":"Benito",
    "Edad":19,
    "Lenguajes":{
        "Python","Switft","Kotlin"
    },
    1:1.80
}

print(my_other_dict)
print(my_dict)


print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict[1])

my_dict["Calle"] = "Ruidera" 

print(my_dict)

del my_dict["Calle"]

print(my_dict)

print("Diego" in my_other_dict) ##Realización de hacer busquedas.

print("Apellido" in my_other_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list= ["Nombre",1,"Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)


my_new_dict = dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,("Diego","Benito"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,(my_dict,"Diego"))
print(my_new_dict.values())
print()
print(list(my_new_dict))
print()
print(tuple(my_new_dict))
print()
print(set(my_new_dict))
print()




























