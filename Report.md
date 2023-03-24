# UITLEG OVER DE OPZET VAN DE CODE

De opdracht was zeer uitdagend en heeft mij velen uren gekost, maar ik ben trots op het eindresultaat! Hieronder geef ik een toelichting op de naar mijn idee waardevolle elementen en zal ik ze daarna verder uitleggen. De volgende 3 elementen vind ik zelf zeer waardenvol in deze CL toepassing:

> - het structuren van de code in verschillende files en folders
> - het zoveel als mogelijk toepassen van DRY en het hergebruiken van functies
> - het concept tijd heb ik dusdanig verwerkt, dat de CL toepassing de mogelijkheid heeft om op verschillende datums de dan aanwezige voorraad te tonen, rekeninghoudend met de vervaldatum die gold op die betreffende datum voor dat betreffende product. Daarnaast kunnen er rapporten gedraaid worden in daten, maanden en jaren.

### _files en folders_

Ik heb de code uitgewerkt in verschillende files. Zo is er overzicht in waar welke code staat en wat deze doet. Dit bevorderd de leesbaarheid en heeft mij geholpen om te debuggen.

De CL start op in de `Main()` en deze bevindt zich in de 'superpy.py' file. Vanuit hier wordt bekeken of de folders en csv-files die gerbuikt worden al aanwezig zijn of dat deze aangemaakt moeten worden. Voor nu zit er dummy data in de csv files. Als je folder met files delete en je start opnieuw de 'superpy.py' op, dan maakt hij lege bestanden aan. Daarnaast checkt hij of direct en alleen de 'superpy.py' aangeroepen wordt of ook al een comment met argumenten. Dit bepaald welke markdown er ingelezen wordt. Als laatst wordt hier de args.parser geactiveerd. Vanuit hier wordt gekeken welke modulen er opgevraagd wordt via de CL. Deze check vind plaats in de 'proces_logic.py':

```code
def proces_args(args):
    # SET INPUT PRODUCTS
    if args.command == "products":
        products(args)

    # SET INPUT BUY
    if args.command == "buy":
        buy(args)

    # SET INPUT SELL
    if args.command == "sell":
        sell(args)

    # SET INPUT REPORTS
    if args.command == "report":
        report(args)

    # SET INPUT INVENTORY
    if args.command == "inventory":
        inventory(args)
```

Hierna roept hij de daadwerkelijk functie aan om uit te voerne op basis van de comments. Het is een soort kapstok.

Ik heb verder onderscheid gemaakt naar code die helpen om de eindfunctie uit te voeren (alle logic files). In de args_functions map zitten de daadwerkelijke functies zoels hierboven beschreven.

### _hergebruiken van functies_

<>

### _tijd_

<>
