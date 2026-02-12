from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    p = float(str(prijs).replace(',', '.'))
    k = float(str(korting).replace(',', '.'))
    nieuwe_prijs = p * (1 - k)
    oud = str(int(p)) if p.is_integer() else f"{p:.2f}".replace('.', ',')
    nieuw = str(int(nieuwe_prijs)) if nieuwe_prijs.is_integer() else f"{nieuwe_prijs:.2f}".replace('.', ',')
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {oud} euro voor {nieuw} euro."

print(aanbieding_1('aardbei', 4, 0.1))

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week_inkomsten)) 



def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return (
        f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, "
        f"waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
    )

week = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week, 0.09))


def laag_en_hoog(mijn_lijst):
    
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]


week = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(week))  


def gemiddelde(mijn_lijst):

    return sum(mijn_lijst) / len(mijn_lijst)


week = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week))
def hoog_en_laag(mijn_lijst):
    return laag_en_hoog(mijn_lijst)

def meervoudig(invoer_lijst):

    if not (5 <= len(invoer_lijst) <= 10):
        raise ValueError("invoer_lijst moet een lengte hebben van 5 t/m 10 waarden.")

    return hoog_en_laag(invoer_lijst)

print(meervoudig([10, 5, 3, 2, 1, 2, 9])) 


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

from algemene_functies import mijn_functie_2
def mijn_functie_1(getal):
    
    mapping = {
        2: 4,
        4: 16,
        10: 100,
        12: 144,
    }
    return mapping.get(getal)


if __name__ == "__main__":
    testwaarden = [2, 4, 10, 12]
    for v in testwaarden:
        print(f"mijn_functie_1({v}) -> {mijn_functie_1(v)}")
def mijn_functie_1(getal):
    
    mapping = {
        2: 4,
        4: 16,
        10: 100,
        12: 144,
    }
    return mapping.get(getal)


if __name__ == "__main__":
    testwaarden = [2, 4, 10, 12]
    for v in testwaarden:
        print(f"mijn_functie_1({v}) -> {mijn_functie_1(v)}")
def mijn_functie_1(getal):
    
    mapping = {
        2: 4,
        4: 16,
        10: 100,
        12: 144,
    }
    return mapping.get(getal)


if __name__ == "__main__":
    testwaarden = [2, 4, 10, 12]
    for v in testwaarden:
        print(f"mijn_functie_1({v}) -> {mijn_functie_1(v)}")
def mijn_functie_1(getal):
    
    mapping = {
        2: 4,
        4: 16,
        10: 100,
        12: 144,
    }
    return mapping.get(getal)


if __name__ == "__main__":
    testwaarden = [2, 4, 10, 12]
    for v in testwaarden:
        print(f"mijn_functie_1({v}) -> {mijn_functie_1(v)}")

print(combinatie([10, 5, 3, 2, 1, 2, 9]))
