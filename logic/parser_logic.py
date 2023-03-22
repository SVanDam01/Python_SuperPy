# Imports
import argparse
from settings import COMPANY_NAME, CURRENT_DATE, F_REPPORTS, I_REPPORTS
from validate_input import validate_date, validate_period
from args_functions.product import product_type


# PARSER SETTINGS
parser = argparse.ArgumentParser(
    prog=f'SuperPy for {COMPANY_NAME}',
    description='We help you to track your inventory and profit',
    epilog='Made by Stefan copyright 2023')
subparser = parser.add_subparsers(
    dest="command", help="Select CL inout options")

# SET SUB-ARGPARSER BUY INCLUDING ARGUMENTS
products_item = subparser.add_parser("products", help="Purchase items")
products_item.add_argument("-a", "--add", metavar=" ",
                           help="Add new products before you can buy/sell them")
products_item.add_argument("-c", "--check", action='store_true',
                           help="Check all administrated products")


# SET SUB-ARGPARSER BUY INCLUDING ARGUMENTS
buy_item = subparser.add_parser("buy", help="Purchase items")
buy_item.add_argument("-d", "--date", default=CURRENT_DATE, type=validate_date,
                      help="Purchase date", metavar=" ")
buy_item.add_argument("-i", "--item", required=True,
                      help=f"Purchase item, make a choice: {product_type} or add them first (products -a/--add)", metavar=" ", choices=product_type)
buy_item.add_argument("-q", "--quantity", required=True, type=int,
                      help="Purchase quantity", metavar=" ")
buy_item.add_argument("-p", "--price", required=True, type=float,
                      help="Purchase total price", metavar=" ")
buy_item.add_argument("-e", "--expiration",
                      help="Optional: the expiration date of the product", metavar=" ", type=validate_date)

# SET SUB-ARGPARSER SELL INCLUDING ARGUMENTS
sell_item = subparser.add_parser("sell", help="Sell items")
sell_item.add_argument("-i", "--item", required=True,
                       help=f"Selling item, make a choice: {product_type}", metavar=" ", choices=product_type)
sell_item.add_argument("-q", "--quantity", required=True, type=int,
                       help="Selling quantity", metavar=" ")
sell_item.add_argument("-p", "--price", required=True, type=float,
                       help="Selling total price", metavar=" ")

# SET SUB-ARGPARSER FINANCIAL REPORTS INCLUDING ARGUMENTS
report_item = subparser.add_parser("report", help="Financial reports")
report_item.add_argument("-t", "--type", required=True,
                         help=f"Select a type of report: {F_REPPORTS}", metavar=" ", choices=F_REPPORTS)
report_item.add_argument("-p", "--period", required=True, type=validate_period,
                         help="Specify a period: day=YYYY-MM-DD, month=YYYY-MM and year=YYYY", metavar=" ")
report_item.add_argument("-i", "--item", default="all", choices=product_type,
                         help="Optional: specify by one product", metavar=" ")

# SET SUB-ARGPARSER INVENTORY REPORTS INCLUDING ARGUMENTS
inventory_item = subparser.add_parser("inventory", help="Inventory reports")
inventory_item.add_argument("-t", "--type", required=True,
                            help=f"Select a type of report: {I_REPPORTS}", metavar=" ", choices=I_REPPORTS)
inventory_item.add_argument("-d", "--date", default=CURRENT_DATE, type=validate_date,
                            help="Purchase date", metavar=" ")
inventory_item.add_argument("-i", "--item", default="all", choices=product_type,
                            help="Optional: specify by one product", metavar=" ")
inventory_item.add_argument("-s", "--save", action='store_true',
                            help="Save output in a seperate cvs file")

# SET PARSE_ARGS
args = parser.parse_args()
