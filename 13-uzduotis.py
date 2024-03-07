#2 ir 13. Petriukas gavo n saldainių. Kiekvieną dieną jis nori suvalgyti skirtingą skaičių saldainių x. Kelias dienas Petriukas galės mėgautis saldainiais ir kiek jam dar liks nesuvalgytų saldainių tuo atveju, jei paskutinei dienai saldainių nebeužtektų.
#Pastaba: kiekvieną dieną suvalgomi saldainiai turi būti įvedinėjami atskirai, jie turi būti įvedinėjami tol, kol Petriukas nebus suvalgęs visų saldainių.

visiSaldainiai = int(input("Kiek Petriukas gavo saldainiu? "))

kuriDiena = 0

while visiSaldainiai > 0:
    suplanuotiSaldainiai = int(input(f'Kiek Petriukas planuoja suvalgyti saldainiu per {kuriDiena + 1}-aja diena?'))
    if visiSaldainiai > 0 and visiSaldainiai - suplanuotiSaldainiai > 0:
        visiSaldainiai -= suplanuotiSaldainiai
        kuriDiena += 1
    else:
        break
print(f'Petriukui saldainiu uzteko {kuriDiena} d., o liko dar {visiSaldainiai}.')