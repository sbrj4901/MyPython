# Day11
import json
with open("ex.json","r") as b:
	data=json.load(b)
with open("ex1.json","w") as f:
	json.dump(data,f)


	


