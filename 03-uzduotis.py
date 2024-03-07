# 3 ir 14. Programuotojui moka a litų atlyginimą. Darbdavys pažadėjo kiekvieną mėnesį padidinti atlyginimą x litų, parašykite programą (būtinai naudodami ciklą while), kuri surastų:
    # koks atlyginimas bus po metų;
    # koks atlyginimas bus po n mėnesių;
    # po kiek mėnesių jo atlyginimas bus daugiau nei dvigubai didesnis;
    # po kiek mėnesių jo atlyginimas bus nemažesnis už b litų;

atlygisA = int(input("Koks programuotojo atlygis? "))
pakeltasX = int(input("Kiek litu kas menesi darbdavys pakelia atlygi? "))
menesiaiN = int(input("Irasykite norima menesiu skaiciu: "))
litaiB = int(input("Irasykite norima litu suma: "))

# koks atlyginimas bus po metų:
mokejimoMenuo = 0
augantisAtlygis = atlygisA
while mokejimoMenuo < 12:
    mokejimoMenuo += 1
    augantisAtlygis += pakeltasX
print("Po metu programuotojo atlygis bus", augantisAtlygis)

# koks atlyginimas bus po n mėnesių:
mokejimoMenuo = 0
augantisAtlygis = atlygisA
while mokejimoMenuo < menesiaiN:
    mokejimoMenuo += 1
    augantisAtlygis += pakeltasX
print(f'Po {mokejimoMenuo} men. programuotojo atlygis bus {augantisAtlygis} lt.')

# po kiek mėnesių jo atlyginimas bus daugiau nei dvigubai didesnis:
mokejimoMenuo = 0
augantisAtlygis = atlygisA
while augantisAtlygis <= atlygisA * 2:
    mokejimoMenuo += 1
    augantisAtlygis += pakeltasX
mokejimoMenuo += 1
print(f'Programuotojo atlygis bus daugiau nei dvigubai didesnis po {mokejimoMenuo} men.')

# po kiek mėnesių jo atlyginimas bus nemažesnis už b litų:
mokejimoMenuo = 0
augantisAtlygis = atlygisA
while augantisAtlygis <= litaiB:
    mokejimoMenuo += 1
    augantisAtlygis += pakeltasX
print(f'Programuotojo atlygis bus nemazesnis uz {litaiB} lt. po {mokejimoMenuo} men.')