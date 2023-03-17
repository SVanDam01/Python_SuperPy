# Imports
import os
from settings import PATH, CSV_FILES, CSV_SALE, CSV_INVENT, CSV_PURCHASE, CURRENT_DATE, product_type
from csv_code import create_csv_folder, create_csv, read_rows, create_rows_dict
from function_logic import checking_stock_for_sale, actual_inventory, calculation_product, calculation_total
from parser_logic import args


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

# START PROGRAMMA OP IN DE MAIN

CURRENT_DATE = str(CURRENT_DATE)


def main():
    # CHECK AND/OR CREATE CSV FILES
    isExist = os.path.exists(PATH)
    if not isExist:
        create_csv_folder()
        create_csv(CSV_FILES)

    # SET INPUT BUY
    if args.command == "buy":
        # count existing rows in file
        data_csv = read_rows("\\purchase")
        buy_id = len(data_csv) + 1
        # Apply argpars data in to csv file
        input_data = [buy_id, args.date,
                      args.item, args.quantity, args.price, args.expiration]
        buy_data = [dict(zip(CSV_INVENT[1:], input_data))]
        create_rows_dict("\\purchase", CSV_PURCHASE[1:], buy_data)
        create_rows_dict("\\actual_inv", CSV_INVENT[1:], buy_data)
        print("the input is proceed!")

    # SET INPUT SELL
    if args.command == "sell":
        # checking quantity is avalible in stock
        stock_qty = checking_stock_for_sale(args.item, CURRENT_DATE)
        if stock_qty >= args.quantity:
            # count existing rows in file
            data_csv = read_rows("\\sold")
            sell_id = len(data_csv) + 1
            # Apply data (argpars + cost) in to csv file
            get_costprice_and_updated_inventory = actual_inventory(
                args.item, CURRENT_DATE, args.quantity, "\\actual_inv")
            costprice = get_costprice_and_updated_inventory[0]
            total_revenue_of_sale = args.quantity * args.price
            total_cost_of_sale = args.quantity * costprice
            total_profit_of_sale = total_revenue_of_sale - total_cost_of_sale
            input_data = [sell_id, CURRENT_DATE,
                          args.item, args.quantity, args.price, costprice, total_revenue_of_sale, total_profit_of_sale]
            sell_data = [dict(zip(CSV_SALE[1:], input_data))]
            create_rows_dict(
                "\\sold", CSV_SALE[1:], sell_data)
            create_csv([CSV_INVENT])
            create_rows_dict(
                "\\actual_inv", CSV_INVENT[1:], get_costprice_and_updated_inventory[1])
            print(
                f"The input is proceed! {stock_qty - args.quantity} left of {args.item}")
        else:
            print(f"Sorry, we only have {stock_qty} of {args.item} in stock")

    # SET INPUT REPORTS
    if args.command == "report":
        if args.type == "revenue" and args.item == "all":
            display = calculation_total(
                args.period, product_type, CSV_SALE[len(CSV_SALE)-2:len(CSV_SALE)-1][0])
            print(
                f"Per {args.period} the totall revenue of all sold products is € {display}")
        elif args.type == "revenue" and args.item != "all":
            display = calculation_product(
                args.period, args.item, CSV_SALE[len(CSV_SALE)-2:len(CSV_SALE)-1][0])
            print(
                f"Per {args.period} the totall revenue of {args.item} is € {display}")
        elif args.type == "profit" and args.item == "all":
            display = calculation_total(
                args.period, product_type, CSV_SALE[len(CSV_SALE)-1:][0])
            print(
                f"Per {args.period} the totall profit of all sold products is € {display}")
        elif args.type == "profit" and args.item != "all":
            display = calculation_product(
                args.period, args.item, CSV_SALE[len(CSV_SALE)-1:][0])
            print(
                f"Per {args.period} the totall revenue of {args.item} is € {display}")

## Kopieeren voor commentline HELP##
# python main.py --help
# python main.py sell --help
# python main.py report --help

## Kopieeren voor commentline BUY##
# python main.py buy --date 2022-02-14 --item banaan --quantity 4 --price 4.00 --expiration 2023-02-21
# python main.py buy --date 2022-02-14 --item banaan --quantity 2 --price 6.00 --expiration 2023-02-23
# python main.py buy --item banaan --quantity 2 --price 6.00
# python main.py buy --item peren --quantity 5 --price 9.20 --expiration 2023-03-23
# python main.py buy --date 2023-13-14 --type fruit --item banaan --quantity 2 --price 6.00
# python main.py buy --item bananen --quantity 2 --price 7.20 --expiration 2023-02-23

## Kopieeren voor commentline SELL##
# python main.py sell --date 2023-02-14 --item fruit --quantity 4 --price 4.00
# python main.py sell --date 2023-02-14 --item banaan --quantity 1 --price 7.00
# python main.py sell --date 2023-03-14 --item peren --quantity 2 --price 3.00
# python main.py sell --item banaan --quantity 2 --price 3.00
# python main.py sell --item banaan --quantity 12 --price 16.00
# python main.py sell -date 2023-02-14 -item bier

## Kopieeren voor commentline REPORT##
# python main.py report --type revenue --item banaan --period 2023-03-17
# python main.py report --type revenue --period 2023-03-15
# python main.py report --type revenue --period 2023-03
# python main.py report --type verlag --period 2023-03-15
# python main.py report --type profit --period 2023-03
# python main.py report --type profit --item banaan --period 2023-03-17


# --------------------------------------#
if __name__ == "__main__":
    main()
