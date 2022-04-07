# Imports
import csv
import os
import set_date

date_file = open(set_date.path_file_date, 'r')
date = date_file.read()
date_file.close()

path_current_dir = os.path.dirname(__file__)
path_file_inventory = os.path.join(path_current_dir, 'data', 'inventory.csv')
path_file_buy_ledger = os.path.join(path_current_dir, 'data', 'buy_ledger.csv')

last_id_inventory = -1
last_id_ledger = -1

def change_value_in_csv(row_id, column_nr, new_value):
    reader = csv.reader(open(path_file_inventory))
    lines = list(reader)

    lines[row_id][column_nr] = int(lines[row_id][column_nr]) + new_value

    writer = csv.writer(open(path_file_inventory, 'w', newline=''))
    writer.writerows(lines)

def buy(item, price, expiration_date):
    global last_id_inventory

    if os.path.exists(path_file_inventory):
        global last_id_inventory

        item_exists = False
        for row in open(path_file_inventory): last_id_inventory += 1

        reader = csv.reader(open(path_file_inventory, 'r'))

        row_counter = -1
        for row in reader:
            row_counter += 1
            if item in row:
                item_exists = True
                break

        with open(path_file_inventory, 'a', newline='') as csvfile:
            if item_exists: 
                change_value_in_csv(row_counter, 1, 1)
            else:
                writer = csv.writer(csvfile)
                writer.writerow([last_id_inventory + 1, int(1), item, price, expiration_date])
    else:
        with open(path_file_inventory, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Count', 'Item', 'Price', 'Expiration date'])
            writer.writerow([1, int(1), item, price, expiration_date])

    if os.path.exists(path_file_buy_ledger):
        global last_id_ledger
        for row in open(path_file_buy_ledger): last_id_ledger += 1

        with open(path_file_buy_ledger, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([last_id_ledger + 1, date, item, price])
    
    else:
        with open(path_file_buy_ledger, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Buy date', 'Item', 'Price'])
            writer.writerow([1, date, item, price])