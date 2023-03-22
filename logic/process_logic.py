# Imports
from args_functions.product import products
from args_functions.buy import buy
from args_functions.sell import sell
from args_functions.report import report
from args_functions.inventory import inventory


# This file process the args to the function that are related to the args.

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


## Kopieeren voor commentline PRODUCTS##
# python superpy.py products --add bier
# python superpy.py products --check

## Kopieeren voor commentline HELP##
# python superpy.py --help
# python superpy.py sell --help
# python superpy.py report --help

## Kopieeren voor commentline BUY##
# python superpy.py buy --date 2022-02-14 --item banaan --quantity 4 --price 4.00 --expiration 2023-02-21
# python superpy.py buy --date 2022-02-17 --item kip --quantity 4 --price 8.60 --expiration 2023-02-23
# python superpy.py buy --item banaan --quantity 2 --price 6.00
# python superpy.py buy --item peren --quantity 5 --price 9.20 --expiration 2023-03-23
# python superpy.py buy --date 2023-13-14 --type fruit --item banaan --quantity 2 --price 6.00
# python superpy.py buy --item bananen --quantity 2 --price 7.20 --expiration 2023-02-23

## Kopieeren voor commentline SELL##
# python superpy.py sell --date 2023-02-14 --item fruit --quantity 4 --price 4.00
# python superpy.py sell --date 2023-02-14 --item banaan --quantity 1 --price 7.00
# python superpy.py sell --date 2023-03-14 --item peren --quantity 2 --price 3.00
# python superpy.py sell --item banaan --quantity 2 --price 3.00
# python superpy.py sell --item peren --quantity 3 --price 12.00
# python superpy.pyy sell --item banaan --quantity 12 --price 16.00
# python superpy.py sell -date 2023-02-14 -item bier

## Kopieeren voor commentline REPORT##
# python superpy.py report --type revenue --item banaan --period 2023-03-17
# python superpy.py report --type revenue --period 2023-03-15
# python superpy.py report --type revenue --period 2023-03
# python superpy.py report --type verlag --period 2023-03-15
# python superpy.py report --type profit --period 2023-03
# python superpy.py report --type profit --item banaan --period 2023-03-17

## Kopieeren voor commentline INVENTORY##
# python superpy.py inventory --type inventory --item banaan --date 2023-03-17
# python superpy.py inventory --type revenue --item banaan --date 2023-03-17
# python superpy.py inventory --type inventory --period 2023-03-15
# python superpy.py inventory --type inventory --date 2023-03
# python superpy.py inventory --type inventory --date 2023-03-21
# python superpy.py inventory --type inventory --date 2023-03-21 --save
# python superpy.py inventory --type expired --date 2023-03
# python superpy.py inventory --type expired --item banaan --date 2023-03-17
# python superpy.py inventory --type expired --date 2023-03-17
# python superpy.py inventory --type inventory --item banaan --date 2023-03-17
