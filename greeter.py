def greet_user():
    """Summary
    """
    print("Hello!")





def bye_user():
    """Summary
    """
    print("Bye!")

def add_user():
    """Summary
    """
    #이것도 되는건가
    print("Welcome")


greet_user()


bye_user()

add_user()


def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다.
    
    Args:
        first_name (TYPE): Description
        last_name (TYPE): Description
    """
    full_name = first_name + ' ' + last_name
    return full_name.title()

#이건 무한 루프입니다.
while  True:
    print("\nPlease tell me your name:")
    f_name = input("First_name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

