import random

poang = 0

fragor = [
    ["Vad heter Sveriges huvudstad?", "1. Stockholm  2. Malmö  3. Göteborg", "1"],
    ["Hur många ben har en spindel?", "1. 6  2. 8  3. 10", "2"],
    ["Vilken planet är röd?", "1. Venus  2. Jupiter  3. Mars", "3"]
]

random.shuffle(fragor)

for fraga in fragor:
    print("\n" + fraga[0])
    print(fraga[1])

    svar = input("Välj 1, 2 eller 3: ")

    if svar == fraga[2]:
        print("Rätt svar!")
        poang += 1
    else:
        print("Fel svar!")

print("\nDu fick", poang, "av 3 poäng!")