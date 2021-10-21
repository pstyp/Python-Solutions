num = int(input("Give me a number! "))

if not num % 4:
    print(f"{num} is divisible by 4!")

elif not num % 2: 
    print(f"{num} is an even number!")
    
else:
    print(f"{num} is an odd number!")

## STRECH GOAL
num2 = int(input("Give me a number! "))
check = int(input("Give me another number! "))

if num2 % check: 
    print(f"{num2} is not divisible by {check}!")
    
else:
    print(f"{num2} is divisible by {check}!")