requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")