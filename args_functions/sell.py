# Import
from other.settings import CSV_SALE, CSV_INVENT, console
from logic.csv_logic import create_csv, read_rows, create_rows
from logic.business_logic import checking_stock_for_sale, actual_inventory
from other.date import CURRENT_DATE

# Functions for Sell ARGS


def sell(args):
    # Checking quantity is avalible in stock
    stock_qty = checking_stock_for_sale(args.item.lower(), CURRENT_DATE)
    if stock_qty >= args.quantity:
        # Count existing rows in file
        data_csv = read_rows("\\sold")
        sell_id = len(data_csv) + 1
        # Construct data for sale.csv
        actual_stock = sorted(read_rows("\\actual_inv"),
                              key=lambda id: id["purchase_id"])
        created_inventory = [
            i for i in actual_stock if i["purchase_date"] <= CURRENT_DATE]
        get_costprice_and_updated_inventory = actual_inventory(
            args.item.lower(), CURRENT_DATE, args.quantity, created_inventory)
        costprice = get_costprice_and_updated_inventory[0]
        total_revenue_of_sale = round(args.quantity * args.price, 2)
        total_cost_of_sale = round(args.quantity * costprice, 2)
        total_profit_of_sale = round(
            total_revenue_of_sale - total_cost_of_sale, 2)
        input_data = [sell_id, CURRENT_DATE,
                      args.item.lower(), args.quantity, args.price, costprice, round(total_revenue_of_sale, 2), round(total_profit_of_sale, 2)]
        sell_data = [dict(zip(CSV_SALE[1:], input_data))]
        # Apply data (argpars + cost) in to csv files
        create_rows(
            "\\sold", CSV_SALE[1:], sell_data)
        create_csv([CSV_INVENT])
        create_rows(
            "\\actual_inv", CSV_INVENT[1:], get_costprice_and_updated_inventory[1])
        console.print(
            f"[spring_green3][bold]The input is proceed! [bright_cyan]{stock_qty - args.quantity}[bright_cyan] left of [bright_cyan]{args.item.lower()}[bright_cyan][/bold][spring_green3]")
    else:
        console.print(
            f"[bright_red]Sorry, we only have[bright_red] [bright_cyan][bold]{stock_qty}[/bold][bright_cyan][bright_red] of[bright_red] [bright_cyan][bold]{args.item.lower()}[/bold][bright_cyan][bright_red] in stock[bright_red]")
