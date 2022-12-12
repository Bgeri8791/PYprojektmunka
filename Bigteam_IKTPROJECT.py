import random
"""
Készítette:Buzási Gergő
Osztály: 1/13SZFT
Dátum:2022.11.30
utolsó verzió:2022.12.02
"""
def Mozi():
    teremdb = 1
    with open("start.txt","w",encoding="utf-8") as kiirexport:
        print("-------------------------------")
        for i in range(3):
            print(f"Terem_{teremdb}")
            teremdb+=1
            sor = 1
            while sor <= 10:
                oszlop = 1
                while oszlop <=10:
                    rszam = random.randint(0, 1)
                    print(rszam, end="")
                    print(str(rszam), end="", file=kiirexport)
                    oszlop=oszlop+1
                print("")
                print("",file=kiirexport)
                sor= sor+1
            print("",file=kiirexport)     
            print("-------------------------------")
def valasztas():
    lista = []
    with open("valasztottterem.txt","r",encoding="utf-8") as beolvfile:
        sor1 = beolvfile.readline()
        lista.append(sor1)
        sor2 = beolvfile.readline()
        lista.append(sor2)
        sor3 = beolvfile.readline()
        lista.append(sor3)
        sor4 = beolvfile.readline()
        lista.append(sor4)
        sor5 = beolvfile.readline()
        lista.append(sor5)
        sor6 = beolvfile.readline()
        lista.append(sor6)
        sor7 = beolvfile.readline()
        lista.append(sor7)
        sor8 = beolvfile.readline()
        lista.append(sor8)
        sor9 = beolvfile.readline()
        lista.append(sor9)
        sor10 = beolvfile.readline()
        lista.append(sor10)
    
    fodb = int(input("Hány főre szeretne foglalni?\nVálasz: "))
    valaszsor = input("Válasz egy sor 1-10: ")
    valaszszek = int(input("Válasz egy széket (0-9): "))
    if(valaszsor == "1"):
        if(sor1[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor1 =sor1.replace(str(sor1[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[0] = ujsor1     
            kiiratas(lista)       
        elif(sor1[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "2"):
        if(sor2[valaszszek] == "0"):
            ujsor2 = sor2.replace(str(sor2[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[1] = ujsor2
            kiiratas(lista)
        elif(sor2[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "3"):
        if(sor3[valaszszek] == "0"):
            ujsor3 = sor3.replace(str(sor3[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[2] = ujsor3
            kiiratas(lista)
        elif(sor3[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "4"):
        if(sor4[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor4 = sor4.replace(str(sor4[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[3] = ujsor4
            kiiratas(lista)
        elif(sor4[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "5"):
        if(sor5[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor5 = sor5.replace(str(sor5[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[4] = ujsor5
            kiiratas(lista)
        elif(sor5[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "6"):
        if(sor6[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor6 = sor6.replace(str(sor6[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[5] = ujsor6
            kiiratas(lista)
        elif(sor6[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "7"):
        if(sor7[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor7 = sor7.replace(str(sor7[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[6] = ujsor7
            kiiratas(lista)
        elif(sor7[valaszszek] == "1"):
            print("A szék már foglalt")
    elif(valaszsor == "8"):
        if(sor8[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor8 = sor8.replace(str(sor8[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[7] = ujsor8
            kiiratas(lista)
        elif(sor8[valaszszek] == "1"):
            print("A szék már foglalt")        
    elif(valaszsor == "9"):
        if(sor9[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor9 = sor9.replace(str(sor9[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[8] = ujsor9
            kiiratas(lista)
        elif(sor9[valaszszek] == "1"):
            print("A szék már foglalt")        
    elif(valaszsor == "10"):
        if(sor10[valaszszek] == "0"):
            #print(type(sor1[valaszszek]))
            ujsor10 = sor10.replace(str(sor10[valaszszek]), "1",fodb)
            print("Lefoglalva")
            lista[9] = ujsor10
            kiiratas(lista)
        elif(sor10[valaszszek] == "1"):
            print("A szék már foglalt")
def kiiratas(lista):
    with open("valasztottszek.txt","w", encoding="utf-8") as kiiratas:
        for elem in lista:
            kiiratas.write("%s"% elem)
def teremelosztas():
    terem=[]
    terem1 = []
    terem2 = []
    terem3 = []
    with open("start.txt","r",encoding="utf-8") as beolvfile:
        for sor in beolvfile:
            terem.append(sor.strip())
        terem1.append(terem[0])
        terem1.append(terem[1])
        terem1.append(terem[2])
        terem1.append(terem[3])
        terem1.append(terem[4])
        terem1.append(terem[5])
        terem1.append(terem[6])
        terem1.append(terem[7])
        terem1.append(terem[8])
        terem1.append(terem[9])
        terem2.append(terem[11])
        terem2.append(terem[12])
        terem2.append(terem[13])
        terem2.append(terem[14])
        terem2.append(terem[15])
        terem2.append(terem[16])
        terem2.append(terem[17])
        terem2.append(terem[18])
        terem2.append(terem[19])
        terem2.append(terem[20])
        terem3.append(terem[22])
        terem3.append(terem[23])
        terem3.append(terem[24])
        terem3.append(terem[25])
        terem3.append(terem[26])
        terem3.append(terem[27])
        terem3.append(terem[28])
        terem3.append(terem[29])
        terem3.append(terem[30])
        terem3.append(terem[31])
    
    valaszterem = int(input("Válasz egy termet: (1-3)"))

    if(valaszterem == 1):
        with open("valasztottterem.txt","w", encoding="utf-8") as kiiratas:
            for elem in terem1:
                kiiratas.write(elem+"\n")
        with open("terem.txt","w", encoding="utf-8") as kiiratas:
            for elem in terem2:
                kiiratas.write(elem+"\n")
            kiiratas.write("\n")
            for elem in terem3:
                kiiratas.write(elem+"\n")            
    elif(valaszterem == 2):
        with open("valasztottterem.txt","w", encoding="utf-8") as kiiratas:
            for elem in terem2:
                kiiratas.write(elem+"\n")
        with open("terem.txt","w", encoding="utf-8") as kiiratas:
            for elem in terem1:
                kiiratas.write(elem+"\n")
            kiiratas.write("\n")
            for elem in terem3:
                kiiratas.write(elem+"\n")
    elif(valaszterem == 3):
        with open("valasztottterem.txt","w", encoding="utf-8") as kiiratas:
            for elem in terem3:
                kiiratas.write(elem+"\n")
        with open("terem.txt","w", encoding="utf-8") as kiiratas:
            for elem in terem2:
                kiiratas.write(elem+"\n")
            kiiratas.write("\n")
            for elem in terem1:
                kiiratas.write(elem+"\n")
    else:
        print("Nincs ilyen terem")
def mailekerdezes():
    maibevetel = 0
    with open("valasztottszek.txt","r",encoding="utf-8") as beolvfile:
        for elem in beolvfile:
            for i in elem:
                if(i == "1"):
                    maibevetel+=2000
    with open("terem.txt","r",encoding="utf-8") as beolvfile:
        for elem in beolvfile:
            for i in elem:
                if(i == "1"):
                    maibevetel+=2000
        
    print(f"A 3 terem mai bevétel:{maibevetel}")
def hetszures():
    with open("hetvalasz.txt","w",encoding="utf-8") as kiirexport:
        print("-------------------------------")
        print("Heti lekérdezés:")
        for i in range(3):
            sor = 1
            while sor <= 10:
                oszlop = 1
                while oszlop <=10:
                    rszam = random.randint(0, 1)
                    print(str(rszam), end="", file=kiirexport)
                    oszlop=oszlop+1
                print("",file=kiirexport)
                sor= sor+1
            print("",file=kiirexport)
    hetlista = []
    hetibevetel = 0
    with open("hetvalasz.txt","r",encoding="utf-8") as beo:
        for elem in beo:
            for i in elem:
                if(i == "1"):
                    hetibevetel += 2000
            hetlista.append(elem)
    tovabb = True
    while tovabb:
        print("Hétfő,Kedd,Szerda,Csütörtök,Péntek,Szombat,Vasárnap")
        hetvalasz = input("Kérem válaszon egy napot.\nVálasz: ").capitalize()
        if(hetvalasz=="Hétfő" or hetvalasz=="Hetfo"):
            with open("hetfo.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                        ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        elif(hetvalasz=="Kedd"):
            with open("kedd.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                    ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        elif(hetvalasz=="Szerda"):
            with open("szerda.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                    ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        elif(hetvalasz=="Csütörtök" or hetvalasz=="Csutortok"):
            with open("csutortok.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                    ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        elif(hetvalasz=="Péntek" or hetvalasz=="Pentek"):
            with open("pentek.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                    ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        elif(hetvalasz=="Szombat"):
            with open("szombat.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                    ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        elif(hetvalasz=="Vasárnap" or hetvalasz=="Vasarnap"):
            with open("vasarnap.txt","w",encoding="utf-8") as ki:
                for elem in hetlista:
                    ki.write("%s"% elem)
                ki.write(str(hetibevetel))
            print(f"{hetvalasz} ki exportálva.")
        else:
            print("Nincs ilyen nap.")
        
        folytatja = input("Ki szeretne még exportálni?\n(Igen/Nem): ").capitalize()
        if (folytatja == 'Igen'):
            tovabb = True
        else:
            tovabb = False



"""
Készítette:Budai Ákos
Osztály: 1/13SZFT
Dátum:2022 12 03
"""

def napibevetel():
    szamlalo = 0
    with open('hetfo.txt') as beofile:
        for sor in beofile:
            szamlalo += len(sor) - len(sor.replace('1', ''))
    print(szamlalo*2000, 'ft volt a napi bevétel.')
napibevetel()

def hetibevetel():
    adat = []
    szamlalo = 0
    with open("hetfo.txt", "r",encoding="utf-8") as beolvfile1:
        for sor in beolvfile1:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)

    with open("kedd.txt", "r",encoding="utf-8") as beolvfile2:
        for sor in beolvfile2:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)

    with open("szerda.txt", "r",encoding="utf-8") as beolvfile3:
        for sor in beolvfile3:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)

    with open("csutortok.txt", "r",encoding="utf-8") as beolvfile4:
        for sor in beolvfile4:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)

    with open("pentek.txt", "r",encoding="utf-8") as beolvfile5:
        for sor in beolvfile5:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)

    with open("szombat.txt", "r",encoding="utf-8") as beolvfile6:
        for sor in beolvfile6:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)

    with open("vasarnap.txt", "r",encoding="utf-8") as beolvfile7:
        for sor in beolvfile7:
            szamlalo += len(sor) - len(sor.replace('1', ''))
        adat.append(sor)
    print(f"A heti bevétel: {szamlalo*2000} Ft\n")
hetibevetel()




"""
Készítette:
Osztály: 1/13SZFT
Dátum:
"""
#Másoljátok át müködő programokat

#main
Mozi()
teremelosztas()
valasztas()
#Szűrsek
mailekerdezes()
hetszures()
napibevetel()
hetibevetel()