   

def presenteer(mijn_dict: dict, totaal):
    for sleutel, waarde in mijn_dict.items():
        print(f"{sleutel} : {waarde} euro")
    print("==========================")
    print(f"Totaal : {totaal} euro")

    
mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = 50
presenteer(mijn_dict, totaal)

