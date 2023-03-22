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

**_Example check_**:

![An example of listing all products your company is offering](/assets/product_check.bmp)

**_Example adding product_**:

![An example of adding a new product to the list](/assets/product_add.bmp)

### _FINANCIAL REPORTS_

Show the financial report for thge revenue of profit in a certain period

1. python superpy.py report revenue -p <type: period> -i <type: all / product name>
2. python superpy.py report profit -p <type: period> -i <type: all / product name>

**_Example revenue for one product on a single date_**:

![An example of listing all products your company is offering](/assets/revenue_item_date.bmp)

**_Example totall profit in a certain period_**:

![An example of adding a new product to the list](/assets/profit_all_period.bmp)

### _INVENTORY REPORTS_

Show the inventory on a certain date

1. python superpy.py inventory -t <type: inventory or experiration> -p <type: period> -i <type: all / product name> s- <type: save (optional)>

**_Example inventory (only in de terminal)_**:

![An example of adding a new product to the list](/assets/inventory_item.bmp)

**_Example all expired product on a certain date (in de terminal + saving the file in Excel)_**:

![An example of adding a new product to the list](/assets/expired_all_save.bmp)

### _PURCHASE PRODUCTS_

Add the new bought products

1. python superpy.py buy -d <type: date> -i <type: product name> -q <type: quantity> -p <type: price> e- <type: experation date (optional)>

**_Example bought product without experation date_**:

![An example of adding a new product to the list](/assets/product_add.bmp)

**_Example bought product with experation date_**:

![An example of adding a new product to the list](/assets/product_add.bmp)

### _SELLING PRODUCTS_

Add the sold products

1. python superpy.py sell -i <type: product name> -q <type: quantity> -p <type: price>

**_Example selling product when quantity is in stock_**:

![An example of adding a new product to the list](/assets/product_add.bmp)

**_Example selling product when quantity is NOT in stock_**:

![An example of adding a new product to the list](/assets/product_add.bmp)
