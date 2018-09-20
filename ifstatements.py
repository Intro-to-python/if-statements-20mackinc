#if statements
#age = 16
age = input("What is your age?:")
if age >= 16:
    print("you can drive a car!")
#a condution is a programming statement that compares things and tells us if something is true or false: this is called a boolean
#! means not (like not true)
#elif age < 16:
    #print("you can drive soon!")
else:
    print("you can drive someday!")

if age > 16:
    print("you can drive")
elif age < 16:
    print("you cant drive yet")
elif age == 16:
    print("good luck on your drivers test")
else:
    print("not sure")
