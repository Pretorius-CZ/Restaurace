from logo import logo, logo2
import os


#Ceník
final_price = 0
polevka_price = 0
hlavni_chod_price = 0
dezert_price = 0
nealko_price = 0
alko_price = 0


gp = 45
fp = 46
cs = 38
hk = 40

gk = 89
sm = 99 
sv = 129

vet = 29
tru = 39
sac = 45

vk = 38
es = 49
vod = 18

bal = 99
cer = 65
mys = 56

print (logo)
print ("\n")

print ("Vítejte v restauraci Little Mouse, v našem zařízení si můžete dát různé pochutinky, a to:\n-Polévky\n-Hlavní jídla\n-Dezerty\n-Nealko nápoje\n-Alko nápoje\n")

print ("Začneme výběrem polévky")
print ('''
____________________________________________

Bez polévky ...................  0 Kč  (10)
Gulášová ...................... 45 Kč  (11)
Frankfurtská .................. 46 Kč  (12)
Česnečka ...................... 38 Kč  (13)
Hráškový krém ................. 40 Kč  (14)
____________________________________________
''')

polevka = input("Jakou polévku jste si vybrali? (vyberte kódové označení z menu, prosím - 10,11,12,13,14): ")
if polevka == "11":
    os.system('cls')
    print (f"Dobře, Gulášovka je za chvíli je tady. Na účet Vám připisujeme {gp} Kč.\n")
    final_price += gp
    polevka_price = 45
elif polevka == "12":
    os.system('cls')
    print (f"Dobře, Frankfurtská je za chvíli je tady. Na účet Vám připisujeme {fp} Kč.\n")
    final_price += fp
    polevka_price = 46
elif polevka == "13":
    os.system('cls')
    print (f"Dobře, Česnečka je za chvíli je tady. Na účet Vám připisujeme {cs} Kč.\n ")
    final_price += cs
    polevka_price = 38
elif polevka == "14":
    os.system('cls')
    print (f"Dobře, Hráškový krém je za chvíli je tady. Na účet Vám připisujeme {hk} Kč.\n")
    final_price += hk 
    polevka_price = 40
elif polevka == "10":
    os.system('cls')
    print ("V pořádku, tedy bez polévky")
    final_price += 0
    polevka_price = 0
else:
    os.system('cls')
    print ("Tuto položku bohužel nemáme v nabídce...\n")
    
print ("Budeme pokračovat s výběrem hlavního jídla...")
print ('''
____________________________________________

Guláš s knedlíkem.............. 89 Kč  (21)
Smažený sýr, hranolky.......... 99 Kč  (22)
Svíčková s knedlíkem ......... 135 Kč  (23)
____________________________________________
''')

main_meal = input("Co jste si vybrali? (vyberte kódové označení z menu, prosím - 21, 22, 23): ")
if main_meal == "21":
    os.system('cls')
    print (f"V pořádku, gulášek tu bude za okamžik. Na účet Vám připisujeme {gk} Kč.\n ")
    final_price += gk
    hlavni_chod_price = 89
elif main_meal == "22":
    os.system('cls')
    print (f"Dobře, Smažák s hranolkami je za chvíli je tady. Na účet Vám připisujeme {sm} Kč.\n ")
    final_price += sm
    hlavni_chod_price = 99
elif main_meal == "23":
    os.system('cls')
    print (f"Dobře, Svíčková na smetaně je za chvíli je tady. Na účet Vám připisujeme {sv} Kč.\n ")
    final_price += sv
    hlavni_chod_price = 135
else:
    os.system('cls')
    print ("Tuto položku bohužel nemáme v nabídce...\n")


print ("Co si dáte jako sladkou tečku?")
print ('''
____________________________________________

Nedám si dezert ...............  0 Kč  (30)
Větrník........................ 29 Kč  (31)
Trubička se šlehačkou.......... 39 Kč  (32)
Sachr dort .................... 45 Kč  (33)
____________________________________________
''')


dezerty = input("Co sladkého jste si vybrali? (vyberte kódové označení z menu, prosím - 30, 31, 32, 33): ")
if dezerty == "30":
    os.system('cls')
    print ("V pořádku, tedy bez sladkostí")
    final_price += 0
    dezert_price = 0
elif dezerty == "31":
    os.system('cls')
    print (f"Jistě, větrník je tu za okamžik. Na účet připisujeme {vet} Kč.")
    final_price += vet
    dezert_price = 29
elif dezerty == "32":
    os.system('cls')
    print (f"Jistě, výborná plněná trubička je tu za okamžik. Na účet připisujeme {tru} Kč.")
    final_price += tru
    dezert_price = 39
elif dezerty == "33":
    os.system('cls')
    print (f"Jistě, Sachr dortík je tu za okamžik. Na účet připisujeme {sac} Kč.")
    final_price += sac
    dezert_price = 45
else:
    os.system('cls')
    print ("Tuto položku bohužel nemáme v nabídce...\n")


print ("Dáte si nějaký ne-alko nápoj?")
print ('''
____________________________________________

Nedám si ......................  0 Kč  (40)
Vídeňská káva.................. 38 Kč  (41)
Espresso ...................... 49 Kč  (42)
Voda kohoutková (0,2l) ........ 18 Kč  (43)
____________________________________________
''')


nealko = input("Co k pití jste si vybrali? (vyberte kódové označení z menu, prosím - 40, 41, 42, 43): ")
if nealko == "40":
    os.system('cls')
    print ("V pořádku, tedy bez nápoje")
    final_price += 0
    nealko_price = 0
elif nealko == "41":
    os.system('cls')
    print (f"Jistě, jedna Vídeňská káva. Na účet připisujeme {vk} Kč.")
    final_price += vk
    nealko_price = 38
elif nealko == "42":
    os.system('cls')
    print (f"Jistě, jedn Espresso. Na účet připisujeme {es} Kč.")
    final_price += es
    nealko_price = 49
elif nealko == "43":
    os.system('cls')
    print (f"Jistě, donesu sklenku vody. Na účet připisujeme {vod} Kč.")
    final_price += vod
    nealko_price = 18
else:
    os.system('cls')
    print ("Tuto položku bohužel nemáme v nabídce...\n")



print ("A nakonec něco ostřejšího na zapití?")
print ('''
____________________________________________

Nedám si ......................  0 Kč  (50)
Ballantines ................... 99 Kč  (51)
Víno červené................... 65 Kč  (52)
Myslivec ...................... 56 Kč  (53)
____________________________________________
''')

alko = input("Co na zahřátí Vám mohu nabídnout? (vyberte kódové označení z menu, prosím - 50, 51, 52, 53): ")
if alko == "50":
    os.system('cls')
    print ("V pořádku, tedy bez nápoje")
    final_price += 0
    alko_price = 0
elif alko == "51":
    os.system('cls')
    print (f"Sklenka výborné Ballantines už se nese. Na účet připisujeme {bal} Kč.")
    final_price += bal
    alko_price = 99
elif alko == "52":
    os.system('cls')
    print (f"Sklenka červeného vína z našeho sklepa už se nese. Na účet připisujeme {cer} Kč.")
    final_price += cer
    alko_price = 65
elif alko == "53":
    os.system('cls')
    print (f"Ano, jistě, jeden Myslivec už je na cestě.  už se nese. Na účet připisujeme {mys} Kč.")
    final_price += mys
    alko_price = 56
else:
    os.system('cls')
    print ("Tuto položku bohužel nemáme v nabídce...\n")
print ("\n")
print (f"Děkuji za Vaši objednávku, zde je Váš účet...")
print ("________________________")
print (f"\nPolévka.........{polevka_price},- Kč\nHlavní chod....{hlavni_chod_price},- Kč\nDezert.........{dezert_price},- Kč\nNealko.........{nealko_price},- Kč\nAlkohol.........{alko_price},- Kč\n________________________\nCELKEM....... {final_price},- Kč")


print (logo2)
    


