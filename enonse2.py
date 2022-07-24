n=input("Entrer valeur n")
while not n.isdigit():
    n=input("Entrer valeur n")
n=int(n)
if n%4==0:
    print("NOK")
else:
    print("OK")



