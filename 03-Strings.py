## Strings ##

my_string = "Mi string"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))
print(my_string,my_other_string)
print()
print()
my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)
print()
print()
my_tab_line_string = "Este es un string\tcon tabulación"
print(my_tab_line_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string) 

####  Formateo ####
name, surname, age = "Diego", "Benito", 19
print("Mi nombre es: {} {} y mi edad es {}".format(name,surname,age) )

print("Mi nombre es: %s %s y mi edad es %d" %(name,surname,age))

## Desempaquetado de caracteres
language = "python"
a, b,c ,d, e, f = language
print(a)
print(b)


### División ###
language_slice = language[2:6]
print(language_slice)

## Reverse ##
reversed_language = language[::-1]
print(reversed_language)

##Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t "))
print(language.isnumeric())
print(language.lower())
print(language.upper().islower())

