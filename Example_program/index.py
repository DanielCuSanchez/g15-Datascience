from hashing import hash_password

def main():
  print("Main is running 🏃")
  string = input("Type your password: ")
  password_hashed = hash_password(string)
  print("Here you go! 👌 = ", password_hashed.hexdigest())



if __name__ == "__main__":
  main()