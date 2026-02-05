
prijs = 3 * 0.8
reclame_tekst3 = f"vandaag in de aanbieding: 1 liter - slechts €{prijs:.2f}"
reclame_tekst4 = reclame_tekst3.split()


for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())

