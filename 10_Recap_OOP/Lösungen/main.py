from Bank import Bank

# Erstelle eine neue Instanz der Bank-Klasse
sparkasse = Bank()

# Erstelle ein neues Bankkonto für Bill Gates mit einem anfänglichen Guthaben von 999.9
sparkasse.neues_konto_erstellen(0, 999.9, "Bill Gates")

# Erstelle ein neues Bankkonto für eine durchschnittliche Person mit einem anfänglichen Guthaben von 10.0
sparkasse.neues_konto_erstellen(1, 10.0, "Armer Mensch")

# Print the account balance for Bill Gates
print(f"Bill Gates hat {sparkasse.kontostand_abfragen(0)}€")

# Print the account balance for the average person
print(f"Armer Mensch hat {sparkasse.kontostand_abfragen(1)}€")
sparkasse.geld_ueberweisen(0, 1, 100.0)

print(f"Bill Gates hat {sparkasse.kontostand_abfragen(0)}€")
print(f"Armer Mensch hat {sparkasse.kontostand_abfragen(1)}€")