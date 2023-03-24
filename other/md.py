from other.settings import COMPANY_NAME

md = f"""
# WELKOM TO SUPERPY FOR {COMPANY_NAME}!

**PRODUCTS** - Add new products & check for all products you offer
1. products -a / --add <type: product name>
2. products -c / --check

**FINANCIAL REPORTS** - Show the financial report
1. report revenue -p <type: period> -i <type: all / product name>
2. report profit -p <type: period> -i <type: all / product name>  

**INVENTORY REPORTS** - Show the inventory on a certain date
1. inventory -t <type: inventory or experiration> -p <type: period> -i <type: all / product name> s- <type: save (optional)>

**PURCHASE PRODUCTS** - Add the new bought products
1. buy -d <type: date> -i <type: product name> -q <type: quantity> -p <type: price> e- <type: exproration date (optional)>

**SELLING PRODUCTS** - Add the sold products
1. sell -i <type: product name> -q <type: quantity> -p <type: price>
"""

header = f"""

"""
