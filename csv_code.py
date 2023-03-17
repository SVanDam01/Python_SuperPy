# Imports
import csv
# import pandas as pd
import os
from settings import PATH

# FUNCTION CREATE CSV FOLDER:


def create_csv_folder():
    os.makedirs(PATH)


# FUNCTION CREATE CSV FILES:
def create_csv(csv_files):
    for file in csv_files:
        with open(f"{PATH}{file[0]}.csv", mode="w", newline='', encoding="utf8") as csv_file:
            fieldnames = file[1:len(file)]
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames)
            writer.writeheader()


# FUNCTION READ ROWS FROM CSV:


def read_rows(file_name):
    with open(f"{PATH}{file_name}.csv", mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
        return data


# FUNCTION CREATE ROWS IN CSV:
def create_rows_dict(file_name, fieldnames, data):
    with open(f"{PATH}{file_name}.csv", mode="a", newline='', encoding="utf8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for row in data:
            writer.writerow(row)

# FUNCTION FOR USING PANDAS (EXTRACT DATA FORM THE FILES)
# df_sale = pd.read_csv(f"{PATH}\\sale.csv")
# df_buy = pd.read_csv(f"{PATH}\\purchase.csv")
# df_bulk = pd.read_csv(f"{PATH}\\bulk.csv")

# # it = df_bulk.groupby("product_name")["peren"].sum()
# # print(df_buy)
# # print(it)
# print(df_bulk.groupby("product_name").sum())
# print(df_buy.groupby(["product_name"]).count())
