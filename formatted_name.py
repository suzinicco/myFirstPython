def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다.
    
    Args:
        first_name (TYPE): Description
        last_name (TYPE): Description
    """
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)




def get_formatted_name2(first_name, last_name, middle_name=''):
    """매개변수에 기본값을 설정해서 사용자가 매개변수를 넘기지 않아도 동작
    
    Args:
        first_name (TYPE): Description
        last_name (TYPE): Description
        middle_name (str, optional): Description
    
    Returns:
        TYPE: Description
    """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name2('jimi','hendrix')
print(musician)

musician = get_formatted_name2('first','last','middle')
print(musician)

