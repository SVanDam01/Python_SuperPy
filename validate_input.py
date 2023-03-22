# Imports
import datetime as dt

# Check the input for a specific period


def validate_period(period_text):
    if len(period_text) == 4:
        if int(period_text) > 2022 and int(period_text) < 2099:
            return period_text
        else:
            print("Incorrect data format, should be YYYY-MM-DD")
            raise Exception("Incorrect data format")
    elif len(period_text) == 7:
        if (int(period_text[:4]) > 2022 and int(period_text[:4]) < 2099) and (int(period_text[5:7]) > 0 and int(period_text[5:7]) < 13):
            return period_text
        else:
            print("Incorrect data format, should be YYYY-MM-DD")
            raise Exception("Incorrect data format")
    elif len(period_text) == 10:
        try:
            dt.date.fromisoformat(period_text)
            return period_text
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")
            raise ValueError(" ")
    else:
        print("Incorrect data format, should be YYYY-MM-DD")
        raise Exception("Incorrect data format")

# Check the input for a specific date


def validate_date(date_text):
    try:
        dt.date.fromisoformat(date_text)
        return date_text
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        raise ValueError(" ")
