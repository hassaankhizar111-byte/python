first = input("First name: hassaan ")
last = input("Last name: shariq ")
username = first.lower() + "_" + last.lower()
print("Generated username:", username)

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")

age = input("Enter your age: ")
next_month_age = int(age) + 1
sentence = "Next month, you will be " + str(next_month_age) + " years old."
print(sentence)

name = input("Enter your name:\n ")
print(name + ' you are the best')

name = input("Enter your name: ")
city = input("Enter your city: ")
print(name + " you are invited in our company for a visit, in " + city)

name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
skill = input("Enter your skill: ")
favourite_car = input("Enter your favourite_car: ")
print("My name is " + name + " I am " + age + ''' years old with big dreams, I am working hard 
daily on my goals I am learning a very valuable skill ''' + skill + " I live in " + country + ''' 
My goal is to earn from development, cloud computing, and a bbusiness I have decided to build and 
I want buy my dream car ''' + favourite_car + ''' and every thing I dreamed of, I really wanted 
to make make my parents proud.''' )


def calc_sum(a, b):    # def function
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)
calc_sum(20, 30)
calc_sum(100, 200)
calc_sum(7, 3)
