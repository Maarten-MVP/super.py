from datetime import date
import os
import datetime

date = date(
    date.today().year,
    date.today().month,
    date.today().day,
    ).strftime('%d/%m/%Y')

try:
    os.makedirs('data')
except FileExistsError:
    pass
    

path_current_dir = os.path.dirname(__file__)
path_file_date = os.path.join(path_current_dir, 'data', 'set_date.txt')

if not os.path.exists(path_file_date):
    date_file = open(path_file_date, 'w+')
    date_file.write(date)
    date_file.close()

def change_set_date_per_day(days):
    date_file = open(path_file_date, 'r')
    current_date = date_file.read()
    date_file.close()

    set_date = datetime.datetime.strptime(current_date, '%d/%m/%Y') + datetime.timedelta(days=days)
    date_file = open(path_file_date, 'w+')
    date_file.write(set_date.strftime('%d/%m/%Y'))
    date_file.close()
    return set_date.strftime('%d/%m/%Y')

def change_set_date_to_today():
    date_file = open(path_file_date, 'w+')
    date_file.write(date)
    date_file.close()

def change_set_date_to_yesterday():
    change_set_date_to_today()
    change_set_date_per_day(-1)

def change_set_date_to_tomorrow():
    change_set_date_to_today()
    change_set_date_per_day(1)



