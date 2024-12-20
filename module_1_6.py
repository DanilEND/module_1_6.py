my_dict={"Danil":2001, "Elina":2005, "Nikita":2000, "Vadim":2002}
print(my_dict)
print(my_dict["Elina"])
print(my_dict.get ("Egor"))
my_dict.update ({"Slava": 1999, "Pasha": 1998})
print(my_dict)
del (my_dict) ["Danil"]
print (my_dict)


my_set= {1,2,3,4, "Danil", 1.3, "True", (2,3,4), "Danil", 4,2}
print (my_set)
print(my_set.add(10))
print(my_set.add("Elina"))
print(my_set)
print (my_set.discard("Danil"))
print (my_set)