"""
THIS PROGRAM FILE TAKES TWO INPUTS I.E NAME OF A USER < AGE , AND RETURNS A STRING
THAT OUTPUTS THE BIRTHYEAR
"""
def calc_birth_year(name,age):
    from datetime import datetime
    current_year = datetime.today().year
    birthyear = current_year - age
    return f"hello {name}, your birthyear is {birthyear}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
result = calc_birth_year(user_name,user_age)
print(result)













