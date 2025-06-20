#Access the first and last characters of the string
name="My name is goofy"
print(name[0])
print(name[-1])

#Slice the string from index 1 to 4
d="kilimanjaro"
print(d[1:5])

#Count how many times a letter appears in a string
l = "banana"
print(l.count("a"))

#Find the index of a specific character
print(l.index("n"))

#Split a sentence into words
k="have a nice day"
print(k.split())#its made into a list

#Join a list of words into a sentence
words = ["I", "love", "Python"]
print(" ".join(words))

#Check if the string starts with a specific word
lol="hey there how are you?"
print(lol.startswith("hey"))

#Compare two strings for equality
str1 = "hello"
str2 = "Hello"
print(str1 == str2)

#Check if a string is a palindrome
s = "malayalam"
print(s == s[::-1])

#Count the number of vowels in a string.
s = "education"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print(count)

#Take a user input string and print it in title case.
str = input("Enter a string: ")
print(str.title())

#Write a program to remove all spaces from a string.
s = "the spaces in between the words are to be removed"
print(s.replace(" ", ""))