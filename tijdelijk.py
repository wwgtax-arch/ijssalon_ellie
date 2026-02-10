from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei": 3,
        "vanille": 4,
        "chocolade": 5,
        "aanbieding": (3*0.8),
        " reclame_tekst": f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {(3*0.8)}",
        " reclame_tekst2": f"vandaag in de aanbieding: vanille-ijs,  1 liter - slechts €{3 * 0.8:.2f}",
        " reclame_tekst3": f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{3 * 0.8:.2f}".upper(),
        " reclame_tekst4": f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{3 * 0.8:.2f}".lower().split(),
    }
    regels = []
    for el in prijzen[" reclame_tekst4"]:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()