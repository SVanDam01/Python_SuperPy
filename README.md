# THIS IS SUPERPY!

SuperPy is a Comment Line Interface (CLI) for inventory management.

## **TECHNICAL**

This CLI is using the following moduls:

> - Pandas
> - Rich

## **FUNCTIONALITIES**

SuperPy has the following functionalities:

### _PRODUCTS_

Add new products & check for all products you offer.

1. python superpy.py products -a / --add <type: product name>
2. python superpy.py products -c / --check

Exemple check:

![An example of listing all products your company is offering](/assets/product_check.bmp)

**FINANCIAL REPORTS** - Show the financial report

1. report revenue -p <type: period> -i <type: all / product name>
2. report profit -p <type: period> -i <type: all / product name>

**INVENTORY REPORTS** - Show the inventory on a certain date

1. inventory -t <type: inventory or experiration> -p <type: period> -i <type: all / product name> s- <type: save (optional)>

**PURCHASE PRODUCTS** - Add the new bought products

1. buy -d <type: date> -i <type: product name> -q <type: quantity> -p <type: price> e- <type: exproration date (optional)>

**SELLING PRODUCTS** - Add the sold products

1. sell -i <type: product name> -q <type: quantity> -p <type: price>
