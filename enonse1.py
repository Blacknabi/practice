
import ipaddress


def adressIP():
    while True:
        try:
            adress=input("antre adres ip a")
            print(ipaddress.ip_address(adress))
            port=adress.replace(".","")
            print(int(port))
            p=0
            for i in port:
                p+=int(i)*int(port[0])
                
            print(f"port ki ouvri a se {p}")
            break
            
        except:
            print("adress ip a pa bon, antre vale a anko")
            adressIP()
    
adressIP()
