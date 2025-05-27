class Calculator:
    def __init__(self, num1: int, num2: int) -> None:
        self.num1 = num1
        self.num2 = num2

    def addition(self) -> None:  # Addition  (+)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1 + self.num2
        print(f"Addition results: {self.num1}+{self.num2}={result}")

    #                 ******************
    def subtraction(self) -> None:  # Subtacraction  (-)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1 - self.num2
        print(f"Subtraction results: {self.num1} - {self.num2} = {result}")

    #                  *****************
    def Multy(self) -> None:  # Multyplication   (*)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1 * self.num2
        print(f"Multiplication results: {self.num1} X {self.num2} = {result}")

    #                  *****************

    def division(self) -> None:  # Division  (/)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1 / self.num2
        print(f"division results: {self.num1} / {self.num2} = {result}")

    #                  *****************

    def Module(self) -> None:  # Module  (%)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1 % self.num2
        print(f"Module results: {self.num1} % {self.num2} = {result}")

    #                  *****************
    def floor_division(self) -> None:  # Floor Division  (//)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1 // self.num2
        print(f"Floor Division results: {self.num1} // {self.num2} = {result}")

    #                  *****************
    def exponentiation(self) -> None:  # Exponentiation  (**)
        self.num1 = int(input("Enter the first number please: "))
        self.num2 = int(input("Enter the second number please: "))

        result = self.num1**self.num2
        print(f"Exponentiation results: {self.num1} ** {self.num2} = {result}")
