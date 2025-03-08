from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
 
#--| Setup
options = Options()
#options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
#--| Parse or automation
browser.get('https://www.macrotrends.net/stocks/charts/MSFT/microsoft/income-statement?freq=A')
time.sleep(3)
soup = BeautifulSoup(browser.page_source, 'lxml')
table = soup.select('#contentjqxgrid > div.jqx-grid-content.jqx-widget-content')
#print(table)
 
# First row test
#revenue = soup.select('#row0jqxgrid')
#print(revenue)
first_val = soup.select('#row0jqxgrid > div:nth-child(3) > div')
#print('-' * 20)
print(first_val[0].text)