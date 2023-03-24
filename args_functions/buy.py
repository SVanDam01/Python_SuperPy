# Import
from other.settings import CSV_INVENT, CSV_PURCHASE, console
from logic.csv_logic import read_rows, create_rows

# Functions for Buy ARGS


def buy(args):
    # Count existing rows in file
    data_csv = read_rows("\\purchase")
    buy_id = len(data_csv) + 1
    # Apply argpars data in to csv file
    input_data = [buy_id, args.date,
                  args.item.lower(), args.quantity, args.price, args.expiration]
    buy_data = [dict(zip(CSV_INVENT[1:], input_data))]
    create_rows("\\purchase", CSV_PURCHASE[1:], buy_data)
    create_rows("\\actual_inv", CSV_INVENT[1:], buy_data)
    console.print(
        "[spring_green3][bold]The input is proceed![/bold][spring_green3]")
