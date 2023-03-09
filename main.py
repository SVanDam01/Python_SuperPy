# Imports
import argparse
from datetime import date
from settings import CSV_FILES, COMPANY_NAME
from csv_code import create_csv_folder, create_csv, create_rows, read_rows


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
# current date


product_type = {"fruit": ["banaan", "aardbei", "peren", "appels"], "groenten": [
    "bloemkool", "paprika", "wortel"], "vlees": ["kip", "rund", "varken"]}

# START PROGRAMMA OP IN DE MAIN.


def main():
    create_csv_folder()
    create_csv(CSV_FILES)
    parser = argparse.ArgumentParser(
        prog=f'SuperPy for {COMPANY_NAME}',
        description='We help you to track your inventory and profit',
        usage="Oeps, something is wrong",
        epilog='Made by Stefan copyright 2023')
    subparser = parser.add_subparsers(dest="command")

    sell_item = subparser.add_parser("sell", help="sell item")
    sell_item.add_argument("-d", "--date", required=True, help="selling date")
    sell_item.add_argument("-t", "--type", required=True,
                           choices=product_type.keys(), help=f"selling type, make a choice: {product_type.keys()}")
    sell_item.add_argument("-i", "--item", required=True,
                           help=f"selling item, make a choice: {product_type}")
    sell_item.add_argument("-q", "--quantity", required=True,
                           help="selling quantity")
    sell_item.add_argument("-p", "--price", required=True,
                           help="selling total price")

    args = parser.parse_args()

    if args.command == "sell":
        if args.item not in product_type[args.type]:
            print(
                f"select correct item that belongs to the type: {product_type[args.type]}")
        else:
            print("the input is proceed!")
            data = [1, 1, args.date, args.type,
                    args.item, args.quantity, args.price]
            create_rows("sale", data)
            print(data)

## Kopieeren voor commentline##
# python main.py sell --date 2022-02-14 --type fruit --item fruit --quantity 4 --price 4.00
# python main.py sell --date 2022-02-14 --type fruit --item banaan --quantity 4 --price 4.00
# python main.py sell --date 2022-03-14 --type fruit --item appels --quantity 2 --price 3.00
# python main.py sell -date 2022-02-14 -item bier
# python main.py sell -h


# --------------------------------------#

if __name__ == "__main__":
    main()
