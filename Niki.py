#Készítette: Koch Nikolett
#Osztály: 1/13SZFT
#Dátum: 2022.12.05

#Alap feladat 02: Napi bevétel lekérdezése, foglalás után kiiratni a fájlba, előző állapot betöltése(olvasás) vagy üres fájl (írás), függvényekben és eljárásokban
def niki():
    
    h = 0
    k = 0
    print("Hétfő, Kedd, Szerda, Csütörtök, Péntek, Szombat, Vasárnap")
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
        print(f"{K} Forint a keddi nap bevétele.")
    elif(napvalaszto=="Szerda"):
        with open("szerda.txt","r",encoding="utf-8") as Sz:
            for elem in Sz:
                for i in elem:
                    if(i == "1"):
                        Sz += 2000
        print(f"{Sz} Forint a szerdai nap bevétele.")
    elif(napvalaszto=="Csütörtök" or napvalaszto=="Csutortok"):
        with open("csutortok.txt","r",encoding="utf-8") as Cs:
            for elem in Cs:
                for i in elem:
                    if(i == "1"):
                        H += 2000
        print(f"{H} Forint a csütörtöki nap bevétele.")
    elif(napvalaszto=="Péntek" or napvalaszto=="Pentek"):
        with open("pentek.txt","r",encoding="utf-8") as P:
            for elem in P:
                for i in elem:
                    if(i == "1"):
                        P += 2000
        print(f"{P} Forint a pénteki nap bevétele.")
    elif(napvalaszto=="Szombat"):
        with open("szombat.txt","r",encoding="utf-8") as Szo:
            for elem in Szo:
                for i in elem:
                    if(i == "1"):
                        Szo += 2000
        print(f"{Szo} Forint a szombati nap bevétele.")
    elif(napvalaszto=="Vasárnap" or napvalaszto=="Vasarnap"):
        with open("csutortok.txt","r",encoding="utf-8") as V:
            for elem in V:
                for i in elem:
                    if(i == "1"):
                        V += 2000
<<<<<<< HEAD
                print(f"{V} Forint a szombati nap bevétele.")
                
            else:
                print("Nincs ilyen nap.")
niki()
>>>>>>> c747616a5fd173cf17a89f37a9935bf478de31cb
=======
        print(f"{V} Forint a szombati nap bevétele.")          
    else:
        print("Nincs ilyen nap.")
niki()
>>>>>>> 2634aca (nikivalt)
