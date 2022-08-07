import csv

def write(data=['ss-1001', '30.45', '50.44', '2022-08-06 15:05:05']):
    with open('result.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

