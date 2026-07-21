# 14th July 2026 - 15th July 2026 - Control Flow and Logical Operators

# If Condition
#     Do This
# else
#     Do This

# In Python Spacing and Identation is Really Important

print("Welcome to the If Else Nested Even Odd Divisibility Game")

number = int(input("Write the number: "))

if number % 2 == 0:
    if number % 5 == 0:
        print(f"Number {number} is Even and Divisible by 5")
    else:
        print(f"Number {number} is Even and Not Divisible by 5")
else:
    if number % 5 == 0:
        print(f"Number {number} is Odd and Divisible by 5")
    else:
        print(f"Number {number} is Odd and Not Divisible by 5")


print("Welcome to the If Elif Else Even Odd Divisibility Game")

number = int(input("Write the number: "))

if number % 2 == 0 and number % 5 == 0:
    print(f"Number {number} is Even and Divisible by 5")
elif number % 2 == 0:
    print(f"Number {number} is Even and Not Divisible by 5")
elif number % 5 == 0:
    print(f"Number {number} is Odd and Divisible by 5")
else:
    print(f"Number {number} is Odd and Not Divisible by 5")
