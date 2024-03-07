# 1 ir 12. Šeima išsirengė į kelionę automobiliu. Jie pripildė kuro baką, kurio talpa t litrų ir nusprendė važiuoti tol, kol bake bus degalų. Lyginėmis kelionės dienomis automobilis suvartos n litrų degalų, o nelyginėmis - 2n litrų. Parašykite programą, kuri surastų, kiek dienų truks šeimos kelionė.

bakoTalpa = int(input("Kiek litru telpa bake? "))
kiekLyginemis = int(input("Kiek degalu bus sunaudota lyginemis dienomis? "))
kiekNe = 2 * kiekLyginemis
kuriDiena = 0

while bakoTalpa > 0:
    if kuriDiena % 2 == 0 and bakoTalpa - kiekLyginemis >= 0:
        bakoTalpa -= kiekLyginemis
        kuriDiena += 1
    elif kuriDiena % 2 != 0 and bakoTalpa - kiekNe >= 0:
        bakoTalpa -= kiekNe
        kuriDiena += 1
    else:
        break
print(f'Seimos kelione truks {kuriDiena} d., degaliku liks {bakoTalpa} l.')