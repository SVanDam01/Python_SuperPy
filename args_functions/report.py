# Import
from other.settings import CSV_SALE, console
from logic.business_logic import calculation_product, calculation_total
from args_functions.product import product_type

# Functions for Report ARGS


def report(args):
    if args.type == "revenue" and args.item.lower() == "all":
        # Calculate the revenue in a certain period for all products
        display = calculation_total(
            args.period, product_type, CSV_SALE[len(CSV_SALE)-2:len(CSV_SALE)-1][0])
        console.print(
            f"[bright_cyan]Per [bold]{args.period}[/bold] the totall revenue of all sold products is [bold]€ {round(display,2)}[/bold][bright_cyan]")
    elif args.type == "revenue" and args.item.lower() != "all":
        # Calculate the revenue in a certain period for a single product
        display = calculation_product(
            args.period, args.item.lower(), CSV_SALE[len(CSV_SALE)-2:len(CSV_SALE)-1][0])
        console.print(
            f"[bright_cyan]Per [bold]{args.period}[/bold] the totall revenue of [bold]{args.item.lower()}[/bold] is € [bold]{round(display,2)}[/bold][bright_cyan]")
    elif args.type == "profit" and args.item.lower() == "all":
        # Calculate the profit in a certain period for all products
        display = calculation_total(
            args.period, product_type, CSV_SALE[len(CSV_SALE)-1:][0])
        console.print(
            f"[bright_cyan]Per [bold]{args.period}[/bold] the totall profit of all sold products is € [bold]{round(display,2)}[/bold][bright_cyan]")
    elif args.type == "profit" and args.item.lower() != "all":
        # Calculate the profit in a certain period for a single product
        display = calculation_product(
            args.period, args.item.lower(), CSV_SALE[len(CSV_SALE)-1:][0])
        console.print(
            f"[bright_cyan]Per [bold]{args.period}[/bold] the totall revenue of [bold]{args.item.lower()}[/bold] is € [bold]{round(display,2)}[/bold][bright_cyan]")
