n=10
i=1
for i in range(n):
    a =input("entre valeur a ")
    while not a.isdigit():
        a =input("entre valeur a ")
    b=input("entre valeur b ")
    while not b.isdigit():
        b =input("entre valeur b ")
    a=int(a)
    b=int(b) 
    
    if a>b:
        f=a/b
        f=f/2
        f=round(f)
        print(f)
    elif b>a:
        f=b/a
        f=f/2
        f=round(f)
        print(f)
    else:
        f=b/a
        f=f/2
        print(f)
        
exit
