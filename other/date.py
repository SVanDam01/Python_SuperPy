import os
from logic.csv_logic import read_rows, create_rows
from other.settings import SET_UP_DATE, PATH_CSV, CSV_DATE

# Set current date to date.csv for creating the concept of time in de system.


def set_date(date):
    title = CSV_DATE[1]
    add_row = dict(date=date)
    create_rows("\\date", [title], [add_row])


def read_date():
    isExist = os.path.exists(PATH_CSV+"\\date.csv")
    if isExist:
        try:
            CURRENT_DATE = list(read_rows("\\date")[0].values())[0]
            return CURRENT_DATE
        except:
            set_date(SET_UP_DATE)
            return SET_UP_DATE
    else:
        set_date(SET_UP_DATE)
        return SET_UP_DATE


# USE THE DATE OF THE SYSTEM (IN DEFAULT THE DATE AS IS, BUT COULD BE OVERWRITTEN BY THE USER)
CURRENT_DATE = read_date()
