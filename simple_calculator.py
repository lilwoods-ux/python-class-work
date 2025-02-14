myName = input("Enter your name: ")
print("welcome to the concole calculator")
# let the user pick operation to work on
while True:
     print("\nAvailable Operations:")
     print("1. Addition(+):")
     print("2. Subtraction(-):")
     print("3. Multiplication(*):")
     print("4. Division(/):")
     print("5. Modulus(%):")
     print("6. Exit")

     # variable to collect user choice
     my_choice = input("Enter your operation: 1-6 ")
     # prompt them for the numbers to be used
     num1 = float(input("Enter your first number: "))
     num2 = float(input("Enter your second number: "))
     #if the user selects to exit the calculator then we kill the program
     if my_choice == "6":
         print("Thank You for using my app:")
         break
     elif my_choice == "1":
          print("Adding numbers:")
          result = num1 + num2
          print(f"{num1} + {num2} = {result}")
     elif my_choice == "2":
          print('Substracting numbers:')
          result = num1 - num2
          print(f"{num1} - {num2} = {result}")
     elif my_choice == "3":
          print('Multiplying numbers:')
          result = num1 * num2
          print(f"{num1} * {num2} = {result}")
     elif my_choice == "4":
          print('Dividing numbers:')
          result = num1 / num2
          print(f"{num1} / {num2} = {result}")
     elif my_choice == "5":
          print('Modulus:')
          result = num1 % num2
          print(f"{num1} % {num2} = {result}")


     else:
         print(f"{myName}  This is not a valid choice.")