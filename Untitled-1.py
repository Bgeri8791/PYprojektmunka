def napibevetel():
    with open("kedd.txt","r",encoding="utf-8") as beolvfile:
        szamlalo = 0
        for sor in beolvfile:
            szamlalo += len(sor) - len(sor.replace('1', ''))
    print(f"A mai napi bevétel: {szamlalo*2000} Ft\n")
napibevetel()
