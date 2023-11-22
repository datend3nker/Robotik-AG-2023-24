from Noten_berechnen_mathe import calculate_average, calculate_overall_average
from Noten_berechnen_user import get_subjects_and_grades, print_subject_grades
from Noten_berechnen_datei import save_subjects, load_subjects


# Schritt 1: Erstelle ein Wörterbuch, um Fächer und Noten zu speichern
fächer = load_subjects("fächer.pickle")  # Load subjects from file


if fächer is None:
    fächer = get_subjects_and_grades()
else:
    wahl = input("Möchten Sie weitere noten hinzufügen? (j/n) ")
    if wahl == "j":
        fächer = get_subjects_and_grades(fächer)

# Schritt 3: Berechne den gewichteten Durchschnitt für jedes Fach
calculate_average(fächer)

# Schritt 4: Tabelle der Fachnoten ausgeben
print_subject_grades(fächer)

# Schritt 5: Gesamtnote berechnen
gesamtnote = calculate_overall_average(fächer)
# Schritt 7: Gesamtnote ausgeben
print(f"\nGesamtnote: {gesamtnote}")

# Schritt 8: Fächer speichern
save_subjects(fächer, "fächer.pickle")

