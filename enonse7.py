a=input("entrer phrase ou a: ")
while a.isdigit():
    a=input("pa entre chiffre, entrer phrase ou a: ")
liste=["a","e","i","o","u","y"]
liste2=["b","c","d","f","g","h","j","k","l","m","n","p","k","r","s","t","v","w","x","z"," "]
for i in a:
    for j in liste:
        for k in liste2:
            while k in a:
                a=a.replace(k,"*")
                break
print(f" {a} se phrase finale")