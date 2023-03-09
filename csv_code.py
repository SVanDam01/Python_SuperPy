# Imports
import csv
import os
from settings import PATH

file_name = "purchase"

# data = [1, "2023-01-12", "Fruit", "Citroen", 3, 0.85, "2023-01-20"]
# data1 = [2, "2023-01-24", "Fruit", "Citroen", 3, 1.85, "2023-01-20"]


# FUNCTIE AANMAKEN CSV FOLDER:


def create_csv_folder():
    isExist = os.path.exists(PATH)
    if not isExist:
        os.makedirs(PATH)


# FUNCTIE AANMAKEN CSV FILES:


def create_csv(csv_files):
    for file in csv_files:
        with open(f"{PATH}\{file[0]}.csv", mode="w", newline='', encoding="utf8") as csv_file:
            fieldnames = file[1:len(file)]
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()


# FUNCTIE AANMAKEN REGELS CSV:
# data_sale = [1, 1, "2023-01-12", "Fruit", "Citroen", 3, 0.85]


def create_rows(file_name, data):
    with open(f"{PATH}\{file_name}.csv", mode="a", newline='', encoding="utf8") as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerow(data)


# create_rows("sale", data_sale)

# FUNCTIE LEZEN REGELS CSV:


def read_rows(file_name):
    with open(f"{PATH}\{file_name}.csv", mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter='\t')
        data = list(reader)
        print(data)
