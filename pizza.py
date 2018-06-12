def make_pizza(*toppings):
    """주문받은 토핑 리스트 출력
    
    Args:
        *toppings: Description
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(" - " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
