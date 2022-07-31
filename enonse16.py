from ntpath import join
import random
def mo_kache():
    
    chenn=list('abcdefghijklmnopqrstuvwxyz')
    let = ">3a >0a <1u <10k >1a <9j <0s <16u"  
    kache=let.split(" ")
    for i in kache:
        if i[0] ==">":
            b = chenn.index(i[-1]) + int(i[1:-1])
        else:
            b = chenn.index(i[-1]) - int(i[1:-1])
        
        print(chenn[b],end="")
        
mo_kache()