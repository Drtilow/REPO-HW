import sys
# Seznam na uložení záznamů
zaznamy = []
# Hlavní smyčka aplikace
while True:
    # Zobrazení menu
    print("\nMenu:")
    print("1. Přidat nový záznam")
    print("2. Zobrazit existující záznamy")
    print("3. Vyhledat záznam podle klíčového slova")
    print("4. Ukončit aplikaci")
    volba = input("Vyberte možnost: ")

    # Přidání nového záznamu
    if volba == '1':
        jmeno = input("Zadejte jméno studenta: ")
        trida = input("Zadejte třídu studenta: ")
        zaznamy.append((jmeno, trida))
        print("Záznam byl přidán.")

    # Zobrazení existujících záznamů

    # Vyhledání záznamu podle klíčového slova

    # Ukončení aplikace

    # Neplatná volba