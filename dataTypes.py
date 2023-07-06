# data types are the differetn catergorisation of values that are stored in the memory of a computer
# examples; numeric, string, sequence, mapping, boolean, set.
# numerics(int,float,complex,)
num1 = 1000
num2 = 1000.0
num3 = 0
num4 = 1+5j
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

# String(str)
num5 = "1000"
name = "dennis"
print(type(num5))
print(type(name))

# sequence(list, tuple, range)
my_list = [0, 2, 4, 6]
print(type(my_list))
my_list2 = [0, 2, 4, 6, "denis", 10.5]
print(type(my_list2))
my_tuple = (0, 2, 4, 6)
print(type(my_tuple))

# mapping(dict)
my_dict = {"uganda": "kampala", "italy": "rome",
           "france": "paris", "Tz": "dodoma"}
print(type(my_dict))

# boolean (True, False)

# set examples
my_set = {0, 5, 10, 15, 20}
my_set2 = {5, 5, 10, 10, 15, 15, 20, 20}
print(my_set)
print(my_set2)
print(set(my_dict))
