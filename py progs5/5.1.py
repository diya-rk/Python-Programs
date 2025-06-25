#extracting characters from string
text="Programming"
print(text[0])
print(text[-1])
#reverese of a string
p="the great wall of china"
reverse=p[: : -1]
print(reverse)
# Count occurrences of a specific character
l="weclome to ooty"
print(l.count("o"))
#Replace spaces with underscores 
a = "Python is fun to learn"
print(a)
print(a.replace(" ", "_"))
#Check if a string is a palindrome
k=input("Enter the word: ")
if k==k[::-1]:
    print("yes the word is palindrome!!")
else:
    print("the word you have entered is not a palindrome")