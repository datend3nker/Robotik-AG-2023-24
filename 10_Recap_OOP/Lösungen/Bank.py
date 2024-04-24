from Konto import Konto

class Bank:
    def __init__(self):
        self.konten = []

    def neues_konto_erstellen(self, kontonummer: int, kontostand: float, inhaber: str) -> None:
        """
        Erstellt ein neues Konto und fügt es der Bank hinzu.

        Args:
            kontonummer (int): Die Kontonummer des neuen Kontos.
            kontostand (float): Der Anfangskontostand des neuen Kontos.
            inhaber (str): Der Inhaber des neuen Kontos.
        """
        konto = Konto(kontonummer, kontostand, inhaber)
        self.konten.append(konto)

    def kontostand_abfragen(self, kontonummer: int) -> float:
        """
        Ruft den Kontostand für das angegebene Konto ab.

        Args:
            kontonummer (int): Die Kontonummer des Kontos.

        Returns:
            float: Der Kontostand des Kontos. Wenn das Konto nicht gefunden wird, wird None zurückgegeben.
        """
        for konto in self.konten:
            if konto.kontonummer == kontonummer:
                return konto.kontostand
        return None

    def geld_einzahlen(self, kontonummer: int, betrag: float) -> bool:
        """
        Zahlt den angegebenen Betrag auf das angegebene Konto ein.

        Args:
            kontonummer (int): Die Kontonummer des Kontos.
            betrag (float): Der einzuzahlende Betrag.

        Returns:
            bool: True, wenn die Einzahlung erfolgreich war. False, wenn das Konto nicht gefunden wurde.
        """
        for konto in self.konten:
            if konto.kontonummer == kontonummer:
                konto.einzahlen(betrag)
                return True
        return False

    def geld_abheben(self, kontonummer: int, betrag: float) -> bool:
        """
        Hebt den angegebenen Betrag vom angegebenen Konto ab.

        Args:
            kontonummer (int): Die Kontonummer des Kontos.
            betrag (float): Der abzuhebende Betrag.

        Returns:
            bool: True, wenn die Abhebung erfolgreich war. False, wenn das Konto nicht gefunden wurde oder nicht genügend Guthaben hat.
        """
        for konto in self.konten:
            if konto.kontonummer == kontonummer:
                return konto.abheben(betrag)
        return False

    def geld_ueberweisen(self, kontonummer1: int, kontonummer2: int, betrag: float) -> bool:
        """
        Überweist den angegebenen Betrag von einem Konto auf ein anderes Konto.

        Args:
            kontonummer1 (int): Die Kontonummer des ersten Kontos.
            kontonummer2 (int): Die Kontonummer des zweiten Kontos.
            betrag (float): Der zu überweisende Betrag.

        Returns:
            bool: True, wenn die Überweisung erfolgreich war. False, wenn eines der Konten nicht gefunden wurde oder nicht genügend Guthaben hat.
        """
        k1 = object()
        k2 = object()
        for konto1 in self.konten:
            if konto1.kontonummer == kontonummer1:
                k1 = konto1
        for konto2 in self.konten:
            if konto2.kontonummer == kontonummer2:
                k2 = konto2
        if k1.abheben(betrag):
            k2.einzahlen(betrag)
            return True
        else:
            return False