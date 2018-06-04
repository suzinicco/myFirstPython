alien_0 = {'color': 'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print(alien_0['y_position'])


user_0 = { 'username':'efermi',
'first':'enrico',
'last':'fermi'}

for key, value in user_0.items():
    print("\nKey:" + key)
    print("Value:" + value)


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'lee':'anything',
    'phil':'python,'
}

friends = ['phil','sarah','lee']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("   Hi " + name.title() + " I see your favorite language is " + favorite_languages[name].title() + "!")
    else:
        print("Nice to meet you " + name.title() + " How are you?")

if 'erin' not in favorite_languages.keys():
    print("Erin please take our poll!!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll.")

# 세트는 리스트와 비슷하지만, 세트의 각 항목은 반드시 단 하나만 존재한다
for language in set(favorite_languages.values()):
    print(language.title())
