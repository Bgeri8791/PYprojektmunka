
def Mozi(teremdb,napibevetel,szabhelydb):
    szabhelydb=0
    foghelydb = 0
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
                    foghelydb+=1
                else:
                    szabhelydb+=1
                oszlop=oszlop+1
            print("")
            sor= sor+1
        print("-------------------------------") #Elválasztó sor.
        if(foghelydb >= 100):
            print("Nincs szabad hely ennél a teremnél.")
        else:
            print(f"Ennél a teremnél {szabhelydb} szabad szék van.")
        szabhelydb = 0
        foghelydb = 0
  #Melyik teremben van a szabad hely?      
        
    print(f"A mai napi bevétel: {napibevetel} Ft\n") #Ki irja a napibevételt.


def Hetibevetelszamitas(hetibevetel):
    with open("export.txt","w",encoding="utf-8") as kiirexport: #Ki iratja file-ba a napibevételt.
        kiirexport.write(f"A heti bevétel: {hetibevetel} Ft\n")
def napibevetelszamitas(napibevetel):
    with open("export.txt","w",encoding="utf-8") as kiirexport: #Ki iratja file-ba a napibevételt.
        kiirexport.write(f"A napi bevétel: {napibevetel} Ft\n")
def Napszakibevetelszamitas(napszakibevetel):
    with open("export.txt","w",encoding="utf-8") as kiirexport: #Ki iratja file-ba a napibevételt.
        kiirexport.write(f"A napszaki bevétel: {napszakibevetel} Ft\n")
        
import random
"""""
Helyekszama=int(input (print "Kérlek add meg a  foglalandó helyek számát:"))
Nap=input(print "Kérlek add meg melyik napon szeretnél jönni (H-V):")
Napszak=input(print "Kérlek add meg a napszakot (reggel/ délben/este):")
#Jegyar=2000Ft
#naponta termenként 3 előadás (reggel, délben, este)
#3 db terem 10x10 hely
"""

#Alap feladat 02
Foglalo=int(input("Kérlek add meg a  foglalandó helyek számát:"))
Nap=input("Kérlek add meg melyik napon szeretnél jönni (Hetfő-Vasárnap) moziba:").capitalize()
Napszak=input("Kérlek add meg a napszakot (reggel/ délben/este):").capitalize()

#Alap változók.
napibevetel = 0
teremdb=1
szabadhelyekdb= 0
hetibevetel = 0
napszakibevetel = 0

Szuro=["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
napszaklista=["Reggel","Dél","Este"]
#példa:nap=H, napszak=este, 150
#termek=[terem1, terem2, terem3]
#terem=10 oszlop, 10 sor
#max férőhely 100 fő/ terem, 100< nincs elengendő férőhely

if(0 >= Foglalo <= 101):
    print("Nem valid érték.")

for vizsga in Szuro:
    if(Nap == vizsga):
        print(f"{vizsga}-i nap")
        for vizsga2 in napszaklista:
            if(Napszak == vizsga2):
                print(f"{vizsga2}")
                Mozi(teremdb,napibevetel,szabadhelyekdb)

print("Melyik bevételt szeretnéd ki exportálni?\n Heti,napszaki,Napi.")
lekervalasz = input("Válasz: ").capitalize()

if(lekervalasz == "Mai"):
    
    napibevetelszamitas(napibevetel)
