# Imports
import argparse
from settings import COMPANY_NAME, CURRENT_DATE, product_type, REPPORTS
from function_logic import validate_date, validate_period


# PARSER SETTINGS
parser = argparse.ArgumentParser(
    prog=f'SuperPy for {COMPANY_NAME}',
    description='We help you to track your inventory and profit',
    usage="Oeps, something is wrong",
    epilog='Made by Stefan copyright 2023')
subparser = parser.add_subparsers(
    dest="command", help="select CL inout options")

# SET SUB-ARGPARSER BUY INCLUDING ARGUMENTS
buy_item = subparser.add_parser("buy", help="Purchase items")
buy_item.add_argument("-d", "--date", default=CURRENT_DATE.isoformat(), type=validate_date,
                      help="Purchase date", metavar=" ")
buy_item.add_argument("-i", "--item", required=True,
                      help=f"Purchase item, make a choice: {product_type}", metavar=" ", choices=product_type)
buy_item.add_argument("-q", "--quantity", required=True, type=int,
                      help="Purchase quantity", metavar=" ")
buy_item.add_argument("-p", "--price", required=True, type=float,
                      help="Purchase total price", metavar=" ")
buy_item.add_argument("-e", "--expiration",
                      help="Optional: the expiration date of the product", metavar=" ", type=validate_date)

# SET SUB-ARGPARSER SELL INCLUDING ARGUMENTS
sell_item = subparser.add_parser("sell", help="Sell items")
# sell_item.add_argument("-d", "--date", default=CURRENT_DATE.isoformat(), type=validate_date,
#                        help="selling date", metavar=" ")
sell_item.add_argument("-i", "--item", required=True,
                       help=f"Selling item, make a choice: {product_type}", metavar=" ", choices=product_type)
sell_item.add_argument("-q", "--quantity", required=True, type=int,
                       help="Selling quantity", metavar=" ")
sell_item.add_argument("-p", "--price", required=True, type=float,
                       help="Selling total price", metavar=" ")

# SET SUB-ARGPARSER REPORT INCLUDING ARGUMENTS
report_item = subparser.add_parser("report", help="financial reports")
report_item.add_argument("-t", "--type", required=True,
                         help=f"Select a type of report: {REPPORTS}", metavar=" ", choices=REPPORTS)
report_item.add_argument("-p", "--period", required=True, type=validate_period,
                         help="Specify a period: day=YYYY-MM-DD, month=YYYY-MM and year=YYYY", metavar=" ")
report_item.add_argument("-i", "--item", default="all", choices=product_type.append("all"),
                         help="Optional: specify by one product", metavar=" ")

# SET PARSE_ARGS
args = parser.parse_args()
