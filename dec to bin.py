# // Int division
# Decimal to Binary system

dec = int(input("Please enter a number: "))
n = 0
b = []
if dec == 0:
    print("Number is 0")
if dec < 0:
    print("Number is negative")
if dec > 0:
    while dec != 0:
        dec //= 2
        n = (dec % 2)
        b.append(n)
    print("Number is: ", b[::-1])
        
