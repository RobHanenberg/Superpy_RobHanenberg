Hi user, 

Welcome to this application which was created for a supermarket to keep track of their inventory and product flow.

The application is a command line interface (CLI) which can be used in a terminal (for example CMD or Powershell). 
The application contains several options which can be started with specific commands.
There is a help section in the application, with a short explanation for each command.

How to use the applicatin:
    Open the terminal
    Make sure the path leads to the right folder, which is called "superpy"
        For example: C:\users\user\documents\superpy
    To open the help section:
        Typ in the same line as the path " py .\main.py -h"
        The total line should now look like:
            C:\users\user\documents\superpy py .\main.py -h
        Press <enter>    
    To start a command:
        Typ in the same line as the path " py .\main.py " followed by the command
            For example: py .\main.py add_product
        The total line should now look like:
            C:\users\user\documents\superpy py .\main.py add_product
    Everything OK? Then press <enter> and the command will start

In most of the commands, input from the user is requested. If it is, typ your input and press <enter>.
Once the command is finished, the application will show what is done

Below is a list with all commands:
1. Change the system date
    It is possible to do some 'time travelling' by changing the system date. The system date is used in other commands like add_purchase & add_sale, so a purchase from yesterday can still be registrated on the right date.
    Command: change_date
    Requested: 
        With how many days must the current system date change.
2. Add a new product to the list with products
    Command: add_product
    Requested:
        Product ID - take a non existing product ID (see CSV file products for the existing ones) to avoid doubling
        Product name
        Purchase price
        Sell price
3. Add a new purchase
    Take care the system date is automatically used as date of purchase
    Command: add_purchase
    Requested:
        Product ID - the application uses this ID to find the purchased product in the list with products
        Batch ID - take a non existing batch ID (see CSV file purchases) to avoid doubling
        Quantity - put in the purchased quantity
        Expiration date - put in the expiration date in the format yyyy-mm-dd
4. Add a new sale
    Take care the system date is automatically used as selling date
    Command: add_sale
    Requested:
        Product ID - the application uses this ID to find the sold product in the list with products
        Quantity - put in the sold quantity
5. Change the stock of one of the products
    Command: change_stock
    Requested:
        Product ID - the application uses this ID to find the product in the list with products
        Quantity - with how many must the current stock change
6. Remove expired batches
    All batches in CSV file purchases get compared on the expiration date to the date of today (not the system date) and get removed if it is expired
    Command: check_expiration_date
7. Show a graph of the current stock of each product
    Command: visualize_stock
8. Export a CSV file to an Excel file
    The information about products, purchases and sales are saved in CSV files, these can be exported to Excel files so it is easier to make changes or other visualizations
    Command: csv_to_xlsx
    Requested:
        Name of CSV file - put in the name of an existing CSV file in the folder superpy
        Name of Excel file
9. Export an Excel file to a CSV file
    It is also possible to export an excel file back to a CSV file. In case of CSV files products, purchases and sales, take care the headers are the same as it originally was.
    Command: xlsx_to_csv
    Explanation:
        Name of Excel file - put in the name of an existing Excel file in the folder superpy
        Name of CSV file

Enjoy!
