# Imports
from argparse import *
from functions import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    pass

if __name__ == "__main__":
    main()

parser = ArgumentParser(description="Welcome to this CLI, below several commands are shortly explained. For more information, please read file _readme")

subparsers = parser.add_subparsers(dest="command")

change_date = subparsers.add_parser("change_date", help="Used to change the system date. The system date is used in commands add_purchase & add_sale")
add_product_parser = subparsers.add_parser("add_product", help="Used to add a product to the list with products")
change_stock_parser = subparsers.add_parser("change_stock", help="Used to change the stock of a specific product")
add_purchase_parser = subparsers.add_parser("add_purchase", help="Used to add a purchase to the list with purchases and update the stock of the purchased product")
add_sale_parser = subparsers.add_parser("add_sale", help="Used to add a sale to the list with sales and update the stock of the sold product")
check_expiration_date_parser = subparsers.add_parser("check_expiration_date", help="Used to check on expired batches and remove these from the list with purchases")
csv_to_xlsx_parser = subparsers.add_parser("csv_to_xlsx", help="Used to export a csv file into an Excel file")
xlsx_to_csv_parser = subparsers.add_parser("xlsx_to_csv", help="Used to export an Excel file into a csv file")
visualize_stock_parser = subparsers.add_parser("visualize_stock", help="Used to visualize the current stock of each product in a bar diagram")

args = parser.parse_args()

if args.command == "change_date":
    advance_date_file()

if args.command == "add_product":
    add_product()

if args.command == "change_stock":
    change_stock()

if args.command == "add_purchase":
    create_purchase()

if args.command == "add_sale":
    create_sale()

if args.command == "check_expiration_date":
    check_expiration_date()

if args.command == "csv_to_xlsx":
    csv = input("Name of CSV file: ") + ".csv"
    xlsx = input("Name of Excel file: ") + ".xlsx"
    load_csv_to_xlsx(csv, xlsx)

if args.command == "xlsx_to_csv":
    xlsx = input("Name of Excel file: ") + ".xlsx"
    csv = input("Name of CSV file: ") + ".csv"
    load_xlsx_to_csv(xlsx, csv)

if args.command == "visualize_stock":
    visualize_stock()