#Variables

Myvariable = "My String variable"
print(Myvariable)
print("Hola", Myvariable)

#Cambio de tipo de dato de una variable
numero1= 2
print(numero1)
print(type(numero1))
print()
print()
print()
print("Cambio de entero a string")
print(str(numero1))
print(type(str(numero1)))

# Concatenación
print("Esto es una prueba de concatenación:",numero1)

# Funciones del sistema
print(len(Myvariable)) #Length

# Variables en una sola linea

name,surname,alias,age= "Diego", "Benito","theclich2",19
print("Mi nombre es:",name,surname,"Tengo",age,"años.","Y mi alias es:",alias)

# Introducción de datos con inputs (Es el Scanner de JAVA)
"""
name = (input("Cuál es tú nombre?"))
age = (input("Cuál es tú edad?"))

print(name,age)
"""

# Cambiamos su tipo

name=35
age="Brais"
print(name,age)
print("******************************************************************")
# Forzamos el tipo (No sirve de nada)
address: str = "Mi dirección"
address= 32
print(address)
print(type(address))