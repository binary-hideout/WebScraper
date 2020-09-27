from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\Program Files\chromedriver")

#BestBuy
laptops = []

driver.get("https://www.bestbuy.com.mx/c/laptops/c41")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.findAll('div', attrs={'class':'product-line-item-line'}):
    name=a.find('div', attrs={'class':'product-title'})
    laptops.append(name.text)

df = pd.DataFrame({'Laptop Name':laptops}) 
df.to_csv('products.csv', index=False, encoding='utf-8')