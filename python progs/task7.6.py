a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
c=int(input("Choose from the above operations: 1/2/3/4: "))
if c==1 :
    print("the result after addition is:",a+b)
elif c==2 :
    print("the result after subtraction is:",a-b)
elif c==3 :
    print("the result after multiplication is:",a*b)
elif c==4 :
    print("the result after division is:",a/b)
else :
    print("invalid choice!!!")