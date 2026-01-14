from bok import Bok
# Söker ett bibliotek efter en titel 
def sök_efter_titel(bibliotek):
    print("Vilken bok söker du efter?")
    inp = input("->")
    bok_index, bok = bibliotek.hittaTitel(inp)
    if bok != None:
        if bok.utlånad:
            print(f"{bok} är för nuvarande utlånad")
        else: 
            print(f"{bok} finns inne, vill då låna den?(y/n)")
            inp = ""
            while inp not in ["y","n"]:
                inp = input("->").lower()
            if inp == "y":
                bibliotek.lånaBok(bok_index)
                print(f"Du har lånat {bok}")
            else:
                print("Du lånade inte boken")            
    else:
        print("Det finns ingen bok med den titeln på det här biblioteket")
    input("Tryck enter för att fortsätta")
        

# Söker ett bibliotek efter författare
def sök_efter_författare(bibliotek):
    print("Vilken författares böcker söker du efter?")
    inp = input("->")
    böcker = bibliotek.hittaFörfattare(inp)
    if len(böcker) == 0:
        print(f"Biblioteket har inga böcker som är skrivna av {inp}")
    else:
        print(f"Just nu har biblioteket följande böcker av {inp}")
        for bok in böcker:
            print(f"  -{bok}")
    input("Tryck enter för att fortsätta")


# Låna en bok i ett bibliotek
def låna_bok(bibliotek):
    print("Vilken bok vill du låna?")
    print("Ange titeln")
    inp = input("->")
    bok_index, bok = bibliotek.hittaTitel(inp)
    if bok != None:
        if bok.utlånad:
            print(f"{bok} är för nuvarande utlånad")
        else: 
            print(f"{bok} finns inne, vill då låna den?(y/n)")
            inp = ""
            while inp not in ["y","n"]:
                inp = input("->").lower()
            if inp == "y":
                bibliotek.lånaBok(bok_index)
                print(f"Du har lånat {bok}")
            else:
                print("Du lånade inte boken")            
    else:
        print("Det finns ingen bok med den titeln på det här biblioteket")
    input("Tryck enter för att fortsätta")

# Lämna tillbaks en utånad bok
def återlämna_bok(bibliotek):
    print("Vilken bok vill du lämna tillbaka?")
    print("Ange titeln")
    inp = input("->")
    bok_index, bok = bibliotek.hittaTitel(inp)
    if bok != None:
        if not bok.utlånad:
            print(f"{bok} är finn junt nu inne på biblioteket")
        else: 
            print(f"{bok} är utlånad, vill då lämna tillbaka den?(y/n)")
            inp = ""
            while inp not in ["y","n"]:
                inp = input("->").lower()
            if inp == "y":
                bibliotek.lämnaTillbaka(bok_index)
                print(f"Du har lånat {bok}")
            else:
                print("Du lämnade inte tillbaka boken")
    else:
        print("Det finns ingen bok med den titeln på det här biblioteket")
    input("Tryck enter för att fortsätta")

# Lägger till en ny bok i ett bibliotek
def lägg_till_bok(bibliotek):
    print("Vad är bokens titel?")
    titel = input("->")
    print("Vem är bokens författare?")
    författare = input("->")
    print("Vilket år publicerades boken?")
    # Om ett en inkorekt årtal skrivs in fråga igen tills ett korrekt årtal skrivs in
    while True:
        årtal = input("->")
        try:
            årtal = int(årtal)
        except:
            print("Skriv in ett korekt årtal")
        else:
            break
    ny_bok = Bok(författare,titel,årtal)
    bibliotek.läggTill(ny_bok)
    print(f"{ny_bok} har lagts till i biblioteket")
    input("Tryck enter för att fortsätta")

# Tar bort en bok ut ett bibliotek
def ta_bort_bok(bibliotek):
    print("Vilken bok vill du ta bort?")
    print("Ange titeln")
    inp = input("->")
    bok_index, bok = bibliotek.hittaTitel(inp)
    if bok != None:
        print("Är du säker att du vill ta bort boken?(y/n)")
        inp = ""
        while inp not in ["y","n"]:
            inp = input("->").lower()
        if inp == "y":
            bibliotek.lämnaTillbaka(bok_index)
            print(f"Du har lånat {bok}")
    else:
        print("Det finns ingen bok med den titeln på det här biblioteket")
    input("Tryck enter för att fortsätta")

# Listar alla böcker i ett bibliotek
def lista_böcker(bibliotek):
    böcker = bibliotek.listaBöcker()
    if len(böcker) == 0:
        print("Tyvär är biblioteket tomt för nuvarande, kom tillbaka snart")
    else:
        print("Biblioteket inehåller följande böcker")
        for bok in böcker:
            print(f"  -{bok}")
    input("Tryck enter för att fortsätta")

# Sorterar böckerna i ett bibliotek
def sortera_böcker(bibliotek):
    print("Vill du sortera efter Titel(T), Författare(F) eller Årtal(Å)")
    inp = ""
    while inp not in ["t","f","å"]:
        inp = input("->")
    if inp == "t":
        bibliotek.sorteraBöcker("titel")
    elif inp == "f":
        bibliotek.sorteraBöcker("författare")
    elif inp == "å":
        bibliotek.sorteraBöcker("årtal")
    print("Biblioteket har sorterats")
    input("Tryck enter för att fortsätta")