#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver 
from random import randint
from time import sleep
import requests
#from bs4 import BeautifulSoup

url = "https://paystack.com/pay/bk7g6d25-q"
def get_acct(link):
    web = webdriver.Firefox("C:/Users/mine/Hamoye Internship/chromedriver_win32")#edit webdriver path
    web.get(link)

    first_name = "Linda"
    fname = web.find_element_by_xpath('//*[@id="customer-first-name"]')
    fname.send_keys(first_name)

    sleep(randint(4,8))

    lastname = "Ezeoba"
    lname = web.find_element_by_xpath('//*[@id="customer-last-name"]')
    lname.send_keys(lastname)

    sleep(randint(3,6))

    email_address = "lynda.ezeoba@outlook.com"
    email = web.find_element_by_xpath('//*[@id="customer-email"]')
    email.send_keys(email_address)

    sleep(randint(3,9))

    phone_no = "08163449757"
    p_num = web.find_element_by_xpath('//*[@id="customer-phone"]')
    p_num.send_keys(phone_no)
    sleep(randint(4,8))


    pay_now = web.find_element_by_xpath('//*[@id="pay-btn"]')
    pay_now.click()

    sleep(randint(4,8))
    # Switch to iframe where form is
    frame_ref = web.find_elements_by_tag_name("iframe")[1]
    iframe = web.switch_to.frame(frame_ref)

    sleep(2)
    transfer_btn = web.find_element_by_xpath("/html/body/div/div/section/div/div/div[1]/nav/ul/li[3]/a")
    transfer_btn.click()

    sleep(12)
    acct = web.find_element_by_xpath('/html/body/div/div/section/div/div/div[2]/div/section/div/div/div/div[2]/div/p[2]').text

    web.switch_to.default_content()
    web.close()
    return acct
get_acct(url)


# In[ ]:




