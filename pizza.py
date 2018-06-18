def make_pizza(size, *toppings):
    """주문받은 토핑 리스트 출력
    
    Args:
        *toppings: Description
    """
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print(" - " + topping)