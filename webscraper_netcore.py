from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:\Program Files\chromedriver")

#BestBuy
def BestBuy():
    laptops = []

    driver.get("https://www.bestbuy.com.mx/c/laptops/c41")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    pag = 0
    while pag < 4: #cantidad de páginas con contenido
        for a in soup.findAll('div', attrs={'class':'product-line-item-line'}):
            name=a.find('div', attrs={'class':'product-title'})
            laptops.append(name.text)
        driver.find_element_by_xpath('//*[@id="plp-container"]/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/ul/li[7]/a').click()
        print(len(laptops))
        sleep(4)
        pag += 1
    print(len(laptops))

    df = pd.DataFrame({'Laptop Name':laptops}) 
    df.to_csv('products.csv', index=False, encoding='utf-8')
    
    BestBuy()