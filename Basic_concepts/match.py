
letter = input("Type a letter: ")

match letter:
  case("A" | "a"):
    print("A This a vowel")
  case("E" | "e"):
    print("E This a vowel")
  case("I" | "i"):
    print("I This a vowel")
  case("O" | "o"):
    print("O This a vowel")
  case("U" | "u"):
    print("U This a vowel")
  case _:
    print("Is not a vowel")