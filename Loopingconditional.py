# LOOPING CONDITIONAL
l=[10,20,30,40,50]
l1=l.count(20)
	
if l1 > 1:
		print('match found')
else:
	print('match not found')
l1=[10,20,30]
l2=[2]
for a in l1:
	l2.append(a)
print(l2)

l3=[1,2,3,4,5,6,4,5,6,7,8,9]
for i in l3:
	if l3.count(i)>1:
		l3.remove(i)
print(l3)

L=[5,20,30,40,50,20,30,40,50]
d=list(set(L))
print(d)
	
l5=[1,2,3,4,5,2,3,4,6,7,8]
l6=[]
for a in l5:
	if a  not in l6:
		l6.append(a)
for a in l6:
	print(a)








