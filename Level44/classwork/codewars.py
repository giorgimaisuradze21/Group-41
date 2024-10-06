def printBill(customer_name):
    print("------ Bill ------")
    print(customer_name)
    print("------------------")
    


def print_name(y):
   print(f"Welcome {y}")

print_name("Tommy")



def raviiyos(length, width):
    return length * width
length = 7
width = 4

result = raviiyos(length, width)
print(result)



def sum(x):
    res=0
    for i in range(x):
        res+=i
    return res

print(sum(4))