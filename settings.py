# Imports
import os
import datetime as dt
from datetime import date, timedelta

# VARIABLES
CSV_FOLDER_NAME = "csv_files"
MAIN_FODLER_PATH = os.path.dirname(__file__)
PATH = os.path.join(MAIN_FODLER_PATH, CSV_FOLDER_NAME)
CSV_PURCHASE = ["\\purchase", "purchase_id", "purchase_date",
                "product_name", "quantity", "purchase_price", "expiration_date"]
CSV_SALE = ["\\sold", "id", "sell_date",
            "product_name", "quantity", "sell_price", "cost_price", "total_revenue_of_sale", "total_profit_of_sale"]
CSV_INVENT = ["\\actual_inv", "purchase_id", "purchase_date",
              "product_name", "quantity", "purchase_price", "expiration_date"]
CSV_FILES = [CSV_PURCHASE, CSV_SALE, CSV_INVENT]
COMPANY_NAME = "SuperM"
CURRENT_DATE = date.today()
REPPORTS = ["revenue", "profit"]
product_type = ["banaan", "aardbei", "peren", "appels",
                "bloemkool", "paprika", "wortel", "kip", "rund", "varken"]

# print(product_type)
# product_type.append("all")
# print(product_type)
# input = "2023-12-01"
# datum = input + "-01"
# add_days = CURRENT_DATE + timedelta(days=2)
# formating = dt.datetime.strptime(datum, "%Y-%d-%m")

# print(CURRENT_DATE)
# print(datum)
# print(add_days)
# print(formating)
