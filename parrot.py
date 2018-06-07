message = input("Tell me something and I will repeat it back to you: ")
print(message)


prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)

print("\nHello " + name + " !")

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You so old!!")
    

