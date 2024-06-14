#### Listas ####

my_list = [1,2,3,4]

print(my_list)
print(len(my_list))

my_other_list = [19,1.80,"Diego", "Benito"]
print(my_other_list)

my_other_list.append("Martínez")

print(my_other_list)

my_other_list.insert(5,"Ciclismo")

print(my_other_list)

my_other_list.remove(1.80)

print(my_other_list)


my_list.append(4)

my_list.pop()
print(my_list)
print(my_list.pop())

del my_other_list[0]

print(my_other_list)

my_new_list = my_other_list.copy()

my_other_list.clear()
print(my_other_list)
print(my_new_list)
my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)


