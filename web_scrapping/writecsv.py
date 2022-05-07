import csv
from datetime import datetime



def write_to_csv(data):
    date = datetime.now().strftime('%Y-%m-%d')
    with open('./web_scrapping/data-temperature-{}.csv'.format(date),'a',newline='',encoding='utf-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(data)
