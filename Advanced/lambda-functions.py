# Lambda functions: Is a reserved word for using to create shorter versions of functions.

# lambda arguments : expression
def sum(n1, n2):
  return n1+n2

# sum = (n1, n2) =>  n1+n2
sum_example = lambda n1, n2 : n1 + n2


def main_function(param2): #2
  return lambda param: param * param2 #2


table_two = main_function(2) #lambda param: param * 2
table_tree = main_function(3) #lambda param: param * 3

print(table_two(1))
print(table_two(2))
print(table_two(3))
print(table_two(4))


for i in range (0,100):
  print("Table 2 x ",i," = ", table_two(i))
  print("Table 3 x ",i," = ",table_tree(i))




#print(sum(1,2))
#print(sum_example(1,2))