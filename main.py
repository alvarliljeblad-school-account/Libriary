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
    def __init__(self, författare, titel, årtal, utlånad = False):
        self.titel = titel
        self.författare = författare
        self.årtal = årtal
        self.utlånad = utlånad

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Boken {self.titel}, skriven av {self.författare}."

    # Läser en rad i textfilen och returnerar en bok
    def bokFrånFilSträng(sträng):
        sträng_delar = sträng.split(",")
        return Bok(sträng_delar[1],sträng_delar[0],sträng_delar[2], bool(int(sträng_delar[3])))
    
    # Returnerar en sträng som ska skrivas till fil för boken
    def bokTillFilSträng(self):
        return f"{self.titel},{self.författare},{self.årtal},{int(self.utlånad)}"
        
        

class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self, bokLista):
        self.böcker:list = bokLista
    
    # Öppnar en fil til biblioteket
    def öppna(self, filename):
        #Läs filen till en lista med rader
        with open(filename, "r")as fil:
            rader = fil.readlines()
        
        # Skapa en boklista
        boklista = []

        # För varje rad i filen läs in den som en bok till boklistan
        for rad in rader:
            rad.strip()
            boklista.append(Bok.bokFrånFilSträng(rad))
        
        # Sätt bibliotekets böcker till boklistan
        self.böcker = boklista


    # Sparar hela bibliotekskatalogen i en fil.
    def spara(self, filename):
        # Skapa en lista för alla rader i filen
        rader = []

        # Lägg till en sträng för alla böcker i listan av rader
        for bok in self.böcker:
            rader.append(bok.bokTillFilSträng())

        # Skriv raderna till filen
        with open(filename,"w") as fil:
            fil.writelines(rader)

    # Söker på en titel. Returnerar bokens index
    def hittaTitel(self, titel):
        for i, bok in enumerate(self.böcker):
            if bok.titel == titel:
                return i

    # Söker på en författare. Returnerar bokens index
    def hittaFörfattare(self, författare):
        for i, bok in enumerate(self.böcker):
            if bok.författare == författare:
                return i

    # Lånar en bok.
    def lånaBok(self, bok_index):
        self.böcker[bok_index].utlånad = True

    # Återlämnar en bok.
    def lämnaTillbaka(self, bok_index):
        self.böcker[bok_index].utlånad = False

    # Lägger till en ny bok:
    def läggTill(self, bok):
        self.böcker.append(bok)

    # Tar bort en bok:
    def taBort(self, bok):
        self.böcker.remove(bok)

    # Returnerar en lista över alla böcker:
    def listaBöcker(self):
        return self.böcker
    
    # Sorterar listan med böcker efter en nyckel
    def sorteraBöcker(self,nyckel):
        if nyckel == "årtal":
            self.böcker.sort(key=lambda bok: bok.årtal)
        elif nyckel == "titel":
            self.böcker.sort(key=lambda bok: bok.titel)
        elif nyckel == "författare":
            self.böcker.sort(key=lambda bok: bok.författare)

# ------------------------- Användarfunktioner -----------------------------#

# Söker ett bibliotek efter en titel 
def sök_efter_titel(bibliotek):
    pass

# Söker ett bibliotek efter författare
def sök_efter_författare(bibliotek):
    pass

# Låna en bok i ett bibliotek
def låna_bok(bibliotek):
    pass

# Lämna tillbaks en utånad bok
def återlämna_bok(bibliotek):
    pass

# Lägger till en ny bok i ett bibliotek
def lägg_till_bok(bibliotek):
    print("Vad är bokens titel?")
    titel = input("->")
    print("Vem är bokens författare?")
    författare = input("->")
    print("Vilket år publicerades boken?")
    årtal = input("->")
    ny_bok = Bok(författare,titel,årtal)
    bibliotek.läggTill(ny_bok)

# Tar bort en bok ut ett bibliotek
def ta_bort_bok(bibliotek):
    pass

# Listar alla böcker i ett bibliotek
def lista_böcker(bibliotek):
    pass

# Sorterar böckerna i ett bibliotek
def sortera_böcker(bibliotek):
    pass 



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