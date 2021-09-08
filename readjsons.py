import json
with open("file.json","r") as json_file:
 	data=json.load(json_file)
print(data)
# b = data.get("Aggregate")
# print(b)
# for i in b:
#     if i!="English":
#         print("The key is missing")
#         break
#     elif i== "English":
#         print("The block contains English only")

for i in range(1,11):
	print(i)
