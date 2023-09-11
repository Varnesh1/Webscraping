from selenium import Webdriver
from bs4 import BeautifulSoup
import time
import csv
startingurl = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = webDriver.Chrome()
time.sleep(10)

temp_list = []

def scraping():
    headers = ['Name', 'Distance', 'Mass', 'Radius']
    star_data = []
    for i in range(0,1):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tbody in soup.find_all('tbody', attrs = {'class':'wikitable sortable jquery-tablesorter'}):
            tr = tbody.find_all('tr')
            temp_list = []
            for index, tr in enumerate(tr):
                if index ==0:
                    temp_list.append(li_tag_find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(tr.contents[0])
                    except:
                        temp_list.append('')
            star_data.append(temp_list)
        
    table_rows = star_table[1].find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)

        with open('scraped.csv', 'w') as o:
            csvwriter.writeow(headers)
            csv.writer(f)
            csv.writerows(star_data)
scraping()
        
