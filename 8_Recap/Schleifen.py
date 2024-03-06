def weihnachtsbaum(hoehe: int) -> None:
    """
    Prints a Christmas tree of the given height.

    Parameters:
    - hoehe (int): The height of the Christmas tree.

    Returns:
    - None
    """
    raise NotImplementedError("Implementiere die Funktion")

######################

arbeitsstunden_pro_woche = {
    'Montag': 8,
    'Dienstag': 7,
    'Mittwoch': 8,
    'Donnerstag': 6,
    'Freitag': 9,
    'Samstag': 5,
    'Sonntag': 0  # Der Schüler hat am Sonntag nicht gearbeitet
}

# a) Berechne die Gesamtarbeitsstunden f¨ur die Woche
def arbeitsstunden_gesammt(arbeitsstunden: dict) -> int:
    """
    Returns the total amount of working hours in a week.

    Parameters:
    - arbeitsstunden (dict): A dictionary with the days of the week as keys and the amount of working hours as values.

    Returns:
    - int: The total amount of working hours in a week.

    Examples:
        >>> arbeitsstunden_gesammt(arbeitsstunden_pro_woche)
        43
    """
    raise NotImplementedError("Implementiere die Funktion")


# b)Überprüfe, an welchem Tag die meisten Stunden gearbeitet wurden.
def tag_mit_den_meisten_stunden(arbeitsstunden: dict) -> str:
    """
    Returns the day with the most working hours.

    Parameters:
    - arbeitsstunden (dict): A dictionary with the days of the week as keys and the amount of working hours as values.

    Returns:
    - str: The day with the most working hours.

    Examples:
        >>> tag_mit_den_meisten_stunden(arbeitsstunden_pro_woche)
        'Freitag'
    """
    raise NotImplementedError("Implementiere die Funktion")


# Überprüfe, ob der Schüler an jedem Tag mindestens 6 Stunden gearbeitet hat. Wenn ja, gib eine Nachricht aus, dass die Woche erfolgreich war, sonst eine Nachricht des Bedauerns.
def erfolgreiche_woche(arbeitsstunden: dict) -> bool:
    """
    Returns a message if the student worked at least 6 hours every day.

    Parameters:
    - arbeitsstunden (dict): A dictionary with the days of the week as keys and the amount of working hours as values.

    Returns:
    - str: A message if the student worked at least 6 hours every day.

    Examples:
        >>> erfolgreiche_woche(arbeitsstunden_pro_woche)
        true
    """
    raise NotImplementedError("Implementiere die Funktion")


# d) Erstelle ein neues Dictionary, das die Arbeitsstunden pro Tag in Minuten enthält, wobei angenommen wird, dass 1 Stunde gleich 60 Minuten ist.
def arbeitsstunden_in_minuten(arbeitsstunden: dict) -> dict:
    """
    Returns a new dictionary with the working hours per day in minutes.

    Parameters:
    - arbeitsstunden (dict): A dictionary with the days of the week as keys and the amount of working hours as values.

    Returns:
    - dict: A new dictionary with the working hours per day in minutes.

    Examples:
        >>> arbeitsstunden_in_minuten(arbeitsstunden_pro_woche)
        {'Montag': 480, 'Dienstag': 420, 'Mittwoch': 480, 'Donnerstag': 360, 'Freitag': 540, 'Samstag': 300, 'Sonntag': 0}
    """
    raise NotImplementedError("Implementiere die Funktion")


# e) Füge einen neuen Arbeitstag hinzu und weise ihm 8 Stunden zu.
def neuer_arbeitstag(arbeitsstunden: dict, tag: str, stunden: int) -> dict:
    """
    Adds a new working day to the dictionary.

    Parameters:
    - arbeitsstunden (dict): A dictionary with the days of the week as keys and the amount of working hours as values.
    - tag (str): The day of the week.
    - stunden (int): The amount of working hours.

    Returns:
    - dict: A new dictionary with the new working day.

    Examples:
        >>> neuer_arbeitstag(arbeitsstunden_pro_woche, 'Montag', 8)
        {'Montag': 8, 'Dienstag': 7, 'Mittwoch': 8, 'Donnerstag': 6, 'Freitag': 9, 'Samstag': 5, 'Sonntag': 0, 'NeuerTag': 8}
    """
    raise NotImplementedError("Implementiere die Funktion")