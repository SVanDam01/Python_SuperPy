# UITLEG OVER DE OPZET VAN DE CODE

De opdracht was zeer uitdagend en heeft mij velen uren gekost, maar ik ben trots op het eindresultaat! Hieronder geef ik een toelichting op de naar mijn idee waardevolle elementen en zal ik ze daarna verder uitleggen. De volgende 3 elementen vind ik zelf zeer waardenvol in deze CL toepassing:

> - het structuren van de code in verschillende files en folders
> - het zoveel als mogelijk toepassen van DRY en het hergebruiken van functies
> - het concept tijd heb ik dusdanig verwerkt, dat de CL toepassing de mogelijkheid heeft om op verschillende datums de dan aanwezige voorraad te tonen, rekeninghoudend met de vervaldatum die gold op die betreffende datum voor dat betreffende product. Daarnaast kunnen er rapporten gedraaid worden in daten, maanden en jaren.

### _Files en folders_

Ik heb de code uitgewerkt in verschillende files. Zo is er overzicht in waar welke code staat en wat deze doet. Dit bevorderd de leesbaarheid en heeft mij geholpen om te debuggen.

De CL start op in de `Main()` en deze bevindt zich in de 'superpy.py' file. Vanuit hier wordt bekeken of de folders en csv-files die gerbuikt worden al aanwezig zijn of dat deze aangemaakt moeten worden. Voor nu zit er dummy data in de csv files. Als je folder met files delete en je start opnieuw de 'superpy.py' op, dan maakt hij lege bestanden aan. Daarnaast checkt hij of direct en alleen de 'superpy.py' aangeroepen wordt of ook al een comment met argumenten. Dit bepaald welke markdown er ingelezen wordt. Als laatst wordt hier de args.parser geactiveerd. Vanuit hier wordt gekeken welke modulen er opgevraagd wordt via de CL. Deze check vind plaats in de 'proces_logic.py':

```python
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

### _Hergebruiken van functies_

Ik had als doel om zoveel als mogelijk functies her te gebruiken en hierdoor slim om te gaan met het verwerken van de code. Voorbeelden hiervoor zijn:

##### Maken, lezen en schrijven van de verschillende csv files:

Voor het maken, uitlezen en schrijven van de verschillende csv files wordt dezelfde functie gebruikt. Zie bijvoorbeeld de functie voor het lezen van csv files:

```python
def read_rows(file_name):
    with open(f"{PATH_CSV}{file_name}.csv", mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
        return data
```

##### Culculatie revenue en profit:

Voor de berekening van de totalen revenue en profit wordt gebruik gemaakt van dezelfde functie:

```python
def calculation_total(date, items_list, report):
    list_total = 0
    for item in items_list:
        list_total += int(calculation_product(date, item, report))
    return round(list_total, 2)
```

##### Calculatie actuele - en historische inventaris:

Het meest trots ben ik op ondersdtaande functie. Deze functie werkt voor zowel het verwerken van de verkoop op een datum (als argumenten sell op wordt gegeven). Het zoekt naar de oudste vooraad en die gaat eerst naar 0, daarna naar de volgende net zo lang tot dat alle opgeven aantallen verkochten producten op 0 staat en het restant aan vooraad slaat hij weer op in de csv file.

```python
def actual_inventory(item, date, qty, file):
    actual_inv = file
    new_inventory = []
    keep_inventory = [i for i in actual_inv if i["product_name"]
                      != item]
    for k in keep_inventory:
        new_inventory.append(k)
    update_inventory = [i for i in actual_inv if i["product_name"]
                        == item]
    sorted_data = sorted(
        update_inventory, key=lambda id: int(id["purchase_id"]))
    qty_list = qty
    total_cost_purchase = 0
    # loop through the list of inventory untill the qty_list is 0. After each loop the amount will decr. by the amount af the row
    # of the qty of the current row is > 0 it will be added to the inventory list with the new velue. Otherwise is will be deleted.
    while qty_list > 0:
        for i in sorted_data:
            if (int(i["quantity"]) > qty_list and qty_list != 0) and (i["expiration_date"] == "" or i["expiration_date"] > date):
                cost = float(i["purchase_price"]) * qty_list
                total_cost_purchase = total_cost_purchase + cost
                new_qty = int(i["quantity"]) - qty_list
                qty_list = 0
                i["quantity"] = str(new_qty)
                new_inventory.append(i)
            elif (int(i["quantity"]) < qty_list or int(i["quantity"]) == qty_list) and (i["expiration_date"] == "" or i["expiration_date"] > date):
                cost = float(i["purchase_price"]) * int(i["quantity"])
                total_cost_purchase = total_cost_purchase + cost
                new_qty = 0
                qty_list = qty_list - int(i["quantity"])
                continue
            else:
                new_inventory.append(i)
    # return the new dict of the inventory and the mean of the cost price
    new_inventory = sorted(new_inventory, key=lambda id: id["purchase_id"])
    mean_cost_purchase = total_cost_purchase / qty
    return mean_cost_purchase, new_inventory
```

Het mooie aan deze functie is dat deze functie hergebruikt wordt bij het terugkijken in de tijd. Dezelfde argumenten worden meegegeven en het streept per verkoop regel de inventaris in de tijd af, tot de opgegeven datum. Hiermee wordt de functie volledig hergebruikt en kan de vooraad op een datum precies worden teruggehaald. Dit kan hij doen met de volgende functie:

```python
def inventory_per_date(date, item):
    sold_file = read_rows("\\sold")
    sold_items = [i for i in sold_file if i["sell_date"] <= date]
    initual_stock = sorted(
        read_rows("\\purchase"), key=lambda id: id["purchase_id"])
    created_inventory = [
        i for i in initual_stock if i["purchase_date"] <= date]
    for i in sold_items:
        callback = actual_inventory(
            i["product_name"], i["sell_date"], int(i["quantity"]), created_inventory)[1]
        created_inventory = callback
    if item != "all":
        filter_item = [
            i for i in created_inventory if i["product_name"] == item]
        created_inventory = filter_item
    return created_inventory
```

### _Tijd_

Als laatste het concept tijd. Ik heb er voor gekozen om de tijd als standaard variabele op te nemen en deze vast te zetten op 'vandaag'. Dit vond ik het meest logische als we kijken naar waarvoor de tool gebruikt wordt. Als nu een 'verkoop' wordt opgegeven is dat altijd vandaag. Alleen voor de inkoop kan worden afgeweken. De reden hiervoor is dat de vooraad anders fouten kan gaan geven. Daarnaast heb ik het concept van tijd verwerkt in de code, op zo'n manier dat financiele rapporten (revenue en profit) gedraait kunnen worden op een specifieke dag, maand of jaar. Dit doe ik door de input te checken op het juiste format:

```python
def validate_period(period_text):
    if len(period_text) == 4:
        if int(period_text) >= 2022 and int(period_text) <= 2099:
            return period_text
        else:
            print("Incorrect data format, should be YYYY (between 2022 and 2099)")
            raise Exception("Incorrect data format")
    elif len(period_text) == 7:
        if (int(period_text[:4]) >= 2022 and int(period_text[:4]) <= 2099) and (int(period_text[5:7]) > 0 and int(period_text[5:7]) < 13):
            return period_text
        else:
            print("Incorrect data format, should be YYYY-MM (between 2022 and 2099)")
            raise Exception("Incorrect data format")
    elif len(period_text) == 10:
        try:
            dt.date.fromisoformat(period_text)
            return period_text
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            raise ValueError(" ")
    else:
        print("Incorrect data format, should be YYYY-MM-DD")
        raise Exception("Incorrect data format")

# Check the input for a specific date


def validate_date(date_text):
    try:
        dt.date.fromisoformat(date_text)
        return date_text
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        raise ValueError(" ")
```

Maar daarnaast ook de input bij de rapportes om te zetten in het juiste format (is de functie die geraadpleegd wordt in de functie bij onderdeel "Culculatie revenue en profit" - `calculation_total(date, items_list, report)`):

```python
def calculation_product(date, item, report):
    data = read_rows("\\sold")
    total = 0
    if len(date) == 10:
        selections = [s[report]
                      for s in data if s["product_name"] == item and s["sell_date"] == date]
        total = sum(list(map(float, selections)))
    elif len(date) == 7:
        selections = [s[report] for s in data if s["product_name"] ==
                      item and dt.date.fromisoformat(s["sell_date"]).strftime("%Y-%m") == date]
        total = sum(list(map(float, selections)))
    elif len(date) == 4:
        selections = [s[report] for s in data if s["product_name"] ==
                      item and dt.date.fromisoformat(s["sell_date"]).strftime("%Y") == date]
        total = sum(list(map(float, selections)))
    return total
```
