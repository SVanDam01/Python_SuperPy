# THIS IS SUPERPY!

SuperPy is a Comment Line Interface (CLI) for inventory management.

## **TECHNICAL**

This CLI is using the following moduls:

> - Pandas
> - Rich

## **FUNCTIONALITIES**

SuperPy has the following functionalities:

### _1. PRODUCTS_

Add new products & check for all products you offer.

> - python superpy.py products -a / --add <type: product name>
> - python superpy.py products -c / --check

**_Example check_**:

![An example of listing all products your company is offering](/assets/product_check.bmp)

**_Example adding product_**:

![An example of adding a new product to the list](/assets/product_add.bmp)

### _2. FINANCIAL REPORTS_

Show the financial report for thge revenue of profit in a certain period

> - python superpy.py report revenue -p <type: period> -i <type: all / product name>
> - python superpy.py report profit -p <type: period> -i <type: all / product name>

**_Example revenue for one product on a single date_**:

![An example of the revenue for one product on a single date](/assets/revenue_item_date.bmp)

**_Example totall profit in a certain period_**:

![An example of the totall profit in a certain period](/assets/profit_all_period.bmp)

### _3. INVENTORY REPORTS_

Show the inventory on a certain date

> - python superpy.py inventory -t <type: inventory or experiration> -p <type: period> -i <type: all / product name> s- <type: save (optional)>

**_Example inventory (only in de terminal)_**:

![An example of a product in stock on a certain date](/assets/inventory_item.bmp)

**_Example all expired product on a certain date (in de terminal + saving the file in Excel)_**:

![An example of all expired product on a certain date](/assets/expired_all_save.bmp)

### _4. PURCHASE PRODUCTS_

Add the new bought products

> - python superpy.py buy -d <type: date> -i <type: product name> -q <type: quantity> -p <type: price> e- <type: experation date (optional)>

**_Example bought product without experation date_**:

![An example of adding a new bought product](/assets/buy.bmp)

**_Example bought product with experation date_**:

![An example of adding a new bought product](/assets/buy_exp.bmp)

### _5. SELLING PRODUCTS_

Add the sold products

> - python superpy.py sell -i <type: product name> -q <type: quantity> -p <type: price>

**_Example selling product when quantity is in stock_**:

![An example of selling products when quantity is in stock](/assets/sell.bmp)

**_Example selling product when quantity is NOT in stock_**:

![An example of selling products when quantity is NOT in stock](/assets/sell_not.bmp)

### _HELP_

Get more information about the argument per functionality

> - python superpy.py products -h
> - python superpy.py report -h
> - python superpy.py inventory -h
> - python superpy.py buy -h
> - python superpy.py sell -h
