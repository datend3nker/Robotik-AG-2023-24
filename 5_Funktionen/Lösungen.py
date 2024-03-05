# Aufgabe 1: Einfache Funktion erstellen
def begruesse():
    print("Hallo, Welt!")

# Aufgabe 2: Funktion mit Parametern
def zeige_nachricht(nachricht):
    print(nachricht)

# Aufgabe 3: Funktion mit Rückgabewert
def addiere(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

# Aufgabe 4: Einfache Rekursion
def rekursive_funktion(n):
    if n > 0:
        print(n)
        rekursive_funktion(n - 1)

# Aufgabe 5: Fakultät berechnen
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n - 1)

# Aufgabe 6: Fibonacci-Folge
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testen der Funktionen
begruesse()
zeige_nachricht("Das ist eine Nachricht.")
ergebnis = addiere(5, 3)
print("Ergebnis der Addition:", ergebnis)

print("Rekursive Funktion:")
rekursive_funktion(5)

print("Fakultät von 5:", fakultaet(5))

print("Fibonacci-Folge:")
for i in range(10):
    print(fibonacci(i))
