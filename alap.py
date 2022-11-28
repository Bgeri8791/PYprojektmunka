import random 
def NapMozi(teremdb,napibevetel):
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



#Alap változók.
napibevetel = 0
teremdb=1
Szuro=["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]



#Melyik napot tölse be?
print("Kérlek adj meg a hét napjaiból egyet.\nHa csak a mai napot szeretnéd írd be, hogy 'Ma'")
valasznap= input("Választott nap: ").capitalize()


if(valasznap =="Ma"):
    print("Betöltse az előző lekérdezést?\n")
    valasz2= input("Betöltse? (Igen vagy nem): ").capitalize()
    print("")
    if(valasz2 == "Igen"):
        with open("export.txt", 'r', encoding='utf-8') as beofile:
            for adat in beofile:
                adatok = adat.strip().split(" ")
                napibevetel = int(adatok[4])                        
        print(f"Az előző napi bevétel:{napibevetel}") 
        MaiMozi(teremdb,napibevetel)
    elif(valasz2 == "Nem"):
        MaiMozi(teremdb,napibevetel)
for i in Szuro:
    if(valasznap == i):
        NapMozi(teremdb,napibevetel) 

