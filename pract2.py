# for condtion in single line code
data = ["Policy/azure/compliance/xyoz", "Policy/aws/compliance/axzd",
 		"Policy/gcp/compliance/xmcy", "Policy/azure/compliance/ahck",
 		"Policy/aws/compliance/mcrd", "Policy/gcp/compliance/xazd"]
def check(l, k):   
	l2 = [v for v in l if k in v]  
	return l2
a = check(data, "gcp")   
print(a)