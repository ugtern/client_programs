from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as NSEE
from datetime import datetime
import time

def isElementPresent(locator):
    try:
        driver.find_element_by_xpath(locator)
    except NSEE:
        print ('No such thing')
        return False
    return True

def auth():
    driver.find_element_by_xpath('//*[@id="page_home_index"]/header/div[2]/div/div/div[2]/div/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sign-in"]/div/div/div[1]/ui-scroll/div/div/div/div/app-auth-signin/form/div[1]/ui-n-input/div/input').send_keys("ugtern@mail.ru")
    driver.find_element_by_xpath('//*[@id="sign-in"]/div/div/div[1]/ui-scroll/div/div/div/div/app-auth-signin/form/div[2]/ui-n-input/div/input').send_keys("13raRdR133sEpb5yzb8NaGM6kcD6wD9Czk")
    driver.find_element_by_xpath('//*[@id="sign-in"]/div/div/div[1]/ui-scroll/div/div/div/div/app-auth-signin/form/div[4]/button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/div/ui-chart-container/div/div[1]/app-asset-tabs/nav/app-asset-tab/div/div[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[4]/div/app-asset-selector/label/input').send_keys("EUR/USD")
    time.sleep(1)
    if (isElementPresent('/html/body/div[4]/div/app-asset-selector/ui-scroll/div/div/div/ul[2]/li[2]/a') == True):
        driver.find_element_by_xpath('/html/body/div[4]/div/app-asset-selector/ui-scroll/div/div/div/ul[2]/li[2]/a').click()
    else:
        driver.find_element_by_xpath('/html/body/div[4]/div/app-asset-selector/ui-scroll/div/div/div/ul[1]/li[2]/a').click()
    time.sleep(5)
    pars_text()

def pars_text():
    global grad1, grad2, schet, up_but, down_but, schet_mod
    grad1 = driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[4]/div/span[1]').text
    grad2 = driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[4]/div/span[2]').text
    schet = driver.find_element_by_xpath('//*[@id="page_home_trading"]/header/app-account/div/div[1]/div/button/div[1]/app-currency/span/span/span[1]').text

    grad1 = grad1.split(' ')
    schet = schet.split(' ')
    schet = schet[0]+schet[1]
    schet = schet.split(',')

    grad1 = int(grad1[0])
    schet = int(schet[0])
    
def clickUp():
    up_but.click()
    time.sleep(90)
    sleditel()

def clickDown():
    down_but.click()
    time.sleep(90)
    sleditel()

def sleditel():
    global a
    schet_mod = driver.find_element_by_xpath('//*[@id="page_home_trading"]/header/app-account/div/div[1]/div/button/div[1]/app-currency/span/span/span[1]').text
    schet_mod = schet_mod.split(' ')
    schet_mod = schet_mod[0]+schet_mod[1]
    schet_mod = schet_mod.split(',')
    schet_mod = int(schet_mod[0])
    if schet > schet_mod:
        i = 0
        while i<a:
            driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[1]/div/ui-counter/div/div/button[1]').click()
            i+=1
        a*=3
        print('Не бей насяльниха все поправим!')
        f = open('fail_log.txt', 'a')
        output = str(grad1)+' '+str(grad1)+' '+str(schet)
        now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        f.write(now+': '+output+'\n')
        f.close()
    else:
        i = 0
        while i<a:
            driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[1]/div/ui-counter/div/div/button[2]').click()
            i+=1
        print('К успеху идем!')
        f = open('win_log.txt', 'a')
        output = str(grad1)+' '+str(grad1)+' '+str(schet)
        now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        f.write(now+': '+output+'\n')
        f.close()
        a = 1

driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get("https://binomo.com/ru/trading")

global a
a = 1
    
time.sleep(5)

auth()

up_but = driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[5]/div/div/div/button[1]')
down_but = driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[5]/div/div/div/button[2]')

schet_up = driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[1]/div/ui-counter/div/div/button[1]')
schet_down = driver.find_element_by_xpath('//*[@id="eur-graphs"]/div/aside/div/div[1]/div/div[1]/div/ui-counter/div/div/button[2]')

while True:
    pars_text()
    time.sleep(1)
    if grad1 >= 80:
        clickUp()
    elif grad1 <= 20:
        clickDown()
    else:
        f = open('every_sec_log.txt', 'a')
        output = str(grad1)+' '+str(grad1)+' '+str(schet)
        now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        f.write(now+': '+output+'\n')
        f.close()


