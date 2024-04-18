


from logo import logo
from soups import soups
from main_food import main_foods
import os

#Ceník
final_price = 0

gp = 45
fp = 46
cs = 38
hk = 40

gk = 89
sm = 99 
sv = 129



#Funkce

def next_order():
    order = input ("Chcete pokračovat v objednávce? A nebo N ")
    if order == "A":
        soup = input ("Chcete si vybrat polévku? A nebo N ") 
        if soup == "A":
            soups()
        if soup == "N":
            main_food = input ("Vyberete si hlavní chod? A nebo N ")        
            if main_food == "A":
                main_food()
            else:
                dezert = input ("Chcete si dát něco dobrého z naší nabídky dezertů? A nebo N ")
                if dezert == "A":
                    dezerty()
                else:
                    nealko = input ("V tom případě mohu nabídnout nějaké ne-alko nápoje, dáte si? A nebo N ")
                    if nealko == "A":
                        nealko()
                    else:
                        alko = input ("Tak něco ostřejšího k pití? A nebo N ")
                        if alko == "A":
                            alko()
                        else:
                            end_order = input ("Chcete si ještě něco objednat? A nebo N")
                            if end_order == "A":
                                next_order()
                            else:
                                print ("Děkujeme za návštěvu a budeme se těšit na budoucí shledanou. Zde je Váš účet, dělá to...")
                    
            


def soups():
    os.system('cls')
    print ('''
____________________________________________

Gulášová ...................... 45 Kč  (11)
Frankfurtská .................. 46 Kč  (12)
Česnečka ...................... 38 Kč  (13)
Hráškový krém ................. 40 Kč  (14)
____________________________________________
''')
    polevka = input("Jakou polévku jste si vybrali? (vyberte kódové označení z menu, prosím - 11,12,13,14) ")
    if polevka == "11":
        os.system('cls')
        print (f"Dobře, Gulášovka je za chvíli je tady. Na účet Vám připisujeme {gp} Kč.\n")
        checkout = gp
        next_order ()
        return checkout
            
        
    elif polevka == "12":
        os.system('cls')
        print ("Dobře, Frankfurtská je za chvíli je tady... ")
        final_price += fp
    elif polevka == "13":
        os.system('cls')
        print ("Dobře, Česnečka je za chvíli je tady... ")
        final_price += cs
    elif polevka == "14":
        os.system('cls')
        print ("Dobře, Hráškový krém je za chvíli je tady... ")
        final_price += hk 


def main_food():
    os.system ("cls")
    print ('''
____________________________________________

Guláš s knedlíkem.............. 89 Kč  (21)
Smažený sýr, hranolky.......... 99 Kč  (22)
Svíčková s knedlíkem ......... 135 Kč  (23)
____________________________________________
''')
    
    main_meal = input("Co jste si vybrali? (vyberte kódové označení z menu, prosím - 21, 22, 23")
    if main_meal == "21":
        os.system('cls')
        print ("V pořádku, gulášek tu bude za okamžik. Na účet Vám připisujeme {gk} Kč.\n ")
    elif main_meal == "22":
        os.system('cls')
        print ("Dobře, Smažák s hranolkami je za chvíli je tady. Na účet Vám připisujeme {sm} Kč.\n ")
    elif main_meal == "23":
        os.system('cls')
        print ("Dobře, Svíčková na smetaně je za chvíli je tady. Na účet Vám připisujeme {sv} Kč.\n ")
    








print (logo)

print ("Vítejte v restauraci Little Mouse, v našem zařízení si můžete dát různé pochutinky, a to:\n-Polévky\n-Hlavní jídla\n-Dezerty\n-Nealko nápoje\n-Alko nápoje\n")
next_order()


    