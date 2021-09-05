#Day9
#functions and arguments
l1 = ('hello')
l2 = ('world')
def diff(a,b):
	print(a.upper(), b.upper())
diff (l1, l2)


def do (*args):
	print(args)
do(10,20,30,40)

def do (**wargs):
	print(wargs)
do()

