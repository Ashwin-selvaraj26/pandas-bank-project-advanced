class Some:
    def __init__(self):
        self.__balance = 0

    def view(self) :
        print(self.__balance)
        
        
somenum = Some()

print(somenum.__balance)