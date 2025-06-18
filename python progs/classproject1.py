print("WELCOME TO JOJO'S SHOPMART")
a=input("Enter your Name: ")
print(f"Hi {a}!! Have a great shopping experience!")
b=int(input("Enter the number of items to be purchased: "))
i=0
tot=0
for i in range(b):
    c=input("Enter the item name: ")
    d=int(input("Enter the price of item: "))

    
    tot=tot+d
print("Total Amount: ",tot)

if tot>=2000:
    print("You have a deduction of $100!!")
    addamt=lambda tot : tot-100
    total=addamt(tot)
    print("Total Amount to be Payed is: ",total)
else:
    print("Total Amount to be Payed is: ",tot)