price=int(input("Enter the Price: "))
def calculate_total(price, tax=5):
    return price + (price * tax / 100)
print("The total cost is: ",calculate_total(price))