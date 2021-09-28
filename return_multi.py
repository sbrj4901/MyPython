#Returning Multiple Values using Tuples
def multiple():
    operation = "Sum" 
    total = 5+10
    return operation, total;

operation, total = multiple()

print(operation, total)