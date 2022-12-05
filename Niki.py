#Készítette: Koch Nikolett
#osztály: 1/13SZFT
#Dátum: 2022.12.05



def niki():
    h=0
    k=0
    sz=0
    cs=0
    p=0
    szo=0
    v=0
    
    napvalaszto=input(("Kérlek add meg melyik napi bevételt szeretnéd lekérdezni (Hétfő- Vasárnap):")).capitalize()
    if(napvalaszto=="Hétfő" or napvalaszto=="Hetfo"):
        with open("hetfo.txt","r",encoding="utf-8") as H:
            for elem in H:
                for i in elem:
                    if(i == "1"):
                        h += 2000
        print(f"{h} Forint a hétfői nap bevétele.")
    elif(napvalaszto=="Kedd"):
        with open("kedd.txt","r",encoding="utf-8") as K:
            for elem in K:
                for i in elem:
                    if(i == "1"):
                        k += 2000
        print(f"{k} Forint a keddi nap bevétele.")
    elif(napvalaszto=="Szerda"):
        with open("szerda.txt","r",encoding="utf-8") as Sz:
            for elem in Sz:
                for i in elem:
                    if(i == "1"):
                        sz += 2000
        print(f"{sz} Forint a szerdai nap bevétele.")
    elif(napvalaszto=="Csütörtök" or napvalaszto=="Csutortok"):
        with open("csutortok.txt","r",encoding="utf-8") as Cs:
            for elem in Cs:
                for i in elem:
                    if(i == "1"):
                        cs += 2000
        print(f"{cs} Forint a csütörtöki nap bevétele.")
    elif(napvalaszto=="Péntek" or napvalaszto=="Pentek"):
        with open("pentek.txt","r",encoding="utf-8") as P:
            for elem in P:
                for i in elem:
                    if(i == "1"):
                        P += 2000
        print(f"{p} Forint a pénteki nap bevétele.")
    elif(napvalaszto=="Szombat"):
        with open("szombat.txt","r",encoding="utf-8") as Szo:
            for elem in Szo:
                for i in elem:
                    if(i == "1"):
                        szo += 2000
        print(f"{szo} Forint a szombati nap bevétele.")
    elif(napvalaszto=="Vasárnap" or napvalaszto=="Vasarnap"):
        with open("csutortok.txt","r",encoding="utf-8") as V:
            for elem in V:
                for i in elem:
                    if(i == "1"):
                        v += 2000
                print(f"{v} Forint a szombati nap bevétele.")
                
            else:
                print("Nincs ilyen nap.")
niki()