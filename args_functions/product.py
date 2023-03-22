# Import
from logic.csv_logic import read_rows, create_rows
from logic.business_logic import product_list
from settings import console

# Functions for Product ARGS

product_type = product_list()


def products(args):
    # Retrive the data from the Product.csv and create the list of all products
    data_csv = read_rows("\\products")
    # If "Check" is the argument return the list of current productnames
    if args.check == True:
        # print the list of all products
        console.print(
            f"[bright_cyan][bold]The following products are administrated: {product_type}[/bold][bright_cyan]")
    else:
        # Check if the products already exist
        if args.add.lower() in product_type:
            console.print(
                f"[bright_cyan][bold]{args.add} already exist![/bold][bright_cyan]")
        else:
            # If the product is not in the list, create it in de csv file Producuts
            header = str(list(data_csv[0].keys())[0])
            add_row = dict(product_name=args.add.lower())
            create_rows("\\products", [header], [add_row])
            console.print(
                f"[spring_green3][bold]{args.add} is added to the list![/bold][spring_green3]")
