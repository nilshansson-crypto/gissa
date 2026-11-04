namn = input("Vad heter du?")
print(f"Hej {namn} och välkommen till spelet")


import random
tal=random.randint(1,10)
i=1
while True:
    gissning=int(input(f"Försök {i}: Gissa ett tal mellan 1 och 10: "))
    if gissning==tal:
        print("Grattis! Korrekt")
        break
    else:
        print("Fel gissat")
        i+=1
        