#list comprehension 
n=[x for x in range(1,6)]
print(n)
#square value
s=[x*x for x in range (1,6)]
print(s)
#even no.s in given range
e=[x for x in range(1,21) if x%2 == 0]
print(e)
#odd no.s 
o=[x for x in range(1,21) if x%2 != 0]
print(o)