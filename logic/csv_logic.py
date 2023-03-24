# Imports
import csv
import os
from other.settings import PATH_CSV

# Function for creating the CSV folder:


def create_csv_folder(folder):
    os.makedirs(folder)


# Function for creating a CSV file:
def create_csv(csv_files):
    for file in csv_files:
        with open(f"{PATH_CSV}{file[0]}.csv", mode="w", newline='', encoding="utf8") as csv_file:
            fieldnames = file[1:len(file)]
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames)
            writer.writeheader()


# Function for reading a CSV file:


def read_rows(file_name):
    with open(f"{PATH_CSV}{file_name}.csv", mode="r", encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
        return data


# Function for creating a row in a CSV file:
def create_rows(file_name, fieldnames, data):
    with open(f"{PATH_CSV}{file_name}.csv", mode="a", newline='', encoding="utf8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for row in data:
            writer.writerow(row)
