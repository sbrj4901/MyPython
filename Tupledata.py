# TUBLE DATA TYPES,DICTIONARY DATA TYPES,
# TUBLE
t=(1,2,3,4)
print(dir(t))
t1=(101,723.1,5,105)
print(min(t1))
print(max(t1))
print(len(t1))
t2=(5,6,7,8)
t3=(t1,t2)
print(t3)
#t1[0]=100
#print(t1)
# DICT
d={'name':'Rajesh','age':29}
print(dir(d))
print(len(d))
print(str(d))
print(d.keys())
print(d.items())
d1={'sanjay':103}
d.update(d1)
print(d)
d.pop('age')
print(d)
# SET METHODS
# difference
# intersection
# union
# symmetry
a={1,2,3,4}
b={1,2,3,4,5}
print(dir(a))
