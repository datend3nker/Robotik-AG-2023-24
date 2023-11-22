def get_subjects_and_grades(fächer: dict = {})-> dict:
    """
    Diese Funktion fordert den Benutzer auf, die Anzahl der Fächer, ihre Namen, Notentypen und Gewichtungen einzugeben.
    Diese Informationen werden dann in einem Wörterbuch gespeichert und zurückgegeben.

    Args:
        fächer (int, optional): Die Anzahl der Fächer. Standardmäßig None.

    Returns:
        dict: Ein Wörterbuch, das die Informationen über die Fächer, Noten und Gewichtungen enthält.
    """
    if fächer != {}:
        for fach in fächer:
            print(f"Das Fach {fach} hat folgende Notentypen: {fächer[fach]['notentypen']}")
            print(f"Das Fach {fach} hat folgende Gewichtungen: {fächer[fach]['gewichtungen']}")

            for notentyp in fächer[fach]["noten"]:
                print(f"Das Fach {fach} hat folgende Noten: {fächer[fach]['noten'][notentyp]}")

                zusätzliche_noten = input(f"Geben Sie zusätzliche Noten für {notentyp} ein (durch Kommas getrennt): ").split(",")
                if zusätzliche_noten != [""]:
                    fächer[fach]["noten"][notentyp].extend([float(note) for note in zusätzliche_noten])

    else:
        anzahl_faecher = int(input("Geben Sie die Anzahl der Fächer ein: "))  # Fordere den Benutzer auf, die Anzahl der Fächer einzugeben

        for i in range(anzahl_faecher):
            fach = input(f"Geben Sie den Namen von Fach {i+1} ein: ")  # Fordere den Benutzer auf, den Namen jedes Fachs einzugeben
            notentypen = input(f"Geben Sie die Notentypen für {fach} ein (durch Kommas getrennt): ").split(",")
            gewichtungen = input(f"Geben Sie die Gewichtungen für {fach} ein (durch Kommas getrennt): ").split(",")
            fächer[fach] = {"notentypen": notentypen, "gewichtungen": gewichtungen, "noten": {}}  # Füge das Fach dem Wörterbuch hinzu

            for notentyp in notentypen:
                noten = input(f"Geben Sie {notentyp} Noten ein (durch Kommas getrennt): ").split(",")
                fächer[fach]["noten"][notentyp] = [float(note) for note in noten]
            
    return fächer

def print_subject_grades(fächer):
    """
    Prints the subject grades along with their average scores.

    Args:
        fächer (dict): A dictionary containing the subject names as keys and their respective grades as values.

    Returns:
        None
    """
    print("Fach\t\tDurchschnittsnote")
    print("---------------------------")
    for fach in fächer:
        print(f"{fach}\t\t{fächer[fach]['durchschnittsnote']}")
