from pass_gen import generate_password
from hashing import hash_password


def main_menu():
  print("------------------")
  print("Welcome")
  print("------------------")
  print("1. Hash password")
  print("2. Create password")
  print("3. Create and hash password")
  option = int(input("Type your option: "))

  match option:
    case 1:
      string = input("Type your password: ")
      password_hashed = hash_password(string)
      print("Here you go! ㊙️ = ", password_hashed.hexdigest())
    case 2:
      long = int(input("Type how many characters you want your password: "))
      password = generate_password(long)
      print("Here you go! 👌 = ", password)
    case 3:
      long = int(input("Type how many characters you want your password: "))
      password = generate_password(long)
      password_hashed = hash_password(password)
      print("Here you go! 👌 Password = ", password)
      print("Here you go! ㊙️ Password hashed = ",password_hashed.hexdigest())
