import random
napibevetel = 0
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

print(f"A 3 terem mai bevétel: {napibevetel}Ft")

