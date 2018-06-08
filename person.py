def build_person(first_name, last_name, age=''):
    """안녕하세요
    
    Args:
        first_name (TYPE): Description
        last_name (TYPE): Description
        age (str, optional): Description
    """
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('이','규철',age=28)
print(musician)

print("안녕하세요")

