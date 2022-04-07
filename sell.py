# Imports
import csv
import os
import set_date

from rich.theme import Theme
from rich.console import Console

custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)

date_file = open(set_date.path_file_date, 'r')
date = date_file.read()
date_file.close()

path_current_dir = os.path.dirname(__file__)
path_file_inventory = os.path.join(path_current_dir, 'data', 'inventory.csv')
path_file_sell_ledger = os.path.join(path_current_dir, 'data', 'sell_ledger.csv')

last_id_inventory = -1
last_id_ledger = -1

def change_value_in_csv(row_id, column_nr, new_value):
    reader = csv.reader(open(path_file_inventory))
    lines = list(reader)

    lines[row_id][column_nr] = int(lines[row_id][column_nr]) + new_value

    writer = csv.writer(open(path_file_inventory, 'w', newline=''))
    writer.writerows(lines)

def check_if_product_has_stock(row_id, column_nr):
    reader = csv.reader(open(path_file_inventory))
    lines = list(reader)

    if lines[row_id][column_nr] == '0': return False
    else: return True

def sell(item, price):
    global last_id_inventory

    if os.path.exists(path_file_inventory):

        item_exists = False
        for row in open(path_file_inventory): last_id_inventory += 1

        reader = csv.reader(open(path_file_inventory, 'r'))

        row_counter = -1
        for row in reader:
            row_counter += 1
            if item in row:
                item_exists = True
                break

        if item_exists == True:
            has_stock = check_if_product_has_stock(row_counter, 1)
            if has_stock == False: return console.print('Product has no stock, buy some first', style='error')
            else: change_value_in_csv(row_counter, 1, -1)
        else: return console.print('Product does not exist in the store, buy some first', style='error')
    
    else:
        return console.print('No products in the store, buy some first', style='error')


    if os.path.exists(path_file_sell_ledger):
        global last_id_ledger
        for row in open(path_file_sell_ledger): last_id_ledger += 1

        with open(path_file_sell_ledger, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([last_id_ledger + 1, date, item, price])
        
            return console.print(f"1 {item} have been sold and removed from inventory", style='success')
    
    else:
        with open(path_file_sell_ledger, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Sell date', 'Item', 'Price' ])
            writer.writerow([1, date, item, price])

            return console.print(f"1 {item} have been sold and removed from inventory", style='success')

