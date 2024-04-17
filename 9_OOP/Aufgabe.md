# Einleitung
Du bist nun ein Spiele  Entwickler und sollst deine Teamkollegen beim Entwickeln eines 2D Spieles helfen.
Deine Aufgabe ist es deinem Team das Programmieren des Spielers abzunehmen.
Dazu müssen folgende Sachen implementiert werden.
# Position
Schreibe eine Klasse  `Position` welche zum speichern der von Koordinaten benutzt wird.
Die Klasse besitzt 2 Attribute: `X` und `Y` welche beide integer sind.
# Player
In dieser Aufgabe wird der tatsächliche Spieler implementiert.
## a)
Schreibe eine Klasse `Player`, welche den Spieler auf dem Spielfeld darstellen soll.

## b)
Der Spieler besitzt:
- `Namen` beschreibt, wie der Spieler heißt
- `Klasse` der Spieler ist (Magier, Tank, Bandit)
- `Schaden` welches den Schaden beschreibt, den der Spieler austeilen kann
- `Position` beschreibt die Koordinaten, wo sich der Spieler befindet. Benutze hierzu die Klasse `Position` aus der vorigen Aufgabe
- `LP` beschreibt die Lebenspunkte die der Spieler besitzt.

## c)
Der Spieler soll folgende Aktionen können:
- `get_damage` Fügt dem Spieler den angegebenen Schaden zu
- `move` bewegt den Spieler zu der angegebenen Position