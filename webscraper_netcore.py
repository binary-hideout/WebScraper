from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("C:\Program Files\chromedriver")

#----------------------BestBuy----------------
def BestBuy():
    laptops = []

    driver.get("https://www.bestbuy.com.mx/c/laptops/c41")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    pag = 0
    while pag < 3: #cantidad de páginas con contenido
        for a in soup.findAll('div', attrs={'class':'product-line-item-line'}):
            name=a.find('div', attrs={'class':'product-title'})
            laptops.append(name.text)
        driver.find_element_by_xpath('//*[@id="plp-container"]/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/ul/li[7]/a').click()
        print(len(laptops))
        sleep(4)
        pag += 1

    #print(len(laptops))
    for lap in laptops:
        lap = lap.split("-")
    cels = BestBuyCels()
    teles = BestBuyTvs()
    df = pd.DataFrame({'Laptop Brand':[x for x in laptops[0]]}, {'Laptop Model':[x for x in laptops[0]]})
    df2 = pd.DataFrame({'Cellphone Name':cels}) 
    df3 = pd.DataFrame({'TV Name':teles})
    df.to_csv('laptops.csv', index=False, encoding='utf-8')
    df2.to_csv('cels.csv', index=False, encoding='utf-8')
    df3.to_csv('tvs.csv', index=False, encoding='utf-8')


def BestBuyCels():
    celulares = []

    driver.get("https://www.bestbuy.com.mx/c/telefonos-celulares/c53")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    pag = 0
    while pag < 10: #cantidad de páginas con contenido
        for a in soup.findAll('div', attrs={'class':'product-line-item-line'}):
            name=a.find('div', attrs={'class':'product-title'})
            celulares.append(name.text)
        driver.find_element_by_xpath('//*[@id="plp-container"]/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/ul/li[7]/a').click()
        print(len(celulares))
        sleep(6) 
        pag += 1
    print(len(celulares))

    return celulares

def BestBuyTvs():
    tvs = []

    driver.get("https://www.bestbuy.com.mx/c/pantallas/c35")

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    pag = 0
    while pag < 4: #cantidad de páginas con contenido

        for a in soup.findAll('div', attrs={'class':'product-line-item-line'}):
            name=a.find('div', attrs={'class':'product-title'})
            tvs.append(name.text)

        driver.find_element_by_xpath('//*[@id="plp-container"]/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/ul/li[10]/a').click()
        print(len(tvs))
        sleep(6) 
        pag += 1
    print(len(tvs))

    return tvs

#-----------------Amazon---------------

def Amazon():

    link1 = 'https://www.amazon.com.mx/gp/bestsellers/electronics/9687458011?ref_=Oct_s9_apbd_obs_hd_bw_bAZbaMl_S&pf_rd_r=HZ45SGH8T7GKZ74AS33S&pf_rd_p=4d9d93c0-fea5-5ed3-9cdc-da3baf21c408&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=9687458011'
    link2='https://www.amazon.com.mx/gp/bestsellers/electronics/9687458011/ref=zg_bs_pg_2/132-1166954-1513655?ie=UTF8&pg=2'
    driver.get(link1)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    celulares = []
    sleep(2)

    for a in soup.findAll('div', attrs={'class':'p13n-sc-truncated'}):

        #print(a.text)
        celulares.append(a.text)

    driver.get(link2)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    sleep(2)

    for a in soup.findAll('div', attrs={'class':'p13n-sc-truncated'}):

        #print(a.text)
        celulares.append(a.text)

    laps = AmazonLaptops()    
    #tvs = Amazontvs()
    print(len(celulares), 'cels')
    print(len(laps), 'laps')
    #print(len(tvs), 'tvs')

    if( ((len(celulares)) > 0) and (len(laps) > 0)):
        df = pd.DataFrame({'Cellphone Name':celulares})
        df.to_csv('celsAmazon.csv', index=False, encoding='utf-8')
        df2 = pd.DataFrame({'Laptop Name':laps})
        df2.to_csv('lapsAmazon.csv', index=False, encoding='utf-8')


def AmazonLaptops():
    link1='https://www.amazon.com.mx/gp/bestsellers/electronics/10189669011?ref_=Oct_s9_apbd_obs_hd_bw_bB7aoOB_S&pf_rd_r=5794MD68EN89CRQZWMDQ&pf_rd_p=58d7811c-7134-5551-b955-42726ceffed4&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=10189669011'
    link2='https://www.amazon.com.mx/gp/bestsellers/electronics/10189669011/ref=zg_bs_pg_2?ie=UTF8&pg=2'
    driver.get(link1)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    laptops = []
    sleep(2)

    
    for a in soup.findAll('div', attrs={'class':'p13n-sc-truncate-desktop-type2 p13n-sc-truncated'}):
        laptops.append(a.text)
    
    driver.get(link2)
    sleep(2)

    for a in soup.findAll('div', attrs={'class':'p13n-sc-truncate-desktop-type2 p13n-sc-truncated'}):
        laptops.append(a.text)

    return laptops
    
#Call the sites you want to get the info from
#BestBuy()
Amazon()