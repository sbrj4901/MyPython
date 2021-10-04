# use break after print statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# use break before print statement
fruits = ["apple",'banana','cherry']
for x in fruits:
	if x == 'banana':
	 break
	print(x)

# use continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
     continue
    print(x)