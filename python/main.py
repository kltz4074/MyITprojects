import random

rdn = random.randint(5000000, 10000000000000000)
print(rdn)
inputi = input(">>")

if int(inputi) == rdn:
    print("sigma")
else:
    print("no")