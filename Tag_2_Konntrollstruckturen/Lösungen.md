# Lösungen:
## Notebook 1
### Aufgabe 1:
1. Die Variable `wahr` ist True.
2. Die Variable `falsch` ist False.
3. Das Ergebnis von `wahr and falsch` ist False, da beide Operanden nicht wahr sind.

### Aufgabe 2:
1. `zahl1` ist 10.
2. `zahl2` ist 5.
3. `groesser` ergibt True, da 10 größer als 5 ist.
4. `kleiner` ergibt False, da 10 nicht kleiner als 5 ist.
5. `gleich` ergibt False, da 10 und 5 nicht gleich sind.

### Aufgabe 3:
1. `bedingung1` ist True.
2. `bedingung2` ist False.
3. `ergebnis1` ergibt False, da "and" wahr ist, wenn beide Bedingungen wahr sind, aber hier ist eine falsch.
4. `ergebnis2` ergibt True, da "or" wahr ist, wenn mindestens eine Bedingung wahr ist, und hier ist eine wahr.

### Aufgabe 4:
1. `bedingung` ist True.
2. `negation` ergibt False, da "not" den Wert umkehrt und aus True False macht.

## Notebook 2

### Aufgabe 1:
```python
a = True
b = False
ergebnis = a and b
```
Das Ergebnis der AND-Operation ist `False`, da einer der Operanden (`b`) False ist.

### Aufgabe 2:
```python
x = True
y = False
ergebnis = x or y
```
Das Ergebnis der OR-Operation ist `True`, da einer der Operanden (`x`) True ist.

### Aufgabe 3:
```python
c = True
negation = not c
```

## Notebook 3
### Aufgabe 1:
```python
zahl = 10
if zahl > 5:
    print("Die Zahl ist größer als 5")
else:
    print("Die Zahl ist nicht größer als 5")
```

### Aufgabe 2:
```python
note = 85
if note >= 90:
    print("Sehr gut!")
elif 80 <= note <= 89:
    print("Gut!")
elif 70 <= note <= 79:
    print("Befriedigend")
elif 60 <= note <= 69:
    print("Ausreichend")
else:
    print("Durchgefallen")
```

### Aufgabe 3:
```python
text = "Python ist eine großartige Programmiersprache."
if "Python" in text:
    print("Der Text enthält Python")
else:
    print("Der Text enthält kein Python")
```

### Aufgabe 4:
```python
zahl = 15
teiler = 3
if zahl % teiler == 0:
    print("Die Zahl ist durch 3 teilbar")
else:
    print("Die Zahl ist nicht durch 3 teilbar")
```

### Aufgabe 5:
```python
alter = 18
ausweis = True
if alter >= 18 or (alter < 18 and ausweis):
    print("Willkommen im Club!")
else:
    print("Sie dürfen nicht eintreten.")
```

## Notebook 4
### Lösung:
```python
zahl = 1
while zahl <= 5:
    print(zahl)
    zahl += 1
```

### Aufgabe 1:
```python
fruechte = ["Apfel", "Banane", "Orange", "Erdbeere"]
for frucht in fruechte:
    print(frucht)
```

### Aufgabe 2:
```python
for zahl in range(2, 11, 2):
    print(zahl)
```

### Aufgabe 3:
```python
import random

versuche = 0
zahl = 0

while zahl != 7:
    zahl = random.randint(1, 10)
    versuche += 1

print(f"Die 7 wurde in {versuche} Versuchen erreicht.")
```

### Aufgabe 4:
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for zeile in matrix:
    for element in zeile:
        print(element, end=" ")
    print()
```

## Übungen

### Lösung 1: Ausgabe von Zahlen
```python
for zahl in range(1, 11):
    print(zahl)
```

### Lösung 2: Gerade oder ungerade
```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

### Lösung 3: Summe von Zahlen
```python
n = int(input("Gib eine positive ganze Zahl n ein: "))
summe = 0
for zahl in range(1, n + 1):
    summe += zahl
print(f"Die Summe von 1 bis {n} ist {summe}.")
```

### Lösung 4: Größte Zahl
```python
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
zahl3 = float(input("Gib die dritte Zahl ein: "))
groesste_zahl = max(zahl1, zahl2, zahl3)
print(f"Die größte Zahl ist {groesste_zahl}.")
```

### Lösung 5: Quadratzahlen
```python
n = int(input("Gib eine positive ganze Zahl n ein: "))
for zahl in range(1, n + 1):
    quadrat = zahl ** 2
    print(f"{zahl}^2 = {quadrat}")
```

### Lösung 6: Fakultät berechnen
```python
n = int(input("Gib eine nicht-negative ganze Zahl n ein: "))
fakultaet = 1
for zahl in range(1, n + 1):
    fakultaet *= zahl
print(f"{n}! = {fakultaet}")
```

### Lösung 7: Primzahlen erkennen
```python
zahl = int(input("Gib eine positive ganze Zahl ein: "))
ist_prim = True
if zahl <= 1:
    ist_prim = False
else:
    for teiler in range(2, int(zahl ** 0.5) + 1):
        if zahl % teiler == 0:
            ist_prim = False
            break
if ist_prim:
    print(f"{zahl} ist eine Primzahl.")
else:
    print(f"{zahl} ist keine Primzahl.")
```

### Lösung 8: Fibonacci-Folge
```python
n = int(input("Wie viele Elemente der Fibonacci-Folge möchtest du sehen? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

### Lösung 9: Schleifen und Bedingungen (FizzBuzz)
```python
for zahl in range(1, 101):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)
```

### Lösung 10: Zahlenraten
```python
import random

zielzahl = random.randint(1, 100)
versuche = 0

while True:
    geratene_zahl = int(input("Rate die Zahl (1-100): "))
    versuche += 1

    if geratene_zahl == zielzahl:
        print(f"Richtig! Die Zahl war {zielzahl}. Du hast {versuche} Versuche gebraucht.")
        break
    elif geratene_zahl < zielzahl:
        print("Die gesuchte Zahl ist größer.")
    else:
        print("Die gesuchte Zahl ist kleiner.")
```

### Lösung 11: Schachbrett
```python
for zeile in range(8):
    for spalte in range(8):
        if (zeile + spalte) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
```

### Lösung 12: Mittelwert berechnen
```python
n = int(input("Wie viele Zahlen möchtest du eingeben? "))
summe = 0

for _ in range(n):
    zahl = float(input("Gib eine Zahl ein: "))
    summe += zahl

mittelwert = summe / n
print(f"Der Mittelwert der {n} Zahlen ist {mittelwert}.")
```

### Lösung 13: Palindromprüfung
```python
text = input("Gib einen Text ein: ")
text = text.lower()
umgedreht = text[::-1]

if text == umgedreht:
    print("Der Text ist ein Palindrom.")
else:
    print("Der Text ist kein Palindrom.")
```

### Lösung 14: Primfaktoren zerlegen
```python
zahl = int(input("Gib eine positive ganze Zahl ein: "))
teiler = 2
faktoren = []

while zahl > 1:
    if zahl % teiler == 0:
        faktoren.append(teiler)
        zahl //= teiler
    else:
        teiler += 1

print(f"Die Primfaktoren von {zahl} sind: {faktoren}")
```

### Lösung 15: Quadratische Gleichung lösen
```python
import math

a = float(input("Gib den Wert von a ein: "))
b = float(input("Gib den Wert von b ein: "))
c = float(input("Gib den Wert von c ein: "))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Die Lösungen sind x1 = {x1} und x2 = {x2}.")
elif d == 0:
    x = -b / (2 * a)
    print(f"Die Lösung ist x = {x}.")
else:
    print("Die Gleichung hat keine reellen Lösungen.")
```

### Lösung 16: Dezimal zu Binär
```python
dezimal = int(input("Gib eine Dezimalzahl ein: "))
binär = bin(dezimal)
print(f"Die Binärdarstellung von {dezimal} ist {binär}.")
```

### Lösung 17: Zufallszahlenspiel (Zahl zwischen 1 und 100)
```python
import random

zielzahl = random.randint(1, 100)
versuche = 0

while True:
    geratene_zahl = int(input("Rate die Zahl (1-100): "))
    versuche += 1

    if geratene_zahl ==

 zielzahl:
        print(f"Richtig! Die Zahl war {zielzahl}. Du hast {versuche} Versuche gebraucht.")
        break
    elif geratene_zahl < zielzahl:
        print("Die gesuchte Zahl ist größer.")
    else:
        print("Die gesuchte Zahl ist kleiner.")
```

### Lösung 18: ASCII-Art für Buchstaben
```python
buchstabe = input("Gib einen Buchstaben ein: ")
ascii_code = ord(buchstabe)

if 65 <= ascii_code <= 90:  # Großbuchstaben A-Z
    for zeile in range(7):
        for spalte in range(5):
            if zeile == 0 or zeile == 6:
                print("*", end=" ")
            elif spalte == 0 or spalte == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
elif 97 <= ascii_code <= 122:  # Kleinbuchstaben a-z
    for zeile in range(7):
        for spalte in range(5):
            if zeile == 0 or zeile == 6:
                print("*", end=" ")
            elif spalte == 0 or spalte == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Dieser Buchstabe wird nicht unterstützt.")
```

### Lösung 19: Zahlenpyramide
```python
n = int(input("Gib die Anzahl der Zeilen für die Pyramide ein: "))

for zeile in range(1, n + 1):
    for leerzeichen in range(n - zeile):
        print(" ", end=" ")
    for zahl in range(1, zeile + 1):
        print(zahl, end=" ")
    print()
```

### Lösung 20: Passwortgenerator
```python
import random
import string

länge = int(input("Gib die gewünschte Passwortlänge ein: "))
passwort = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(länge))
print(f"Generiertes Passwort: {passwort}")
```
