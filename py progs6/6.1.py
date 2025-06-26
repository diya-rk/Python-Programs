a={1,2,3,4}
b={3,4,5,6,7,8}
c={1,2,3}
#union
print(a.union(b))
#intersection
print(a.intersection(b))
#difference 
print(a.difference(b))#a-b
print(b.difference(a))#b-a
#symmetric difference
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(30 in a)
print(c.issubset(a))
print(a.issuperset(c))

#frozen set
fs=frozenset([1,2,3,4])
print(fs)
print(type(fs))
