token="web-insecure;34829sjdfnsj32984madsdkj"
print(token)
print()
tok=list(token)
for i in tok:
    if ";" in i:
        j=tok.index(i)
        j=int(j)
        del tok[:j]
        tok.remove(";")
        stra="".join(tok)
        print(f"token final la se {stra}")
        
        
       