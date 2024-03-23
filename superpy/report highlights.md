# **Report highlights**
## Introduction
In this report some technical highlights of the code in folder *superpy* are described. Below the three highlight are already listed:
1. Saving lists without overwriting
2. Message product ID was not found 
3. Stock is too low

## Saving lists without overwriting
In the beginning I was struggling with overwriting the CSV files without losing old data. I solved this by adjusting the following steps:
- Read the existing data from CSV file *products.csv* in the `product_list` with function `read_product`.
    - `product_list` get emptied.
    - Data in *products.csv* get added to `product_list`.
- Another part of a function runs.
- Data in `product_list` is written back to *products.csv* with function `save_product`.

## Message product ID was not found
In several functions, a product ID is asked to the user. The function starts looking for this product ID in `product_list`. The function should only find once the the product ID, see I added the variable `found_product_id`. Which get value `False` when the function starts and turn into `True` when the given product ID is found in `product_list`. In case the product ID is not found, this is displayed in a message:
```python
if not found_product_id:
    print(f"Product ID {purchase['product_id']} wasn't found")
```

## Stock is too low
When the user wants to create a new sale, function `create_sale()` is used. This functions retrieves the product data from the given product ID and checks if there is enough in stock compared with the quantity of the sale.
```python
if int(product['stock']) < int(sale['quantity']):
    print(f'Stock too low, only {product['stock']} available')
```
Only in case the stock is high enough, the sale is added to the `sale_list` and the stock of the product get updated in `product_list`.
```python
else:
    product['stock'] = int(product['stock']) - int(sale['quantity'])
    sale_list.append(sale)
    print(f"Added the sale to the list with sales and updated the stock of product {sale['product_name']}")
```
