# Imports
import argparse
import os

import buy
import set_date
import sell
import report
import graph

from rich.theme import Theme
from rich.console import Console

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    pass


if __name__ == "__main__":
    main()

custom_theme = Theme({'success': 'green', 'error': 'red'})
console = Console(theme=custom_theme)

path_current_dir = os.path.dirname(__file__)
path_file_inventory = os.path.join(path_current_dir, 'data', 'inventory.csv')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='subparser_name')

buy_parser = subparsers.add_parser("buy", help="add an item to the inventory. Expected arguments in the correct order: productname price expiration-date")
buy_parser.add_argument("name", help="name of the product")
buy_parser.add_argument("price", help="price of the product", type=int)
buy_parser.add_argument("expiration", help="expiration date of the product")

date_parser = subparsers.add_parser("set-date", 
    help="set the working date. Default is Today. Type keywords such as today, tommorow, yesterday or number of days you want to go back (ex. -1 is yesterday) or advance (ex. 1 is tomorrow)"
    )
date_parser.add_argument("--keyword", 
    help="add a predefined keyword (options: today, tomorrow or yesterday)", 
    type=str
    )
date_parser.add_argument("--days", 
    help="add a number, representing the number of days you want to advance or go back", 
    type=int
    )

sell_parser = subparsers.add_parser("sell", help="sell an item from the store. Expected arguments in the correct order: productname price")
sell_parser.add_argument("name", help="name of the product")
sell_parser.add_argument("price", help="price of the product", type=int)

report_parser = subparsers.add_parser("report", help="print a report of the \'inventory\',  \'buy_ledger\' or  \'sell_ledger\'")
report_parser.add_argument('type', help='possible reports: inventory, buy_ledger, sell_ledger, revenue, profit, graph_profit (graph of the profit of past 5 days)', type=str)
report_parser.add_argument('--date', help='optional: add \'today\' or \'yesterday\' to specify the report\'s timeframe', default='none')

args = parser.parse_args()

if args.subparser_name == 'buy':
    if args.name and args.price and args.expiration:
        buy.buy(args.name, args.price, args.expiration)
        console.print(f"1 {args.name} have been added to the inventory", style='success')

elif args.subparser_name == 'set-date':
    if args.keyword == 'today':
        set_date.change_set_date_to_today()
        console.print('Working date set to today', style='success')
    elif args.keyword == 'tomorrow':
        set_date.change_set_date_to_tomorrow()
        console.print('Working date set to tomorrow', style='success')
    elif args.keyword == 'yesterday':
        set_date.change_set_date_to_yesterday()
        console.print('Working date set to yesterday', style='success')
    elif args.days:
        console.print(f'You have moved to {set_date.change_set_date_per_day(args.days)}', style='success')

elif args.subparser_name == 'sell':
    sell.sell(args.name, args.price)

elif args.subparser_name == 'report':

    if args.type == 'revenue':
        console.print(f'[bold cyan]revenue[/]: €{report.report_revenue(args.date)}')
    elif args.type == 'profit':
        console.print(f'[bold cyan]profit[/]: €{report.report_profit(args.date)}')
    elif args.type == 'graph_profit':
        graph.graph()
    elif args.type == 'sell_ledger' or 'buy_ledger' or 'inventory':
        report.report_table(args.type, args.date.lower())

    



        








    














