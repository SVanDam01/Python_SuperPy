import os

# VARIABLES
CSV_FOLDER_NAME = "csv_files"
MAIN_FODLER_PATH = os.path.dirname(__file__)
PATH = os.path.join(MAIN_FODLER_PATH, CSV_FOLDER_NAME)
CSV_PURCHASE = ["purchase", "id", "purchase_date", "type",
                "product_name", "quantity", "purchase_price", "expiration_date"]
CSV_SALE = ["sale", "id", "purchase_id", "sell_date", "type",
            "product_name", "quantity", "sell_price"]
CSV_FILES = [CSV_PURCHASE, CSV_SALE]
COMPANY_NAME = "SuperM"
