import Mozi as Moziimp
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
        Moziimp.MaiMozi(teremdb,napibevetel)
    elif(valasz2 == "Nem"):
        Moziimp.MaiMozi(teremdb,napibevetel)
for i in Szuro:
    if(valasznap == i):
        Moziimp.NapMozi(teremdb,napibevetel,valasznap) 

