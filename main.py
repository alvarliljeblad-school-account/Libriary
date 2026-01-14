# ------------------------------- Information --------------------------------- #
"""
Titel: Biblioteket
Författare: Alvar Liljeblad
Datum: 2026-01-14

Det här är ett program för hantering av enklare biblioteksrutiner.
Programmet lagrar böckerna i en fil med namnet "bibliotek.txt" mellan körningarna.
"""

# -------------------------------- Importer ----------------------------------- #
from bok import Bok
from bibliotek import Bibliotek
import användarfunktioner

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    biblioteket = Bibliotek([])
    biblioteket.öppna("bibliotek.txt")

    menyVal = ""

    while menyVal != "q":

        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:

            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            5. Lägg till ny bok                                 6. Ta bort bok
            7. Lista alla böcker                                8. Sortera böcker
            q. Avsluta

        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            användarfunktioner.sök_efter_titel(biblioteket)
        elif menyVal == "2":
            användarfunktioner.sök_efter_författare(biblioteket)
        elif menyVal == "3":
            användarfunktioner.låna_bok(biblioteket)
        elif menyVal == "4":
            användarfunktioner.återlämna_bok(biblioteket)
        elif menyVal == "5":
            användarfunktioner.lägg_till_bok(biblioteket)
        elif menyVal == "6":
            användarfunktioner.ta_bort_bok(biblioteket)
        elif menyVal == "7":
            användarfunktioner.lista_böcker(biblioteket)
        elif menyVal == "8":
            användarfunktioner.sortera_böcker(biblioteket)
    
    # När programmet är slut spara till filen
    biblioteket.spara("bibliotek.txt")


print(
"""
                                   .--.                   .---.
                               .---|__|           .-.     |~~~|
                            .--|===|--|_          |_|     |~~~|--.--.
                            |  |===|  |'\     .---!~|  .--|   |--|--|
                            |%%|   |  |.'\    |===| |--|%%|   |  |  |
                            |%%|   |  |\.'\   |   | |__|  |   |  |  |
                            |B | I |B | \L \  |=I=|O|T=|E | K |E |T |
                            |  |   |__|  \.'\ |   |_|__|  |~~~|__|__|
                            |  |===|--|   \.'\|===|~|--|%%|~~~|--|--|
                            ^--^---'--^    `-'`---^-^--^--^---'--'--'
""")

main()