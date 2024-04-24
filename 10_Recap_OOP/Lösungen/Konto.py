class Konto:
    def __init__(self, kontonummer: str, kontostand: float, inhaber: str) -> None:
        """
        Initialisiert ein Konto-Objekt mit Kontonummer, Kontostand und Inhaber.

        Args:
            kontonummer (str): Die Kontonummer des Kontos.
            kontostand (float): Der aktuelle Kontostand des Kontos.
            inhaber (str): Der Inhaber des Kontos.
        """
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.inhaber = inhaber

    def einzahlen(self, betrag: float) -> None:
        """
        Führt eine Einzahlung auf das Konto durch.

        Args:
            betrag (float): Der einzuzahlende Betrag.
        """
        self.kontostand += betrag

    def abheben(self, betrag: float) -> None:
        """
        Führt eine Abhebung vom Konto durch.

        Args:
            betrag (float): Der abzuhebende Betrag.
        """
        if self.kontostand >= betrag:
            self.kontostand -= betrag
            return True
        else:
            print("Nicht genug Geld auf dem Konto.")
            return False