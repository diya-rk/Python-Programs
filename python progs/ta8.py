a=int(input("enter a number: "))
count=0
while a!=0:
    a//=10
    count+=1
print("the number of digits in is:",count)