i=0
n=4
nonb=[0,1,2,3,4]
liste=[]
for i in range(n):
    a=nonb[::-1]
    print(a)
    liste.append(a[-1])
    del a[-1]
    
    nonb=a
    print(nonb)
    if i==3:
        for j in nonb:
            liste.append(j)
    
   
print(liste)
m=liste[::-1]
print(m)
print(f"men index element 3: {m.index(3)}")
