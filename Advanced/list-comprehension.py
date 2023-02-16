# Lists comprehensions: They are a shorter version of a list declaration, it is used to filter, modify and remove data.
my_list = ["Delia","Francisco", "Victor", "Maria", "Maria", "Luis"]


new_list = [ element for element in my_list if element == "Maria"] #Lists comprehension


print(my_list)
new_list.append("Daniel")
print(new_list)