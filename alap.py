import random
print("Betöltse az előző lekérdezést?\nIgen-->1\nNem-->2\n")
valasz= int(input("Választás: "))
napibevetel = 0

if(valasz == 1):
    with open("export.txt", 'r', encoding='utf-8') as beofile:
        for adat in beofile:
            adat.strip()
            napibevetel = int(adat)
            print(napibevetel)
    for i in range(3):
        sor = 1
        while sor <= 10:
            oszlop = 1
            while oszlop <=10:
                randomszam = random.randint(0, 1)
                print(randomszam, end=" ")
                if(randomszam == 1):
                    napibevetel += 2500
                oszlop=oszlop+1
            print("")
            sor= sor+1
    print("-------------------------------")
    print(f"Az előző és aznapi bevétel összesen:{napibevetel}Ft")
elif(valasz == 2):
    for i in range(3):
        sor = 1
        while sor <= 10:
            oszlop = 1
            while oszlop <=10:
                randomszam = random.randint(0, 1)
                print(randomszam, end=" ")
                if(randomszam == 1):
                    napibevetel += 2500
                oszlop=oszlop+1
            print("")
            sor= sor+1
    print("-------------------------------")
    print(f"Napi bevétel:{napibevetel}Ft")
        
          


"""
#Mentés
for i in range(3):
    sor = 1
    while sor <= 10:
        oszlop = 1
        while oszlop <=10:
            randomszam = random.randint(0, 1)
            print(randomszam, end=" ")
            if(randomszam == 1):
                napibevetel += 2500
            oszlop=oszlop+1
        print("")
        sor= sor+1
    print("-------------------------------")


print(f"Napi bevétel:{napibevetel}Ft")
"""  

