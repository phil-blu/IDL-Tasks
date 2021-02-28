#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install pandas
import pandas as pd
#pip install -U selenium
from selenium import webdriver #+ download geckodriver, see [https://pypi.org/project/selenium/] 
from random import randint
from time import sleep
#pip install requests
import requests
#pip install beautifulsoup
from bs4 import BeautifulSoup
#pip install os
import os

#To read the csv file
file = pd.read_csv("version3.csv")


num = 0
index = []
for i in range(len(file)):
    index.append(num)
    num+=1
file['index'] = index
#file.head(3)

file_names = list(file['index'])

#To get all available links
links = file['Passport']
link_list = [link for link in links if not str(link)=='nan']
#link_list


#Downloading each image using unique links
for url in link_list:
    web = webdriver.Firefox("C:/Users/mine/Hamoye Internship/chromedriver_win32")#file path for webdriver
    web.get(url)

    sleep(randint(4,8))

    download_button = web.find_element_by_xpath('/html/body/div/div[1]/div/a')
    download_button.click()

    sleep(randint(4,7))

    img_url = web.current_url
    request = requests.get(img_url)
    soup = BeautifulSoup(request.text, 'lxml')

    
    #Saving the image with unique filenames
    for file_name in file_names:
        with open(file_name+"_PP"+'.jpg', 'wb') as f:
            image = requests.get(img_url)
            f.write(image.content)
    
    web.close()

