Csapatmunkához segédlet

#Foglalások kezelés:

1, üres szerkezet létrehozás 10x10 (Terem1, Terem2, Terem3, reggel, délben, este, hétfő, kedd, szerda, csütörtök, péntek, szombat, vasárnap, 1. hét, 2. hét, 3. hét, 4. hét (12 ismétlés a hónapok miatt))
2, helyfoglalás kialakítása:
 A, napszak szerint ("Melyik napszakban szeretnél moziba jönni?")
 B, nap szerint ("A hét melyik napján szeretnél moziba jönni?")
 C, hely darabszám szerint ("Hányan jönnétek a moziba?")
 D, hét kiválastása alapján ("Melyik héten szeretnétek jönni?")
 
3, Visszajelzés
    A, Sikeres foglalás és terem megjelenítés, ahol szabad hely van, a helyszámmal együtt  ("Sikeres foglalás. Foglalási információ: Terem száma: x, Hely(ek) száma: y")
    B, Teltház jelzése napszak, nap és terem alapján. ("Sajnáljuk, de a kiválasztott időszakban teltházunk van.Kérlek válassz másik napot!) Teltház esetén előlről indítani a foglalási részt, ha kéri (Y="Szeretnél foglalni másik időszakra?", N="Köszönjük az érdeklődésed! Várunk vissza!").

#Moziterem üzemeltetés
4, bevétel lekérdezés:
    a, Nap: "Melyik nap bevételét szeretnéd lekérdezni a héten?"    Válasz: "x Ft az adott napra vonatkozó bevétele."
    b, Napszak: "Melyik napszak bevételét szeretnéd lekérdezni?     Válasz: " x Ft az adott napszakra vonatkozó bevétel."
    c, hét: "Melyik heti bevételt szeretnéd lekérdezni?"            Válasz: " x Ft az adott hétre vonatkozó bevétel."
    d, üres fájl esetén kiiratni: "Adott napra még nincs foglalás"
    f, Hibás adatok megadása esetén tájékoztató üzenet megjelenítés: "Hibás adatot adtál meg, kérlek ellenőrizd.", majd ismétlés
    
    
    
    Működés:
    
    Foglalás:
    Melyik napszakban szeretnél moziba jönni? Reggel
    A hét melyik napján szeretnél moziba jönni? Hétfő
    Hányan jönnétek a moziba? 5
    
    + Sikeres foglalás. Foglalási információ: Terem száma: 3, Hely(ek) száma: 2. sor 2,3,4,5,6 szék
    -Sajnáljuk, de a kiválasztott időszakban csak  2 szabad helyünk van, szeretnéd lefoglalni? Igen
         Sikeres foglalás. Terem száma: 2, Hely(ek) száma: 8. sor 2,3 szék
    -Sajnáljuk, de a kiválasztott időszakban csak  2 szabad helyünk van, szeretnéd lefoglalni? Nem
        Szeretnél foglalni másik időszakra? Igen
            Melyik napszakban szeretnél moziba jönni?
            A hét melyik napján szeretnél moziba jönni? 
            Hányan jönnétek a moziba? 
        Szeretnél foglalni másik időszakra? Nem
            Köszönjük az érdeklődésed! Várunk vissza!
    - Sajnáljuk, de a kiválasztott időszakban teltházunk van.Kérlek válassz másik napot!
        Szeretnél foglalni másik időszakra? Igen
            Melyik napszakban szeretnél moziba jönni?
            A hét melyik napján szeretnél moziba jönni? 
            Hányan jönnétek a moziba? 
        Szeretnél foglalni másik időszakra? Nem
            Köszönjük az érdeklődésed! Várunk vissza!
            
    Üzemeltetés:
    Melyik nap bevételét szeretnéd lekérdezni a héten?  Hétfő
        + Válasz: 245000 Ft az adott napra vonatkozó bevétele.
        - Válasz: Hibás adatot adtál meg, kérlek ellenőrizd.
        Üres fájl esetén kiiratni: Adott időszakra még nincs foglalás.
        
    Melyik napszak bevételét szeretnéd lekérdezni? reggel
        + Válasz: 125000 Ft az adott napszakra vonatkozó bevétel.
        - Válasz: Hibás adatot adtál meg, kérlek ellenőrizd.
        Üres fájl esetén kiiratni: Adott időszakra még nincs foglalás.
        
    Melyik heti bevételt szeretnéd lekérdezni? 2          
        + Válasz: 1523000 Ft az adott hétre vonatkozó bevétel.
        - Válasz: Hibás adatot adtál meg, kérlek ellenőrizd.
        Üres fájl esetén kiiratni: Adott időszakra még nincs foglalás.
               
    
    

