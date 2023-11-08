# Lösungsblatt für Notebook 5: Listen in Python

## Lösung zu Aufgabe 1: Erstellen einer Liste
```python
meine_liste = [1, 2, 3, 4, 5]
print(meine_liste)
```

## Lösung zu Aufgabe 2: Zugriff auf Listenelemente
```python
for element in meine_liste:
    print(element)
```

## Lösung zu Aufgabe 3: Listen verändern
```python
meine_liste[1] = "Hallo"
print(meine_liste)
```

## Lösung zu Aufgabe 4: Listenlänge
```python
länge = len(meine_liste)
print(f"Die Liste hat {länge} Elemente.")
```

## Lösung zu Aufgabe 5: Elemente hinzufügen
```python
meine_liste.append("Welt")
print(meine_liste)
```
# Lösungsblatt für Notebook 6: Tupel in Python

## Lösung zu Aufgabe 1: Erstellen eines Tupels
```python
wochentage = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag")
print(wochentage)
```

## Lösung zu Aufgabe 2: Zugriff auf Tupellemente
```python
for tag in wochentage:
    print(tag)
```

## Lösung zu Aufgabe 3: Tupel verändern (nicht möglich)
# Versuche, das zweite Element des Tupels zu ändern (Hinweis: Tupel sind unveränderlich).

## Lösung zu Aufgabe 4: Tupellänge
```python
länge = len(wochentage)
print(f"Das Tupel hat {länge} Elemente.")
```

## Lösung zu Aufgabe 5: Elemente hinzufügen (nicht möglich)
# Versuche, ein neues Element zum Tupel hinzuzufügen (Hinweis: Tupel sind unveränderlich).
# Lösungsblatt für Notebook 7: Dictionaries in Python

## Lösung zu Aufgabe 1: Erstellen eines Dictionaries
```python
personen = {"Alice": 30, "Bob": 25, "Eve": 28}
print(personen)
```

## Lösung zu Aufgabe 2: Zugriff auf Dictionary-Werte
# Iteriere über das Dictionary und gib sowohl Schlüssel als auch Werte aus.
```python
for name, alter in personen.items():
    print(f"{name}: {alter} Jahre alt")
```

## Lösung zu Aufgabe 3: Dictionary verändern
```python
personen["Alice"] = 32
print(personen)
```

## Lösung zu Aufgabe 4: Dictionarylänge
```python
anzahl_personen = len(personen)
print(f"Das Dictionary hat {anzahl_personen} Einträge.")
```

## Lösung zu Aufgabe 5: Elemente hinzufügen
```python
personen["Charlie"] = 22
print(personen)
```

# Lösungsblatt für das Übungsnotebook: Vertiefung von `for`-Schleifen mit Datenstrukturen

#### Lösung zu Übung 1: Listen und `range`

`range` wird verwendet, um eine Sequenz von Zahlen zu generieren. In dieser Aufgabe verwenden wir `range(1, 11)`, um eine Sequenz von 1 bis 10 zu erstellen, und berechnen die Quadratzahlen.

```python
for zahl in range(1, 11):
    quadrat = zahl ** 2
    print(f"Die Quadratzahl von {zahl} ist {quadrat}.")
```

#### Lösung zu Übung 2: Listen und `enumerate`

`enumerate` gibt sowohl den Index als auch den Wert eines Elements in einer Sequenz zurück. In dieser Aufgabe verwenden wir `enumerate`, um den Index und das Tier auszugeben.

```python
tiere = ["Hund", "Katze", "Pferd"]
for index, tier in enumerate(tiere):
    print(f"Tier {index + 1}: {tier}")
```

#### Lösung zu Übung 3: Tupel und `enumerate`

`enumerate` funktioniert genauso mit Tupeln. In dieser Aufgabe verwenden wir ein Tupel von Obstsorten und `enumerate`.

```python
obstsorten = ("Apfel", "Banane", "Orange")
for index, obst in enumerate(obstsorten):
    print(f"Obst {index + 1}: {obst}")
```

#### Lösung zu Übung 4: Dictionaries und `items`

`items` gibt sowohl Schlüssel als auch Werte aus einem Dictionary zurück. In dieser Aufgabe verwenden wir `items`, um das Land und die Hauptstadt auszugeben.

```python
laender_hauptstaedte = {"Deutschland": "Berlin", "Frankreich": "Paris", "Italien": "Rom"}
for land, hauptstadt in laender_hauptstaedte.items():
    print(f"Das Land {land} hat die Hauptstadt {hauptstadt}.")
```

#### Lösung zu Übung 5: Listen und `zip`

`zip` kombiniert Elemente aus mehreren Sequenzen paarweise. In dieser Aufgabe verwenden wir `zip`, um vollständige Namen aus Vor- und Nachnamen zu erstellen.

```python
vornamen = ["Alice", "Bob", "Eve"]
nachnamen = ["Smith", "Johnson", "Brown"]
for vorname, nachname in zip(vornamen, nachnamen):
    voller_name = f"{vorname} {nachname}"
    print(voller_name)
```

#### Lösung zu Übung 6: Dictionaries und `values`

`values` gibt alle Werte aus einem Dictionary zurück. In dieser Aufgabe verwenden wir `values`, um nur die Preise auszugeben.

```python
produkte_preise = {"Apfel": 0.5, "Banane": 0.25, "Orange": 0.75}
for preis in produkte_preise.values():
    print(f"Preis: {preis} Euro")
```

#### Lösung zu Übung 7: Listen und `break`

`break` wird verwendet, um eine Schleife vorzeitig zu beenden. In dieser Aufgabe verwenden wir `break`, um aus der Schleife auszubrechen, wenn eine gerade Zahl gefunden wird.

```python
zahlen = [1, 3, 5, 7, 9]
for zahl in zahlen:
    if zahl % 2 == 0:
        print(f"Gerade Zahl gefunden: {zahl}")
        break
```

#### Lösung zu Übung 8: Listen und `continue`

`continue` wird verwendet, um den aktuellen Schleifendurchlauf zu überspringen. In dieser Aufgabe verwenden wir `continue`, um die Ausgabe zu überspringen, wenn die Zahl gerade ist.

```python
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    if zahl % 2 == 0:
        continue
    print(f"Ungerade Zahl gefunden: {zahl}")
```