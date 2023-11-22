def calculate_average(fächer: dict) -> None:
    """
    Calculates the average grade for each subject based on the given grades and weights.

    Args:
        fächer (dict): A dictionary containing the subjects as keys and their corresponding grades and weights as values.

    Returns:
        None
    """
    for fach in fächer:
        noten = fächer[fach]["noten"]
        gewichtungen = fächer[fach]["gewichtungen"]
        noten_gewichtet = []
        for i, notentyp in enumerate(noten):
            noten_summe = sum(noten[notentyp])
            note_typ_schnitt = noten_summe / len(noten[notentyp])
            noten_gewichtet.append(note_typ_schnitt * float(gewichtungen[i]))
        durchschnittsnote = sum(noten_gewichtet)
        fächer[fach]["durchschnittsnote"] = durchschnittsnote

def calculate_overall_average(fächer):
    """
    Calculates the overall average of the given subjects.

    Args:
        fächer (dict): A dictionary containing the subjects and their average grades.

    Returns:
        float: The overall average grade.
    """
    gesamtnote = sum([fächer[fach]["durchschnittsnote"] for fach in fächer]) / len(fächer)
    return gesamtnote
