# Imports
import os
from datetime import date
from rich.console import Console

# VARIABLES
CSV_FOLDER_NAME = "csv_files"
EXPORT_FOLDER_NAME = "export_files"
MAIN_FODLER_PATH = os.path.dirname(__file__)[:len(os.path.dirname(__file__))-5]
PATH_CSV = os.path.join(MAIN_FODLER_PATH, CSV_FOLDER_NAME)
PATH_EXP = os.path.join(MAIN_FODLER_PATH, EXPORT_FOLDER_NAME)
CSV_DATE = ["\\date", "date"]
CSV_PRODUCTS = ["\\products", "product_name"]
CSV_PURCHASE = ["\\purchase", "purchase_id", "purchase_date",
                "product_name", "quantity", "purchase_price", "expiration_date"]
CSV_SALE = ["\\sold", "id", "sell_date",
            "product_name", "quantity", "sell_price", "cost_price", "total_revenue_of_sale", "total_profit_of_sale"]
CSV_INVENT = ["\\actual_inv", "purchase_id", "purchase_date",
              "product_name", "quantity", "purchase_price", "expiration_date"]
CSV_FILES = [CSV_DATE, CSV_PRODUCTS, CSV_PURCHASE, CSV_SALE, CSV_INVENT]
COMPANY_NAME = "SuperM"
SET_UP_DATE = str(date.today())
F_REPPORTS = ["revenue", "profit"]
I_REPPORTS = ["inventory", "expired"]
console = Console()
