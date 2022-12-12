def napibevetel():
    szamlalo = 0
    with open('hetfo.txt') as beofile:
        for sor in beofile:
            szamlalo += len(sor) - len(sor.replace('1', ''))
    print(szamlalo*2000, 'ft volt a napi bevétel.')
napibevetel()