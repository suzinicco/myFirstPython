numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

digits = list(range(1,10))
print(min(digits))
print(max(digits))
print(sum(digits))


players = ['charles','martina','michael','michael','florence','eli']

for player in players[-1:]:
	print(player.title())


my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[2:]

print("list 1 ")
print(my_foods)

print("list 2")
print(friend_foods)