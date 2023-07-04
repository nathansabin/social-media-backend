userInput = "example@gmail.com"

if "@" in userInput and ".":
    print("@ was found")
else:
    print("syntax error")

print(list(userInput))