# Import
from other.date import CURRENT_DATE, set_date
from other.settings import console, CSV_DATE
from logic.csv_logic import create_csv
from datetime import timedelta, datetime

# Functions for Date ARGS


def date(args):
    # commands for checking the current date af the system
    if args.check == True:
        # print the current system date
        console.print(
            f"[bright_cyan][bold]The current date is: {CURRENT_DATE}[/bold][bright_cyan]")
    if args.set:
        # change the current date to a new date en save this in de date.csv
        create_csv([CSV_DATE])
        set_date(args.set)
        console.print(
            f"[bright_cyan][bold]The new current date of the system is set to: {args.set}[/bold][bright_cyan]")
    if args.advance:
        # change the current date to a new date en save this in de date.csv
        create_csv([CSV_DATE])
        new_date = (datetime.strptime(CURRENT_DATE, '%Y-%m-%d') +
                    timedelta(days=int(args.advance))).strftime('%Y-%m-%d')
        set_date(new_date)
        console.print(
            f"[bright_cyan][bold]The new current date of the system is set to: {new_date}[/bold][bright_cyan]")


# python superpy.py date -c
# python superpy.py date -s 2023-02-15
# python superpy.py date -a 10
# python superpy.py sell -i bananen -q 5 -p 4
