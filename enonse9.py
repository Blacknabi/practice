a=input("Enter the first interval: ")
while not a.isdigit():
    a=input("Enter the first interval: ")
b=input("Enter the second interval: ")
while not b.isdigit():
    b=input("Enter the second interval: ")
a=int(a)
b=int(b)
for i in range(a,b):
    i=int(i)
    if i%2==0:
        print(i,end=" ")