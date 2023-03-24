# Imports
import datetime as dt
from logic.csv_logic import read_rows

# Retrive the data from the Product.csv and return the list of all products


def product_list():
    data_csv = read_rows("\\products")
    converted_to_list = []
    for p in data_csv:
        i = list(p.values())[0]
        converted_to_list.append(i)
    return converted_to_list


# Checking the current stock of a item before it could be sold


def checking_stock_for_sale(item, date):
    data = read_rows("\\actual_inv")
    stock = [s["quantity"] for s in data if s["product_name"] == item and s["purchase_date"]
             <= date and (s["expiration_date"] == "" or s["expiration_date"] > date)]
    stock_sum = sum(list(map(int, stock)))
    return stock_sum

# Calculate the revenue or profit per product based on selected period


def calculation_product(date, item, report):
    data = read_rows("\\sold")
    total = 0
    if len(date) == 10:
        selections = [s[report]
                      for s in data if s["product_name"] == item and s["sell_date"] == date]
        total = sum(list(map(float, selections)))
    elif len(date) == 7:
        selections = [s[report] for s in data if s["product_name"] ==
                      item and dt.date.fromisoformat(s["sell_date"]).strftime("%Y-%m") == date]
        total = sum(list(map(float, selections)))
    elif len(date) == 4:
        selections = [s[report] for s in data if s["product_name"] ==
                      item and dt.date.fromisoformat(s["sell_date"]).strftime("%Y") == date]
        total = sum(list(map(float, selections)))
    return total

# Calculate the total revenue or profit based on selected period. It used the fucntion above


def calculation_total(date, items_list, report):
    list_revenues = 0
    for item in items_list:
        list_revenues += int(calculation_product(date, item, report))
    return round(list_revenues, 2)

# Change the actual inventory based. This function is used voor updating the current inventory
# and to rebuild the history of the inventory on a specific date.


def actual_inventory(item, date, qty, file):
    actual_inv = file
    new_inventory = []
    keep_inventory = [i for i in actual_inv if i["product_name"]
                      != item]
    for k in keep_inventory:
        new_inventory.append(k)
    update_inventory = [i for i in actual_inv if i["product_name"]
                        == item]
    sorted_data = sorted(
        update_inventory, key=lambda id: int(id["purchase_id"]))
    qty_list = qty
    total_cost_purchase = 0
    # loop through the list of inventory untill the qty_list is 0. After each loop the amount will decr. by the amount af the row
    # of the qty of the current row is > 0 it will be added to the inventory list with the new velue. Otherwise is will be deleted.
    while qty_list > 0:
        for i in sorted_data:
            if (int(i["quantity"]) > qty_list and qty_list != 0) and (i["expiration_date"] == "" or i["expiration_date"] > date):
                cost = float(i["purchase_price"]) * qty_list
                total_cost_purchase = total_cost_purchase + cost
                new_qty = int(i["quantity"]) - qty_list
                qty_list = 0
                i["quantity"] = str(new_qty)
                new_inventory.append(i)
            elif (int(i["quantity"]) < qty_list or int(i["quantity"]) == qty_list) and (i["expiration_date"] == "" or i["expiration_date"] > date):
                cost = float(i["purchase_price"]) * int(i["quantity"])
                total_cost_purchase = total_cost_purchase + cost
                new_qty = 0
                qty_list = qty_list - int(i["quantity"])
                continue
            else:
                new_inventory.append(i)
    # return the new dict of the inventory and the mean of the cost price
    new_inventory = sorted(new_inventory, key=lambda id: id["purchase_id"])
    mean_cost_purchase = total_cost_purchase / qty
    return mean_cost_purchase, new_inventory


# This function  This function is simular to the function above, but it has some small changes

def inventory_per_date(date, item):
    sold_file = read_rows("\\sold")
    sold_items = [i for i in sold_file if i["sell_date"] <= date]
    initual_stock = sorted(
        read_rows("\\purchase"), key=lambda id: id["purchase_id"])
    created_inventory = [
        i for i in initual_stock if i["purchase_date"] <= date]
    for i in sold_items:
        callback = actual_inventory(
            i["product_name"], i["sell_date"], int(i["quantity"]), created_inventory)[1]
        created_inventory = callback
    if item != "all":
        filter_item = [
            i for i in created_inventory if i["product_name"] == item]
        created_inventory = filter_item
    return created_inventory
