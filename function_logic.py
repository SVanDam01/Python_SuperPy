# Imports
import datetime as dt
from csv_code import read_rows
from settings import product_type

# Check date input


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


# validate_period("2023-13")


def validate_date(date_text):
    try:
        dt.date.fromisoformat(date_text)
        return date_text
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        raise ValueError(" ")


def checking_stock_for_sale(item, date):
    data = read_rows("\\actual_inv")
    stock = [s["quantity"] for s in data if s["product_name"] == item and s["purchase_date"]
             <= date and (s["expiration_date"] == "" or s["expiration_date"] > date)]
    stock_sum = sum(list(map(int, stock)))
    return stock_sum


# print(checking_stock_for_sale("banaan", "2023-03-17"))


def calculation_product(date, item, report):
    data = read_rows("\\sold")
    total_profit = 0
    if len(date) == 10:
        revenue = [s[report]
                   for s in data if s["product_name"] == item and s["sell_date"] == date]
        total_profit = sum(list(map(float, revenue)))
    elif len(date) == 7:
        revenue = [s[report] for s in data if s["product_name"] ==
                   item and dt.date.fromisoformat(s["sell_date"]).strftime("%Y-%m") == date]
        total_profit = sum(list(map(float, revenue)))
    elif len(date) == 4:
        revenue = [s[report] for s in data if s["product_name"] ==
                   item and dt.date.fromisoformat(s["sell_date"]).strftime("%Y") == date]
        total_profit = sum(list(map(float, revenue)))
    return total_profit


def calculation_total(date, items_list, report):
    list_revenues = 0
    for item in items_list:
        list_revenues += int(calculation_product(date, item, report))
    return round(list_revenues, 2)


def actual_inventory(item, date, qty, file):
    actual_inv = read_rows(file)
    new_inventory = []
    keep_inventory = [i for i in actual_inv if i["product_name"]
                      != item and i["purchase_date"] <= date]
    for k in keep_inventory:
        new_inventory.append(k)
    # print(new_inventory)
    update_inventory = [i for i in actual_inv if i["product_name"]
                        == item and i["purchase_date"] <= date]
    # print(update_inventory)
    qty_list = qty
    total_cost_purchase = 0
    while qty_list > 0:
        for i in update_inventory:
            if (int(i["quantity"]) > qty_list and qty_list != 0) and (i["expiration_date"] == "" or i["expiration_date"] > date):
                cost = float(i["purchase_price"]) * qty_list
                # print(f"de kosten zijn {cost}")
                total_cost_purchase = total_cost_purchase + cost
                # vooraad = int(i["quantity"])
                # print(f"vooraad {vooraad} is > {qty_list}")
                new_qty = int(i["quantity"]) - qty_list
                qty_list = 0
                i["quantity"] = new_qty
                new_inventory.append(i)
                # print(f"vooraad is {new_qty} en de aankoop is {qty_list}")
            elif (int(i["quantity"]) < qty_list or int(i["quantity"]) == qty_list) and (i["expiration_date"] == "" or i["expiration_date"] > date):
                cost = float(i["purchase_price"]) * int(i["quantity"])
                # print(f"de kosten zijn {cost}")
                total_cost_purchase = total_cost_purchase + cost
                # vooraad = int(i["quantity"])
                # print(f"vooraad is {vooraad} en aankoop is nog {qty_list}")
                new_qty = 0
                qty_list = qty_list - int(i["quantity"])
                # print(f"{qty_list} is nog")
                continue
            else:
                # verval = i["expiration_date"]
                new_inventory.append(i)
                # print(f"Houden in lijst, omdat expiration date is {verval}")
    mean_cost_purchase = total_cost_purchase / qty
    # print(mean_cost_purchase)
    # for k in new_inventory:
    #     print(k)
    return mean_cost_purchase, new_inventory


# print(actual_inventory("banaan", "2023-03-16", 2, "\\actual_inv"))

def inventory_per_date(date):
    purchase_file = "\\purchase"
    sold_file = read_rows("\\sold")
    sold_items = [i for i in sold_file if i["sell_date"] <= date]
    print(sold_items)
    created_inventory = []
    for i in sold_items:
        callback = actual_inventory(
            i["product_name"], i["sell_date"], int(i["quantity"]), purchase_file)[1]
        created_inventory = callback
        print(created_inventory)


inventory_per_date("2023-03-16")
# lijst is leeg voor de verkoop op 17-03.
