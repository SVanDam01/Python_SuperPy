# THIS IS SUPERPY!

SuperPy for SuperM is a Comment Line Interface (CLI) for inventory management.

## **TECHNICAL**

This CLI is using the following moduls:

> - [Pandas](https://pandas.pydata.org/docs/)
> - [Rich](https://rich.readthedocs.io/en/stable/introduction.html)

The folder csv_files has some dummy records. If you want to get a clean start. Please delete the folder. The first time you run the file, the folders will be automatically generated.

## **FUNCTIONALITIES**

SuperPy has the following functionalities:

### _1. PRODUCTS_

Add new products & check for all products you offer.

> - python superpy.py products -a / --add _<type: product name>_
> - python superpy.py products -c / --check

**_Example check_**:

![An example of listing all products your company is offering](/assets/product_check.bmp)

**_Example adding product_**:

![An example of adding a new product to the list](/assets/product_add.bmp)

### _2. FINANCIAL REPORTS_

Show the financial report for thge revenue of profit in a certain period

> - python superpy.py report revenue -p _<type: period> -i <type: all / product name>_
> - python superpy.py report profit -p _<type: period> -i <type: all / product name>_

**_Example revenue for one product on a single date_**:

![An example of the revenue for one product on a single date](/assets/revenue_item_date.bmp)

**_Example totall profit in a certain period_**:

![An example of the totall profit in a certain period](/assets/profit_all_period.bmp)

### _3. INVENTORY REPORTS_

Show the inventory on a certain date

> - python superpy.py inventory -t _<type: inventory or experiration>_ -p _<type: period>_ -i _<type: all / product name>_ s- _<type: save (optional)>_

**_Example inventory (only in de terminal)_**:

![An example of a product in stock on a certain date](/assets/inventory_item.bmp)

**_Example all expired product on a certain date (in de terminal + saving the file in Excel)_**:

![An example of all expired product on a certain date](/assets/expired_all_save.bmp)

### _4. PURCHASE PRODUCTS_

Add the new bought products

> - python superpy.py buy -d _<type: date>_ -i _<type: product name>_ -q _<type: quantity>_ -p _<type: price>_ e- _<type: experation date (optional)>_

**_Example bought product without experation date_**:

![An example of adding a new bought product](/assets/buy.bmp)

**_Example bought product with experation date_**:

![An example of adding a new bought product](/assets/buy_exp.bmp)

### _5. SELLING PRODUCTS_

Add the sold products

> - python superpy.py sell -i _<type: product name>_ -q _<type: quantity>_ -p _<type: price>_

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
