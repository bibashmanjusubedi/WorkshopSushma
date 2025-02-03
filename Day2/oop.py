# Step 1: Define a Class
class Person:
    # Constructor (__init__) to initialize attributes
    def __init__(self, name, age):
        self.name = name   # Instance variable
        self.age = age

    # Method to display person's details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Step 2: Create an Object of the Person class
person1 = Person("Alice", 25)
person1.display_info()

# Step 3: Demonstrate Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent class constructor
        self.student_id = student_id

    # Method Overriding (Polymorphism)
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

# Step 4: Create an Object of the Student class
student1 = Student("Bob", 20, "S123")
student1.display_info()

# Step 5: Demonstrate Encapsulation (Private Attribute)
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance

    # Public method to access private attribute
    def get_balance(self):
        return self.__balance

    # Public method to modify private attribute safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

# Step 6: Create an Object of BankAccount class
account1 = BankAccount("123456789", 1000)
print(f"Current Balance: ${account1.get_balance()}")
account1.deposit(500)
