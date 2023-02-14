example = True
string = "Example"
number = 12
float_number = 12.3

print(type(example))
print(type(string))
print(type(number))
print(type(float_number))


class Car:
  model = ""
  year = ""
  brand = ""

  def __init__(self, model, year, brand):
    self.model = model
    self.year = year
    self.brand = brand

  def __str__(self):
    # example = self.model + "+" + self.year
    return f"Model: {self.model} Year: {self.year} Brand: {self.brand}" # `${Variable} texto ${variable} `


mazda6 = Car("Mazda 6", 2023, "Mazda")

print(mazda6.year,mazda6.brand, mazda6.year)
print(mazda6.__str__())