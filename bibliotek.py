from bok import Bok
class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self, bokLista):
        self.böcker:list = bokLista
    
    # Öppnar en fil til biblioteket
    def öppna(self, filename):
        #Läs filen till en lista med rader 
        # Om filen inte finns, skapa den
        try:
            with open(filename, "r")as fil:
                rader = fil.readlines()
        except:
            with open(filename, "x") as fil:
                pass
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

    # Söker på en titel. Returnerar bokens index och boken
    def hittaTitel(self, titel):
        for i, bok in enumerate(self.böcker):
            if bok.titel.lower() == titel.lower():
                return i, bok
        return 0, None

    # Söker på en författare. Returnerar böcker av författaren
    def hittaFörfattare(self, författare):
        böcker_av_författaren = []
        for bok in enumerate(self.böcker):
            if bok.författare.lower() == författare.lower():
                böcker_av_författaren.append(bok)
        return böcker_av_författaren

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
    def taBort(self, bok_index):
        self.böcker.pop(bok_index)

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