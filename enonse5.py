n=input("antre nombre lan separe par yon espas")
liste=[]
for i in n.split():
    a=sum(int(j) for j in i)
    liste.append(a)
print(liste)
p=1
for k in liste:
    p*=k
print(p)
    