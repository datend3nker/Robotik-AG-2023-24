# OOP Übungsaufgabe: Konto und Bank

In dieser Übung werdet ihr eine Klasse `Konto` erstellen, die einige grundlegende Attribute und Methoden eines Bankkontos repräsentiert. Anschließend werdet ihr eine Klasse `Bank` erstellen, die mit Instanzen der Klasse `Konto` arbeitet.

### Konto-Klasse

Erstelle eine Klasse namens `Konto`. Ein Konto soll folgende Attribute haben:

- `kontonummer`: Eine eindeutige Kontonummer (als Integer)
- `kontostand`: Der aktuelle Kontostand (als Float)
- `inhaber`: Der Name des Kontoinhabers (als String)

Die Klasse soll folgende Methoden haben:

- `__init__(self, kontonummer, kontostand, inhaber)`: Ein Konstruktor, der die Attribute `kontonummer`, `kontostand` und `inhaber` initialisiert.
- `einzahlen(self, betrag)`: Eine Methode, die einen Betrag zum Kontostand addiert.
- `abheben(self, betrag)`: Eine Methode, die einen Betrag vom Kontostand abzieht, wenn ausreichend Geld vorhanden ist.

### Bank-Klasse

Erstelle eine Klasse namens `Bank`, die eine Liste von Konten verwaltet. Die Klasse soll folgende Methoden haben:

- `__init__(self)`: Ein Konstruktor, der eine leere Liste `konten` initialisiert.
- `neues_konto_erstellen(self, kontonummer, kontostand, inhaber)`: Eine Methode, die ein neues Konto erstellt und es der Liste `konten` hinzufügt.
- `kontostand_abfragen(self, kontonummer)`: Eine Methode, die den Kontostand für eine bestimmte Kontonummer zurückgibt.
- `geld_einzahlen(self, kontonummer, betrag)`: Eine Methode, die Geld auf das Konto mit der angegebenen Kontonummer einzahlt.
- `geld_abheben(self, kontonummer, betrag)`: Eine Methode, die Geld von dem Konto mit der angegebenen Kontonummer abhebt.
-`geld_ueberweisen(self, kontonummer1, kontonummer2, betrag)`: Eine Methode, die den angegebenen Betrag von konto1 zu konto2 überträgt 

### Hinweise

- Verwende geeignete Datentypen für die Attribute und Parameter.
- Denke daran, Methoden zu verwenden, um auf die Attribute zuzugreifen und sie zu verändern.
- Stelle sicher, dass deine Methoden angemessene Fehlerbehandlung enthalten, z. B. überprüfen, ob ausreichend Geld vorhanden ist, um einen Betrag abzuheben.

Viel Spaß beim Programmieren!
