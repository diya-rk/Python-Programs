#only intergers in the tuple
t1=(1,3,5,2,4,5,3)
print(sum(t1))
print(max(t1))
print(min(t1))
print(sorted(t1))

l1=list(t1)
print(type(l1))
print(l1)
l1.append(100)
print(l1)
t2=tuple(l1)
print(t2)