a=input("entrer tout nombre yo: ")
a=a.split()
print(a)
max=a[0]
min=a[0]

for i in a:
    if i>max:
        max=i
    else:
        max=max
    if i<min:
        min=i
    else:
        min=min
print(min)
print(max)
