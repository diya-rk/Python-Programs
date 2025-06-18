list=[5,6,7.5,"apple","mango",True,[0,1,2]]
print(list)
#add item at end
list.append(100)
print(list)
#add item at any position
list.insert(3,"orange")
print(list)
#replace an element
list[4]="avocado"
print(list)
#remove a specific element 
list.remove(5) #remove() is a built in function
print(list)
#remove element at the end of list
list.pop()
print(list)
#print all elements one by one 
#for item in list:
    #print(item)
#to clear all elements from list 
list.clear
print(list)