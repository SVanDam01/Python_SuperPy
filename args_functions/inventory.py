# Import
import pandas as pd
from logic.business_logic import inventory_per_date
from other.settings import console
from other.settings import PATH_EXP
from rich.table import Table

# Functions for Inventory ARGS


def inventory(args):
    if args.type == "inventory":
        # Rebuild the inventory on a specific date per product or for all products
        data = inventory_per_date(args.date, args.item.lower())
        # Sort the data by id
        sorted_data = sorted(data, key=lambda id: id["purchase_id"])
        # filter on only stock that is not expired by the given date
        inventory_data = [i for i in sorted_data if (
            i["expiration_date"] == "" or i["expiration_date"] >= args.date)]
        table = Table(show_header=True, header_style="bold deep_sky_blue1")
        # Create the headers and the rows for the table in the CL
        if inventory_data != []:
            headers = inventory_data[0].keys()
            for c in headers:
                table.add_column(c)
            for r in inventory_data:
                data_per_row = r.values()
                table.add_row(*data_per_row)
        else:
            # if no data print error massage
            console.print("[red][bold]No data...[/bold][red]")
        console.print(table)
        if args.save == True and inventory_data != []:
            df = pd.DataFrame(inventory_data)
            df.to_excel(f"{PATH_EXP}\\inventory_{args.date}.xlsx", index=False)
            console.print(
                "[spring_green3][bold]The file is created![/bold][spring_green3]")
    elif args.type == "expired":
        # Rebuild the expired products on a specific date per product or for all products
        data = inventory_per_date(args.date, args.item.lower())
        sorted_data = sorted(data, key=lambda id: id['purchase_id'])
        expired_data = [i for i in sorted_data if (
            i["expiration_date"] != "" and i["expiration_date"] < args.date)]
        table = Table(show_header=True, header_style="bold deep_sky_blue1")
        if expired_data != []:
            headers = expired_data[0].keys()
            for c in headers:
                table.add_column(c)
            for r in expired_data:
                data_per_row = r.values()
                table.add_row(*data_per_row)
        else:
            console.print("[red][bold]No data...[/bold][red]")
        console.print(table)
        if args.save == True and expired_data != []:
            df = pd.DataFrame(expired_data)
            df.to_excel(f"{PATH_EXP}\\expired_{args.date}.xlsx", index=False)
            console.print(
                "[spring_green3][bold]The file is created![/bold][spring_green3]")
