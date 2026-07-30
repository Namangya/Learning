# 14th July 2026 - 15th July 2026 - Control Flow and Logical Operators

# If Condition
#     Do This
# else
#     Do This

# In Python Spacing and Identation is Really Important

print("Welcome to the Even Odd Divisibility Game")

number = int(input("Write the number: "))

if number % 2 == 0 and number % 5 == 0:
    print(f"Number {number} is Even and Divisible by 5")
elif number % 2 == 0:
    print(f"Number {number} is Even and Not Divisible by 5")
elif number % 5 == 0:
    print(f"Number {number} is Odd and Divisible by 5")
else:
    print(f"Number {number} is Odd and Not Divisible by 5")


print("Welome to Python Pizza Deliveries")

size=input("What size pizza you want S, M, L: ")
want_pepperoni= input(f"You want Pepperoni in your {size} Pizza? Y or N: ")
extra_cheese= input(f"You want Extra Cheese in your {size} Pizza? Y or N: ")

bill=0

if size == 'S':
    bill=15
    if want_pepperoni == 'Y':
      bill = bill + 2
    
    if extra_cheese == 'Y':
        bill += 1
        
    print(f"Your Final Bill is ${bill}")

elif size == 'M':
    bill=20
    if want_pepperoni == 'Y':
      bill = bill + 2
    
    if extra_cheese == 'Y':
        bill += 1

    print(f"Your Final Bill is ${bill}")
elif size == 'L':
    bill=25
    if want_pepperoni == 'Y':
      bill = bill + 3
    
    if extra_cheese == 'Y':
        bill += 1
        
    print(f"Your Final Bill is ${bill}")

else:
    print("Invalid Input. Please Select from S, M, L")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("You're at the cross road. Where do you want to go")
command=input("    Type ""left"" or ""right"": ")

if command == 'left':
  print("You've come to a lake. There is an island in the middle to lake")
  command=input("    Type ""wait"" to wait for boat. Type ""swim"" to swim across: ")

  if command == 'wait':
    print("You arrive at the island unharmed. There is a house with 3 doors")
    command=input("One Red, One Blue, One Yellow. Which colour do you choose : ")

    if command == 'Yellow':
       command=input("You Win!")

    elif command == 'Red':
       print("Burned by fire. Game Over.")
    
    elif command == 'Blue':
       print("Eaten by beasts. Game Over.")

    else:
       print("Game Over")

  else:
   print("Attacked by trout. Game Over.")

else:
  print("Fall into a hole. Game Over.")