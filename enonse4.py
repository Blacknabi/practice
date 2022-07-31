a=input("entrer la valeur de a: ")
while not a.isdigit() :
    a=input("entrer la valeur de a: ")
b=input("entrer la valeur de b: ")
while not b.isdigit() :
    b=input("entrer la valeur de b: ")
    
a=int(a)
b=int(b)
liste=[]
liste2=[]
liste3=[]
liste4=[]
for n in range(1,20):
    
    if n%a==0 and n%b!=0:
        print(f"{n} se multiple a ")
        liste.append(n)
        
    elif n%b==0 and n%a!=0 :
        liste2.append(n)

    if n%a==0 and n%b==0:
        liste3.append(n)

    elif n%a!=0 and n%b!=0:
        liste4.append(n)

print(liste)
print("total element ki multiple a se", len(liste))
print(liste2)
print("total element ki multiple b se", len(liste2))
print(liste3)
print("total element ki multiple a et b se", len(liste3))
print(liste4)
print("total element ki pa multiple ni a ni b se", len(liste4))
