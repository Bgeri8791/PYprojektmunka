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
