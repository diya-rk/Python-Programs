s1=" Hello python "
print(s1)
print(type(s1))
print(len(s1))
print(s1[-4])
#slice
print(s1[0:5])
print(s1[6:])
#string reverse using slice
print(s1[::-1])
#for loop 
for i in s1:
    print(i)
#membership optr
print('y' in s1)
#case
print(s1.lower())
print(s1.upper())
print(s1.split(','))
print(s1.strip())

#newline 
print("wow\nits\npython")
#tab space
print("wow\tits\tpython")

print("Hello\\hey")
print('it\'s mine')

#string formatting
name='hattori'
age='15'
print("My name is ",name," and my age is ", age)
#or
print(f"My name is {name} and my age is {age}")

#no.of times
print("HI YAO \n"*3)

#string comparison
print("apple" == "Apple")

print('a'<'b')

#equality and identity
a='hi' 
b='hi'
print(a==b)
print(a is b)

#type conversion
l = list(s1)
print(l)

s3="jojosiva123"
print(s3.isalpha())
print(s3.isdigit())
print(s3.isalnum())