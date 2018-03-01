﻿# *-* coding: utf-8 *-*
from selenium import webdriver
import time
import json
from pprint import pprint
import os


mylist = []

def get(id,proxies):
    post = {}
    chome_options = webdriver.ChromeOptions()  
    chome_options.add_argument(('--proxy-server=' + proxies['http']))  
    
    #os.environ["webdriver.chrome.driver"] = executable_path
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=chome_options)
    driver.get('http://www.gzdata.gov.cn/login.html')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(id)
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('Gz55555aaaaa')
    # 点击记住密码

    time.sleep(8)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/form/div[4]/div[2]/button').click()
    # 扫二维码！

    cookie_items = driver.get_cookies()
    for cookie_item in cookie_items:
        post[cookie_item['name']] = cookie_item['value']
    mylist.append({
        'cookie':post,
        'proxies':proxies
    })
    driver.get("http://httpbin.org/ip")
    #driver.get("http://ip.chinaz.com/getip.aspx")
    
    print(driver.page_source)
    time.sleep(3)
    driver.close()


idlist=[
    'haoahaoa',
    'haoahaoa02',
    'haoahaoa03',
    'haoahaoa04',
]
with open('ip.txt','r') as f:
    iplist = f.readlines()

ip = iter(ipList)

for id in idlist:
    flag = True
    while flag:
        try:
            time.sleep(1)
            try:
                p = ip.__next__()
            except:
                flas = False
            get(id,{'http':p})
            flag = False
        except:
            print('ip__unuse')

cookie_str  = json.dumps(mylist)

with open('cookie.txt', 'w+', encoding='utf-8') as f:
    f.write(cookie_str)

print('end')