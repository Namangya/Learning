# 13th July 2026 - 14th July 2026 - Working with Data and Manipulate Strings

# Specific Character of the String
print("Day 2"[2])
print("Day 2"[-1])

print(123+456)

# To make large number readable we use underscore in it.
print(12_34_56_789)

# String, Byte, Tuple, List, Range, Collection, Set, Frozen Set

# To Know the datatype of the given value
print(type("What"))
print(type(12345))
print(type(123.45))
print(type(False))

# Casting DataTypes
print("1" + "2")
print(int("1")+int("2"))
int(), str(), bool(), float()

# print("Number of Letter in your Name: " + str(len(input("What is your Name\n"))))

# Mathematical Operation (P.E.M.D.A.S)

print(123 + 3.45)
print(2 - 1)
print(3 * 5)
print(12 / 2)
print(12 // 2)
print(2 ** 3)

#Thonny to Debug Python Code
print(325+37+656+125+2000+35+28+160+200+105)

print(round(3.45678))
print(round(3.75678))
print(round(3.45678,3))

score=0
test=0

score = score + 1
test +=1

print("Test = ",test," Score = ",score)

score=23
height=2.3
really=True

# F String with which we can use all Data type in the string
print(f"Your Score is = {score}, with height = {height}. Is it really {really}")

print("Welcome to Tip Calculator\n")
total_bill=float(input("What was the total bill? "))
tip_amount=float(input("How much tip would you like to give ? 10, 15, or 20 or any amount? "))
people_split=float(input("How many people to split the bill? "))
each_person= round(((total_bill + tip_amount) / people_split ),2)
print("Each person should pay:",str(each_person))

print("Welcome to Tip Calculator\n")
total_bill=float(input("What was the total bill? "))
tip_percentage=float(input("How much tip would you like to give ? 10, 15, or 20 or any percent? "))
tip_amount=float((total_bill * tip_percentage) / 100)
people_split=float(input("How many people to split the bill? "))
each_person= round(((total_bill + tip_amount) / people_split ),2)
print("Each person should pay:",str(each_person))
print(f"Each person should pay: {each_person}")


# End of Day 2