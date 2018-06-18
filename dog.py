class Dog():

    """개를 모델화하는 시도
    """
    def __init__(self, name, age):
        """name과 age 속성 초기화
        
        Args:
            name (TYPE): Description
            age (TYPE): Description
        """
        self.name = name
        self.age = age

    def sit(self):
        """명령에 따라 앉는 개
        """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """명령에 따라 구르는 개
        """
        print(self.name.title() + " rolled over!")



my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()


