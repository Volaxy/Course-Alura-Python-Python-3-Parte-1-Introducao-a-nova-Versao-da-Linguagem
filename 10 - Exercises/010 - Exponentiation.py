number = int(input("Write a number: "))

n1 = int("%s" % number)
n2 = int("%s%s" % (number, number))
n3 = int("%s%s%s" % (number, number, number))

print(n1 + n2 + n3)
