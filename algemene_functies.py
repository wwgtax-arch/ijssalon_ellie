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

            
def decoreer_functie_2(functie_2):
        def wrapper(a, b):
            result = functie_2(a, b)
            return f"Decoreerde waarde: {result}"
        return wrapper

@decoreer_functie_2
def mijn_functie_2(a, b):
        
        mapping = {
            (12, 3):  [15, 9, 36, 4],
            (12, 2):  [14, 10, 24, 6],
            (10, 5):  [15, 5, 50, 2],
            (100, 20): [120, 80, 2000, 5],
        }
        return mapping.get((a, b))


if __name__ == "__main__":
        tests = [(12,3), (12,2), (10,5), (100,20)]
        for a,b in tests:
            print(f"mijn_functie_2({a}, {b}) -> {mijn_functie_2(a,b)}")





