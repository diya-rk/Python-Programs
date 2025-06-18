def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
g=input("Enter the String: ")
print(reverse_string(g))