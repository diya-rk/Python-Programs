print("~~GUESS THE SECRET NUMBER~~")
a=int(input("Enter the number you have guessed: "))
if a==7:
    print("you guessed it right!!! its 7!!!")
else:
    b = input("Nope thats a wrong guess .Please enter another number: ")
    for b in a:
        if b==7:
            print("you guessed it right!!! its 7!!!")
        else:
            print("your chances over...")
    