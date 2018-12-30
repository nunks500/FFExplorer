import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from multiprocessing import Queue
import os
import sys

if getattr(sys, 'frozen', False):
    cacert = os.path.join(os.path.dirname(sys.executable) + '/lib/certifi', 'cacert.pem')
else:
    cacert = requests.cert.where()

def trade_spider():

    print("Enter machine name(cdx12, obx31, etc): ")
    maquina = input()

    print("Enter subfolder(pt, uk, etc): ")
    subfolder = input()

    print("Enter number of Max Pages to search in clothes/shoes/purses tab: ")
    max_pages = int(input())

    print("In case of any problems, troubleshoot, contact Joel Dinis for more information")
    print("------WELCOME TO FF EXPLORER PLUGIN EDITION------")
    page = 1
    driver = webdriver.Chrome()

    url_novidades = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/sets/women/novidades-da-moda-1.aspx"
    url5 = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/women/accessories-all-1/items.aspx"
    url6 = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/women/jewellery-1/items.aspx"
    url7 = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/women/vintage-archive-1/items.aspx"

    source_code_novidades = requests.get(url_novidades, verify=cacert)
    source_code5 = requests.get(url5, verify=cacert)
    source_code6 = requests.get(url6, verify=cacert)
    source_code7 = requests.get(url7, verify=cacert)

    plain_text_novidades = source_code_novidades.text
    plain_text5 = source_code5.text
    plain_text6 = source_code6.text
    plain_text7 = source_code7.text

    soup_novidades = BeautifulSoup(plain_text_novidades)
    soup7 = BeautifulSoup(plain_text7)
    soup6 = BeautifulSoup(plain_text6)
    soup5 = BeautifulSoup(plain_text5)

    print('------------Novidades------------')
    for link in soup_novidades.findAll('a', {'class': 'listing-item-link no-underline'}):
        href = link.get('href')
        driver.get("https://" + maquina + "-portal.fftech.info" + href)
        html = driver.execute_script("return document.documentElement.innerHTML")
        soup_look_woman = BeautifulSoup(html)
        print('Checking: ' + href)
        if soup_look_woman.findAll('h3', text='Shop the look') != []:
            print('Success: ' + href)

    print('------------Accessories------------')
    for link in soup5.findAll('a', {'class': 'listing-item-link no-underline'}):
        href = link.get('href')
        driver.get("https://" + maquina + "-portal.fftech.info" + href)
        html = driver.execute_script("return document.documentElement.innerHTML")
        soup_look_man = BeautifulSoup(html)
        print('Checking: ' + href)
        if soup_look_man.findAll('h3', text='Shop the look') != []:
            print('Success: ' + href)

    print('------------Jewelry------------')
    for link in soup6.findAll('a', {'class': 'listing-item-link no-underline'}):
        href = link.get('href')
        driver.get("https://" + maquina + "-portal.fftech.info" + href)
        html = driver.execute_script("return document.documentElement.innerHTML")
        soup_look_man = BeautifulSoup(html)
        print('Checking: ' + href)
        if soup_look_man.findAll('h3', text='Shop the look') != []:
            print('Success: ' + href)

    print('------------Vintage------------')
    for link in soup7.findAll('a', {'class': 'listing-item-link no-underline'}):
        href = link.get('href')
        driver.get("https://" + maquina + "-portal.fftech.info" + href)
        html = driver.execute_script("return document.documentElement.innerHTML")
        soup_look_man = BeautifulSoup(html)
        print('Checking: ' + href)
        if soup_look_man.findAll('h3', text='Shop the look') != []:
            print('Success: ' + href)

    while page <= max_pages:
        print('Page: ' + str(page) + ' max_pages: ' + str(max_pages))
        url = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/women/clothing-1/items.aspx?page=" + str(page)
        #url = "https://cdx12-portal.fftech.info/pt/shopping/women/saint-laurent-heart-shaped-cape-item-11596263.aspx?storeid=9306&from=search"
        url2 = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/men/clothing-2/items.aspx?page=" + str(page)
        url3 = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/women/shoes-1/items.aspx?page=" + str(page)
        url4 = "https://" + maquina + "-portal.fftech.info/" + subfolder + "/shopping/women/bags-purses-1/items.aspx?page=" + str(page)

        source_code = requests.get(url)
        source_code2 = requests.get(url2)
        source_code3 = requests.get(url3)
        source_code4 = requests.get(url4)

        plain_text = source_code.text
        plain_text2 = source_code2.text
        plain_text3 = source_code3.text
        plain_text4 = source_code4.text

        soup4 = BeautifulSoup(plain_text4)
        soup3 = BeautifulSoup(plain_text3)
        soup2 = BeautifulSoup(plain_text2)
        soup = BeautifulSoup(plain_text)

        print('------------Clothing-Woman-----------')
        for link in soup.findAll('a', {'class': 'listing-item-link no-underline'}):
             href = link.get('href')
             driver.get("https://" + maquina + "-portal.fftech.info" + href)
             html = driver.execute_script("return document.documentElement.innerHTML")
             soup_look_woman = BeautifulSoup(html)
             print('Checking: ' + href)
             if soup_look_woman.findAll('h3', text='Shop the look') != []:
                 print('Success: ' + href)

        print('------------Clothing-Man-----------')
        for link in soup2.findAll('a', {'class': 'listing-item-link no-underline'}):
            href = link.get('href')
            driver.get("https://" + maquina + "-portal.fftech.info" + href)
            html = driver.execute_script("return document.documentElement.innerHTML")
            soup_look_man = BeautifulSoup(html)
            print('Checking: ' + href)
            if soup_look_man.findAll('h3', text='Shop the look') != []:
               print('Success: ' + href)

        print('------------Shoes-Woman----------')
        for link in soup3.findAll('a', {'class': 'listing-item-link no-underline'}):
            href = link.get('href')
            driver.get("https://" + maquina + "-portal.fftech.info" + href)
            html = driver.execute_script("return document.documentElement.innerHTML")
            soup_look_man = BeautifulSoup(html)
            print('Checking: ' + href)
            if soup_look_man.findAll('h3', text='Shop the look') != []:
               print('Success: ' + href)

        print('------------Purses-Woman----------')
        for link in soup4.findAll('a', {'class': 'listing-item-link no-underline'}):
            href = link.get('href')
            driver.get("https://" + maquina + "-portal.fftech.info" + href)
            html = driver.execute_script("return document.documentElement.innerHTML")
            soup_look_man = BeautifulSoup(html)
            print('Checking: ' + href)
            if soup_look_man.findAll('h3', text='Shop the look') != []:
               print('Success: ' + href)

        page += 1

trade_spider()