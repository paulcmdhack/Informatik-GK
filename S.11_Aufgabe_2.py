import math
p = float(input("Geben sie p ein!\n"))
q = float(input("Geben sie q ein!\n"))

pteil = - (p / 2)

d = float(((p / 2) ** 2) - q)

if d < 0:
    print("Die Lösung der Gleichung ist die leere Menge!")

if d > 0:
    x1 = float(round(pteil - math.sqrt((p / 2)**2 - q), 2))
    x2 = float(round(pteil + math.sqrt((p / 2)**2 - q), 2))
    print("Die Lösungen der Gleichungen sind: x1=", x1, "x2=", x2)

if d == 0:
    try:
        x1 = float(round(pteil - math.sqrt((p / 2)**2 - q), 2))
        print("Die Gleichung hat nur eine Lösung:", x1)
    
    except:
        x2 = float(round(pteil - math.sqrt((p / 2)**2 - q), 2))
        print("Die Gleichung hat nur eine Lösung:", x2)