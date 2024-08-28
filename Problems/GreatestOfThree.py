num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))
num3 = int(input("Enter a 3rd number: "))

if(num1>num2):
    if(num1>num3):
        print(num1," is greater")
    else:
        print(num3,"is greater")
else:
    if(num2>num3):
        print(num2," is greater")
    else:
        print(num3,"is greater")