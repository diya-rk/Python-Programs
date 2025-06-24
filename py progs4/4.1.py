d={
    'name':'Diya',
    'age' : 22,
    'mark': 29
    }
print(d)
print(d['mark'])
d['grade']='A'
d['mark']=45
print(d)
d.pop('age')
del d['mark']
print(d)

for key in d:
    print(key,":",d[key])