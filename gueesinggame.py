import random
choice=1
while choice<7:
	user=int(input("Enter number"))
	r=random.randrange (1,21)
if user =="r":
		print("your entered number is correct")
		break
elif user!=r:
		choice +=1
		print("Invalid")
