# Challenge #1
# Print 3 different strings


print("string 1")
print("string 2")
print("string 3")


# Challenge #2
# Print a message if a variable is < 10 and a different message if the variable is >= 10.

x = 80

if x < 10:
    print("x is less than 10.")
else:
    print("x is either 10 or more!")


# Challenge #3
# Print a message if a variable is less than or equal to 10, another message if the variable
# is > 10 but <= 25, and another message if the variable is > 25.

x = 17

if x <= 10:
    print("x is a low number.")
if x <= 25:
    print("x is definitely greater than 10!")
else:
    print("I think x is a large number.")

# Challenge #4
# Divide 2 variables and print the remainder

x = 10
y = 4

print(x % y)


# Challenge #5
# Divide 2 variables and print the quotient

print(x // y)


# Challenge #6
# Using a variable defined as 'age', assign an integer to 'age' and print different strings depending on the integer
# given to age.

age = 51

if age < 35:
    print("you are younger than 35.")
if age >= 35:
    if age <= 50:
        print("you are between 35 and 50 years old.")
    else:
        print("you are older than 50.")
