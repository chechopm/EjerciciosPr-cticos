"""Module to compute the total sales from a catalogue and a record of sales."""

import sys
import time
import json

def get_name_files():
    """Gets the name of the files from the command line."""
    if len(sys.argv) > 2:
        file_name_catalogue = sys.argv[1]
        file_name_records = sys.argv[2]
        return file_name_catalogue, file_name_records
    print("ERROR: Please provide the name of the files as an argument.")
    return "", ""

def get_data_file(file_name):
    """Reads the data from the file."""
    full_file_name = "ArchivosApoyo/" + file_name
    data_json = []
    try:
        with open(full_file_name, "r", encoding="utf-8") as file:
            data_json = json.load(file)
    except FileNotFoundError:
        print("File not found")
    return data_json

def calculate_total_sales(data_file_catalogue, data_file_records):
    """Calculates the total sales from the data."""
    total_sales = 0
    for record in data_file_records:
        product_id = record.get("Product")
        quantity = record.get("Quantity")
        if product_id is not None and quantity is not None:
            for product in data_file_catalogue:
                if product["title"] == product_id:
                    total_sales += product["price"] * quantity
    return total_sales

def print_results(total_sale, file_write):
    """Prints the results of Total Sales."""
    line = f"Total Sales: ${total_sale:.2f}"
    print(line)
    file_write.write(line + "\n")

def main():
    """Principal Main Compute Sales Function."""
    start_time = time.time()
    file_name_catalogue, file_name_records = get_name_files()
    with open ("SalesResults.txt", "w", encoding="utf-8") as file_write:
        if file_name_catalogue != "" and file_name_records != "":
            data_file_catalogue = get_data_file(file_name_catalogue)
            data_file_records = get_data_file(file_name_records)
            total_sales= calculate_total_sales(data_file_catalogue, data_file_records)
            print_results(total_sales, file_write)
        end_time = time.time()
        string_time = "Execution Time " + str(end_time - start_time) + "s"
        print(string_time)
        file_write.write(string_time + "\n")
        file_write.close()

if __name__ == "__main__":
    sys.exit(main())
