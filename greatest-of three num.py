#WAP to find greath f three number
num1=int(input("enter the value if num1 :"))
num2=int(input("enter the value if num2 :"))
num3=int(input("enter the value if num3 :"))


if(num1==num2==num3):
    print("all are equal")


if(num1>num2 and num1>num3):
    print("num1 is greather" )

if(num2>num3 and num2>num1):
    print("num2 is greather")
elif(num3>num1 and num3>num2):
    print("num3 is greather")