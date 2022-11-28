import random 
def NapMozi(teremdb,napibevetel,valasznap):
    for i in range(3):
        #Itt írja ki a hányas terem aztán nőveli 1-el. Csak 3-ig megy el.
        print(f"Terem_{teremdb}")
        teremdb+=1
        #Random 0-1 között írja ki a számokat 10x10 oszlop és sorban.
        #Ha 1-es akkor azon a széken van foglalás.
        #Ha 2-es akkor szabad a szék.
        sor = 1
        while sor <= 10:
            oszlop = 1
            while oszlop <=10:
                rszam = random.randint(0,1)
                print(rszam, end=" ")
                if(rszam == 1): # Ha 1-es a random szám akkor a napibevételhez adjon 2000Ft-ot. (Ha 0 akkor nem csinál semmit.)
                    napibevetel += 2000
                oszlop=oszlop+1
            print("")
            sor= sor+1
        print("-------------------------------") #Elválasztó sor.
    print(f"A {valasznap}-i bevétel: {napibevetel} Ft\n") 
    with open("napiexport.txt","w",encoding="utf-8") as kiirexport:
        kiirexport.write(f"A {valasznap}-i bevétel: {napibevetel} Ft\n")
def MaiMozi(teremdb,napibevetel):
    for i in range(3):
        #Itt írja ki a hányas terem aztán nőveli 1-el. Csak 3-ig megy el.
        print(f"Terem_{teremdb}")
        teremdb+=1
        #Random 0-1 között írja ki a számokat 10x10 oszlop és sorban.
        #Ha 1-es akkor azon a széken van foglalás.
        #Ha 2-es akkor szabad a szék.
        sor = 1
        while sor <= 10:
            oszlop = 1
            while oszlop <=10:
                rszam = random.randint(0,1)
                print(rszam, end=" ")
                if(rszam == 1): # Ha 1-es a random szám akkor a napibevételhez adjon 2000Ft-ot. (Ha 0 akkor nem csinál semmit.)
                    napibevetel += 2000
                oszlop=oszlop+1
            print("")
            sor= sor+1
        print("-------------------------------") #Elválasztó sor.
    print(f"A mai napi bevétel: {napibevetel} Ft\n") #Ki irja a napibevételt.
    with open("export.txt","w",encoding="utf-8") as kiirexport: #Ki iratja file-ba a napibevételt.
#Kérlek ne változtassatok a kiiratáson.
#Úgyan van kiszámolva hogy az összeg hányadik helyen van.
        kiirexport.write(f"A mai napi bevétel: {napibevetel} Ft\n")
