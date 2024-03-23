# Several imports
import csv
import datetime as dt
from os.path import exists
import pandas as pd
import matplotlib.pyplot as plt

"""
Creates a variable with the date of today
Turns the date of today into a string
"""
today_date = dt.date.today()
today_to_string = today_date.strftime('%Y-%m-%d')

"""
Opens text file date.txt
Reads the date which is in it
Makes a variable as date type
"""
with open('date.txt', 'r') as date:
    current_date = date.readline()
    current_date_to_date = dt.datetime.strptime(current_date, "%Y-%m-%d")

# The date of today and the advanced date printed so the user always knows these values
print(f'Date of today: {today_to_string}')
print(f'Advanced date: {current_date}')

#CHECK
def advance_date_file():
    """
    Asks for the number of days the date must change
    Adds the number of days to the current advanced date
    Convert the advanced date to a string
    Saves the advanced date to date.txt
    """
    try:
        days = int(input('With how many days must the current advanced date get changed? '))
        advanced_date = current_date_to_date + dt.timedelta(days=days)
        advanced_date_to_string = advanced_date.strftime('%Y-%m-%d')
        with open('date.txt', 'w') as date:
            date.write(advanced_date.strftime('%Y-%m-%d'))
        print(f'You changed the date with {days} day(s), the advanced date is now {advanced_date_to_string}')
    except ValueError:
        print('Please take a number without decimals for number of days')

# Couple of empty lists which are used in the functions below it
product_list = []
purchase_list = []
sale_list = []

def read_product():
    """
    Checks if products.csv already exists in the folder
    If file exists, the list product_list get emptied and filled with the information from csv file products.csv
    If file doesn't exist, nothing happens
    """
    file_exists = exists('products.csv')
    if file_exists:
        with open('products.csv', 'r', newline='', encoding='utf-8') as product_file:
            reader = csv.DictReader(product_file)
            product_list.clear()
            for product in reader:
                product_list.append(dict(product))
            return product_list

#CHECK
def save_product():
    """
    Saves list product_list to csv file products.csv
    """
    fieldnames = product_list[0].keys()
    with open('products.csv', 'w', newline='') as product_file:
        writer = csv.DictWriter(product_file, fieldnames=fieldnames)
        writer.writeheader()
        for product in product_list:
            writer.writerow(product)

#CHECK
def read_purchase():
    """
    Checks if purchases.csv already exists in the folder
    If file exists, the list purchase_list get emptied and filled with the information from csv file purchases.csv
    If file doesn't exist, nothing happens
    """
    file_exists = exists('purchases.csv')
    if file_exists:
        with open('purchases.csv', 'r', newline='', encoding='utf-8') as purchase_file:
            reader = csv.DictReader(purchase_file)
            purchase_list.clear()
            for purchase in reader:
                purchase_list.append(dict(purchase))
            return purchase_list

#CHECK
def save_purchase():
    """
    Saves list purchase_list to csv file purchases.csv
    """
    fieldnames = purchase_list[0].keys()
    with open('purchases.csv', 'w', newline='') as purchase_file:
        writer = csv.DictWriter(purchase_file, fieldnames=fieldnames)
        writer.writeheader()
        for purchase in purchase_list:
            writer.writerow(purchase)

#CHECK
def read_sale():
    """
    Checks if sales.csv already exists in the folder
    If file exists, the list sale_list get emptied and filled with the information from csv file sales.csv
    If file doesn't exist, nothing happens
    """
    file_exists = exists('sales.csv')
    if file_exists:
        with open('sales.csv', 'r', newline='', encoding='utf-8') as sales_file:
            reader = csv.DictReader(sales_file)
            sale_list.clear()
            for sale in reader:
                sale_list.append(dict(sale))
            return sale_list

#CHECK
def save_sale():
    """
    Saves list sale_list to csv file sales.csv
    """
    fieldnames = sale_list[0].keys()
    with open('sales.csv', 'w', newline='') as sales_file:
        writer = csv.DictWriter(sales_file, fieldnames=fieldnames)
        writer.writeheader()
        for sale in sale_list:
            writer.writerow(sale)

#CHECK
def add_product():
    """
    Loads all products from products.csv in the product_list
    Creates dictionary product with several variables and adds the dictionary to list product_list
    Saves the product_list back to products.csv
    """
    read_product()
    product = {}
    product['product_id'] = input('Product ID: ')
    product['product_name'] = input('Product name: ')
    product['purchase_price'] = input('Purchase price: ')
    product['sell_price'] = input('Sell price: ')
    product['stock'] = 0
    try: 
        product['purchase_price'] = round(float(product['purchase_price']), 2)
        product['sell_price'] = round(float(product['sell_price']), 2)
    except ValueError:
        print('Please take a number for purchase and sell price')
        return
    product_list.append(product)
    print(f'Added product {product['product_name']} with ID {product['product_id']} to the list with products')
    save_product()

#CHECK
def create_purchase():
    """
    Loads all products from products.csv in the product_list
    Loads all purchases from purchases.csv in the purchase_list
    Creates dictionary purchase with several variables and adds the dictionary to list purchase_list, the information is partly based on the given product_id
    Saves the product_list back to products.csv
    Saves the purchase_list back to purchases.csv
    """
    read_product()
    read_purchase()
    purchase = {}
    purchase['product_id'] = input('Product ID: ')
    found_product_id = False
    for product in product_list:
        if purchase['product_id'] == product['product_id']:
            purchase['batch_ID'] = input('Batch ID: ')
            purchase['product_name'] = product['product_name']
            purchase['purchase_price'] = product['purchase_price']
            purchase['quantity'] = input('Quantity: ')
            purchase['purchase_date'] = current_date
            purchase['expiration_date'] = input('Expiration date (yyyy-mm-dd): ')
            product['stock'] = int(product['stock']) + int(purchase['quantity'])
            purchase_list.append(purchase)
            print(f'Added batch ID {purchase['batch_ID']} to the list with purchases and updated the stock of {purchase['product_name']}')
            found_product_id = True
            break
    if not found_product_id:
        print(f"Product ID {purchase['product_id']} wasn't found")
    save_product()
    save_purchase()

#CHECK
def create_sale():
    """
    Loads all products from products.csv in the product_list
    Loads all sales from sales.csv in the sale_list
    Creates dictionary sale with several variables 
    Checks if there is enough in stock to sell
    If stock is too low, this is shown to the user and nothing happens with the dictionary
    If stock is high enough, stock get updated in product_list and dictionary sale get added to list sale_list
    Saves the product_list back to products.csv
    Saves the sale_list back to sales.csv    
    """
    read_product()
    read_sale()
    sale = {}
    sale['product_id'] = input('Product ID: ')
    found_product_id = False
    try:
        for product in product_list:
            if sale['product_id'] == product['product_id']:
                sale['product_name'] = product['product_name']
                sale['sell_price'] = product['sell_price']
                sale['quantity'] = input('Quantity: ')
                sale['sell_date'] = current_date
                if int(product['stock']) < int(sale['quantity']):
                    print(f'Stock too low, only {product['stock']} available')
                else:
                    product['stock'] = int(product['stock']) - int(sale['quantity'])
                    sale_list.append(sale)
                    print(f'Added the sale to the list with sales and updated the stock of product {sale['product_name']}')
                found_product_id = True
                break
        if not found_product_id:
            print(f"Product ID {sale['product_id']} wasn't found")
    except ValueError:
        print('Please take a number for quantity')
    save_product()
    save_sale()    

#CHECK
def change_stock():
    """
    Loads all products from products.csv in the product_list
    Looks for a specific ID in list product_list
    Changes stock 
    Saves the product_list back to products.csv
    """
    read_product()
    found_product_id = False
    try:
        product_id = input('Product ID: ')
        for product in product_list:
            if product['product_id'] == product_id:
                quantity = int(input('Quantity: '))
                product['stock'] = int(product['stock']) + int(quantity)
                print(f"The stock of product ID {product_id} is changed by {quantity} and now it's {product['stock']}")
                found_product_id = True
                break
        if not found_product_id:
            print(f"Product ID {product_id} wasn't found")
        save_product()
    except ValueError:
        print('Please take a number for quantity')

#CHECK
def check_expiration_date():
    """
    Loads all purchases from purchase.csv in the purchase_list
    Checks all purchases in purchase_list if expiration_date was before the date of today
    Removes the batch from purchase_list if it expired
    Saves the purchase_list back to purchase.csv
    """
    read_purchase()
    for purchase in purchase_list:
        if purchase['expiration_date'] < today_to_string:
            purchase_list.remove(purchase)
            print(f'Batch {purchase['batch_ID']} has been thrown away')
    save_purchase()

#CHECK
def load_csv_to_xlsx(csv_file, xlsx_file):
    """
    Asks for the name of the csv file which needs to be exported
    Asks for the desired name of the xlsx file
    Exports the csv file to an xlsx file
    """
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(xlsx_file, index=False)
        print(f'The csv file {csv_file} is exported to the xlsx file {xlsx_file}')
    except FileNotFoundError:
        print(f'csv file {csv_file} was not found')

#CHECK
def load_xlsx_to_csv(xlsx_file, csv_file):
    """
    Asks for the name of the xlsx file which needs to be exported
    Asks for the desired name of the csv file
    Exports the xlsx file to a csv file
    """
    try:
        df = pd.read_excel(xlsx_file)
        df.to_csv(csv_file, index=False)
        print(f'The xlsx file {xlsx_file} is exported to the csv file {csv_file}')
    except FileNotFoundError:
        print(f'xlsx file {xlsx_file} was not found')

#CHECK
def visualize_stock():
    """
    Visualizes the stock of all products by creating a horizontal bar diagram
    Takes the values in column stock in file products.csv and show these on the X-axis
    Takes the values in column product_name in file products.csv and show these on the Y-axis
    """
    df = pd.read_csv('products.csv')
    data = df['stock']
    plt.barh(df.product_name, data)
    plt.xlabel('Stock per product')
    plt.ylabel('Product')
    plt.title('Stock')
    plt.show()

