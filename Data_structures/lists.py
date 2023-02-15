# Lists: They are indexed, they can have duplicated values and they can be ordered, changeable

students = ["Delia","Carlos","Angel","Ricardo"]

print(students)
print(type(students))
print(len(students))


for i in range(len(students)):
  print(students[i])

students[0] = "Valeria"

for i in range(len(students)):
  print(students[i])

students2 = students.copy()

students2[0] = "Jonathan"

for i in range(len(students)):
  print(students[i])
  print(students2[i])
