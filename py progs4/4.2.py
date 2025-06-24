d={
    'name':'Diya',
    'age' : 22,
    'mark': 29
    }
print(d)

#get a single value of key
print(d.get('name'))
#print the keys
print(d.keys())
#print the values 
print(d.values())
#print the dictionary as key value
print(d.items())
d.popitem()
d.update({'email':'kusum@engf.com'})
print(d)
d.clear()
print(d)