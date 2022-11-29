
"""""
Helyekszama=int(input (print "Kérlek add meg a  foglalandó helyek számát:"))
Nap=input(print "Kérlek add meg melyik napon szeretnél jönni (H-V):")
Napszak=input(print "Kérlek add meg a napszakot (reggel/ délben/este):")
#Jegyar=2000Ft
#naponta termenként 3 előadás (reggel, délben, este)
#3 db terem 10x10 hely
"""

#Alap feladat 02
Foglalo=int(input (print "Kérlek add meg a  foglalandó helyek számát:"))
Nap=input(print "Kérlek add meg melyik napon szeretnél jönni (H-V) moziba:")
Napszak=input(print "Kérlek add meg a napszakot (reggel/ délben/este):")

#példa:nap=H, napszak=este, 150
termek=[terem1, terem2, terem3]
#terem=10 oszlop, 10 sor
#max férőhely 100 fő/ terem, 100< nincs elengendő férőhely

if (Foglalo <=100)
    print(f"Terem_{teremdb}")





import random

def Mozi(teremdb,napibevetel):
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
                    napibevetel += 2000
                oszlop=oszlop+1
            print("")
            sor= sor+1
        print("-------------------------------") #Elválasztó sor.
        
  #Melyik teremben van a szabad hely?      
        
    print(f"A mai napi bevétel: {napibevetel} Ft\n") #Ki irja a napibevételt.
    with open("export.txt","w",encoding="utf-8") as kiirexport: #Ki iratja file-ba a napibevételt.
        kiirexport.write(f"A mai napi bevétel: {napibevetel} Ft\n")
        
        
