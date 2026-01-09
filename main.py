# ------------------------------- Information --------------------------------- #
"""
Titel: Biblioteket
Författare:
Datum:

Det här är ett program för hantering av enklare biblioteksrutiner.
Programmet lagrar böckerna i en fil med namnet "bibliotek.txt" mellan körningarna.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand

# ---------------------------- Klassdefinitioner ------------------------------ #

class Bok:
    """ Bok är en klass som representerar en bok i biblioteket. Varje objekt
    som skapas ur klassen har en titel, författare och en variabel som håller
    reda på om boken är utlånad eller inte. """
    def __init__(self, författare, titel, utlånad = False):
        self.titel = titel
        self.författare = författare
        self.utlånad = utlånad

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Boken {self.titel}, skriven av {self.författare}."

    # Läser en rad i textfilen och returnerar en bok
    def bok_från_sträng(sträng):
        sträng_delar = sträng.split(",")
        return Bok(sträng_delar[1],sträng_delar[0], bool(int(sträng_delar[2])))
    
    # Returnerar en sträng som ska skrivas till fil för boken
    def bok_till_fil_sträng(self):
        return f"{self.titel},{self.författare},{int(self.utlånad)}"
        
        

class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self, bokLista):
        self.böcker = bokLista
    
    # Öppnar en fil til biblioteket
    def öppna(self, filename):
        return

    # Sparar hela bibliotekskatalogen i en fil.
    def spara(self, filename):
        rader = []
        for bok in self.böcker:
            rader.append()


        with open(filename,"w") as fil:
            fil.writelines()

    # Söker på en titel.
    def hittaTitel(self, titel):
        return 

    # Söker på en författare.
    def hittaFörfattare(self, författare):
        return

    # Lånar en bok.
    def lånaBok(self, bok):
        return

    # Återlämnar en bok.
    def lämnaTillbaka(self, bok):
        return

    # Lägger till en ny bok:
    def läggTill(self, bok):
        return

    # Tar bort en bok:
    def taBort(self, bok):
        return

    # Returnerar en lista över alla böcker:
    def listaBöcker(self):
        return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:

            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            4. Lägg till ny bok                                 5. Ta bort bok
            6. Ta bort bok                                      7. Lista alla böcker
            8. Sortera böcker                                   q. Avsluta

        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            pass
        elif menyVal == "2":
            pass
        elif menyVal == "3":
            pass
        elif menyVal == "4":
            pass
        elif menyVal == "5":
            pass
        elif menyVal == "6":
            pass
        elif menyVal == "7":
            pass
        elif menyVal == "8":
            pass

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