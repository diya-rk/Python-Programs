#combining lists
numb1 = [21,24,26]
numb2=[23,25,27]
zipped=zip(numb1,numb2)
print(dict(zipped))
x=0
y=0
res = [(x + y) for x, y in zip(numb1 , numb2)]
print(str(res))