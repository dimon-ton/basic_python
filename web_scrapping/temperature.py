from tabnanny import check
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


all_data = {}

def write_to_csv(data):
    date = datetime.now().strftime('%Y-%m-%d')
    with open('./web_scrapping/data-temperature-{}.csv'.format(date),'a',newline='',encoding='utf-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(data)

def checkTemp(ID): 
    url = 'https://www.tmd.go.th/province.php?id=' + str(ID)

    webopen = urlopen(url) #เปิดเว็บโดยไม่ต้องเปิด Google Chrome ขึ้นมา
    html_page = webopen.read() #อ่านข้อมูลในเว็บ
    webopen.close()#ปิดเว็บ

    data = BeautifulSoup(html_page,'html.parser') #แปลงให้โค้ด bs4 ช่วยแปล
    try:
        temp = data.find('td',{'class':'strokeme'})
        title = data.find('span',{'class':'title'})

        city = title.text.strip()
        temp = temp.text

        all_data[city] = temp
    except:
        pass


for i in range(1,78):
    checkTemp(i)

for k,v in all_data.items():
    data = [k,v]
    write_to_csv(data)

print('saved')
  
    


