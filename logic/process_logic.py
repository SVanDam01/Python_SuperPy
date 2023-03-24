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
