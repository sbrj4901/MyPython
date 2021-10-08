# if and elif
a = 35
b = 36
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else condition
a = 255
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# if statements inside if statements
x = 40

if x > 13:
  print("Above ten,")
  if x > 22:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if not expression
string_1 = ''

if not string_1:
    print('String is empty.')
else:
    print(string_1)

