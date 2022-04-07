import csv
import os
import set_date
from rich.table import Table
from rich.console import Console
import datetime

table = Table(title='report table', row_styles=['','on grey19'])
console = Console()

date_file = open(set_date.path_file_date, 'r')
date = date_file.read()
date_file.close()

yesterday = (datetime.datetime.strptime(set_date.date, '%d/%m/%Y') - datetime.timedelta(days=1)).strftime('%d/%m/%Y')

path_current_dir = os.path.dirname(__file__)

try:
    path_file_inventory = os.path.join(path_current_dir, 'data', 'inventory.csv')
    path_file_sell_ledger = os.path.join(path_current_dir, 'data', 'sell_ledger.csv')
    inventory_reader = csv.reader(open(path_file_inventory, 'r'))
    inventory_list = list(inventory_reader)
    sales_reader = csv.reader(open(path_file_sell_ledger, 'r'))
    sales_list = list(sales_reader)
except FileNotFoundError:
    inventory_list = []
    sales_list = []

prices = {}
for product in inventory_list[1:]:
    prices[product[2]] = product[3]

def report_table(file, filter):
        path_file = os.path.join(path_current_dir, 'data', file + '.csv')
        reader = csv.reader(open(path_file, 'r'))
        data = list(reader)

        if file == 'inventory':

            if filter == 'none':

                table.add_column(data[0][0], style='white')
                table.add_column(data[0][1], style='cyan', justify='center')
                table.add_column(data[0][2], style='magenta')
                table.add_column(data[0][3], style='cyan')
                table.add_column(data[0][4], style='white', justify='right')

                for row in data[1:]:
                    table.add_row(row[0], row[1], row[2], '€ ' + row[3], row[4])
                console.print(table)
                return
            
            else:
                console.print('It is not possible to add a date filter to Inventory report', style='red')

        elif file == 'sell_ledger' or 'buy_ledger':
            filtered_data = [data[0]] + [record for record in data if record[1] == set_date.date]

            if filter.lower() == 'none':
                table.add_column(data[0][0], style='white')
                table.add_column(data[0][1], style='cyan', justify='center')
                table.add_column(data[0][2], style='magenta')
                table.add_column(data[0][3], style='cyan')

                for row in data[1:]:
                    table.add_row(row[0], row[1], row[2], '€ ' + row[3])
                console.print(table)
                return

            if filter.lower() == 'today':
                filtered_data = [data[0]] + [record for record in data if record[1] == set_date.date]

                print(filtered_data)

                table.add_column(filtered_data[0][0], style='white')
                table.add_column(filtered_data[0][1], style='cyan', justify='center')
                table.add_column(filtered_data[0][2], style='magenta')
                table.add_column(filtered_data[0][3], style='cyan')

                for row in filtered_data[1:]:
                    table.add_row(row[0],row[1],row[2], '€ ' + row[3])
                console.print(table)
                return

            if filter.lower() == 'yesterday':
                filtered_data = [data[0]] + [record for record in data if record[1] == yesterday]

                table.add_column(filtered_data[0][0], style='white')
                table.add_column(filtered_data[0][1], style='cyan', justify='center')
                table.add_column(filtered_data[0][2], style='magenta')
                table.add_column(filtered_data[0][3], style='cyan')

                for row in filtered_data[1:]:
                    table.add_row(row[0],row[1],row[2], '€ ' + row[3])
                console.print(table)
                return

def report_revenue(filter):
    revenue = 0

    if filter == 'none':
        global sales_list

        for sale in sales_list[1:]:
            revenue += int(sale[3])
        return revenue
    elif filter == 'yesterday':
        filtered_sales_list = [sale for sale in sales_list if sale[1] == yesterday]
        
        for sale in filtered_sales_list:
            revenue += int(sale[3])
        return revenue
    
    elif filter == 'today':
        filtered_sales_list = [sale for sale in sales_list if sale[1] == set_date.date]

        for sale in filtered_sales_list:
            revenue += int(sale[3])
        return revenue

def report_profit(filter):
    profit = 0
    global prices

    if filter == 'none':
        global inventory_list
        global sales_list
        
        for sale in sales_list[1:]:
            if sale[2] in prices.keys():
                profit += int(sale[3]) - int(prices[sale[2]])
        return profit

    elif filter == 'yesterday':
        filtered_sales_list = [sale for sale in sales_list if sale[1] == yesterday]
        
        for sale in filtered_sales_list:
            if sale[2] in prices.keys():
                profit += int(sale[3]) - int(prices[sale[2]])
        return profit
    
    elif filter == 'today':
        filtered_sales_list = [sale for sale in sales_list if sale[1] == set_date.date]

        for sale in filtered_sales_list:
            if sale[2] in prices.keys():
                profit += int(sale[3]) - int(prices[sale[2]])
        return profit

    elif isinstance(filter, int):
        filtered_sales_list = [sale for sale in sales_list if sale[1] == (datetime.datetime.strptime(set_date.date, '%d/%m/%Y') - datetime.timedelta(days=filter)).strftime('%d/%m/%Y')]

        for sale in filtered_sales_list:
            if sale[2] in prices.keys():
                profit += int(sale[3]) - int(prices[sale[2]])
        return profit


