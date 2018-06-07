responses = {}

#설문이 활성화됐다는 플래그를 설정합니다.
polling_active = True

while polling_active:
    name = input("\nWhat is you name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n---- Poll Results ----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")