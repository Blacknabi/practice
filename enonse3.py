
nom=input("antre nom w svp")
n=nom.split()
name=[]
for a in n:
    a=a[0].upper()+a[1:]
    name.append(a)
print(name)