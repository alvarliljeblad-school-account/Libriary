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
        return f"{self.titel} av {self.författare}."

    # Läser en rad i textfilen och returnerar en bok
    def bokFrånFilSträng(sträng):
        sträng_delar = sträng.split(",")
        return Bok(sträng_delar[1],sträng_delar[0],int(sträng_delar[2]), bool(int(sträng_delar[3])))
    
    # Returnerar en sträng som ska skrivas till fil för boken
    def bokTillFilSträng(self):
        return f"{self.titel},{self.författare},{self.årtal},{int(self.utlånad)}"
        
        