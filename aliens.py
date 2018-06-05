# 딕셔너리를 리스트에 저장하거나 리스트를 딕셔너리 값으로 저장해야 할 때가 있습니다. 이걸 중첩, nesting 이라 부릅니다.
# 
# 딕셔너리를 리스트에
# 리스트를 딕셔너리에
# 딕셔너리를 다른 딕셔너리에
# 

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)



aliens2 = []

for alien_number in range(130):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens2.append(new_alien)

for alien in aliens2[:100]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens2)))



#딕셔너리 안에 리스트 담기
pizza = {'crust':'thick',
'toppings':['mushrooms','txtra cheese']}

print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)



favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + " 's favorite_languages are: ")
    for language in languages:
        print("\t" + language.title())

