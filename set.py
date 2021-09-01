# SET DATA TYPES
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
a=list(set(l1).union(l2))
print(a)
b=list(set(l1).intersection(l2))
print(b)
c=list(set(l1).difference(l2))
print(c)

l3={1,2,3,4,5}
l4={4,5,6,7,8}
d=set(l3).union(l4)
print(d)

l5={'f','g','h','i','j'}
l6={'i','j','k','l','m'}
e=set(l5).intersection(l6)
print(e)

l7=['a','b','c','d']
l8=['e','f']
f=set(l7).union(l8)
print(f)


