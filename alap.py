import random

def Mozi(teremdb,napibevetel):
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
                rszam = random.randint(0, 1)
                print(rszam, end="")
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

#Menü rendszer 01:   
#Az előző napi bevételt betöltse-e?
print("Betöltse az előző lekérdezést?\nIgen-->1\nNem-->2\n")
valasz= int(input("Választás: "))
print("")


#Alap változók.
napibevetel = 0
teremdb=1

#Menü rendszer 02: 
#1-> szeretném az előző export.txt file betölteni. 
#2-> Nem szeretném az előző export.txt file betölteni.
if(valasz == 1):
    with open("export.txt", 'r', encoding='utf-8') as beofile:
        for adat in beofile:
            adatok = adat.strip().split(" ")
            #szoveg=int(adatok[4])
            napibevetel = int(adatok[4])
            print(f"Az előző napi bevétel:{napibevetel}")
    Mozi(teremdb,napibevetel)
elif(valasz == 2):
    Mozi(teremdb,napibevetel)


"""
#Random 0-1 között írja ki a számokat 10x10-es oszlop és sorban.
for i in range(3):
        print(f"Terem_{teremdb}")
        teremdb+=1
        sor = 1
        while sor <= 10:
            oszlop = 1
            while oszlop <=10:
                rszam = random.randint(0, 1)
                print(rszam, end=" ")
                if(rszam == 1):
                    napibevetel += 2500
                oszlop=oszlop+1
            print("")
            sor= sor+1
        print("-------------------------------")


print(f"Napi bevétel:{napibevetel}Ft")
"""

