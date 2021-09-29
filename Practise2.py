# 1.loop methods
import time
data=["policy/azure/compliance/xyoz",
"policy/aws/compliance/axzd",
"policy/gcp/compliance/xmcy",
"policy/azure/compliance/abcd",
"policy/aws/compliance/mcrd",
"policy/gcp/compliance/xazd"]

def validURI(uri, key):
	start = time.time()
	matches = []
	for match in uri:
		if key in match:
			matches.append(match)
	end = time.time()		
	return matches
a = validURI(data,'azure')
print(a)