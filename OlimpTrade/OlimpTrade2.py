from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException as NSEE
from datetime import datetime
import time
import numpy as np

def isElementPresent(locator):
    try:
        driver.find_element_by_xpath(locator)
    except NSEE:
        return False
    return True

def zapis_v_file(kurs, mnenie, our_file):
    f = open(our_file, 'a')
    now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    f.write(now+': '+str(kurs)+': '+str(mnenie)+'\n')
    f.close()


driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get("https://olymptrade.com/")
koridor = np.array([])
raschet = np.array([])
stavka = 0
proebs = 1
klicks = 0
stavka_time = 0
is_stavka = False
stavka_vniz = False
stavka_vverh = False

time.sleep(5)
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[1]/header/div/div[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/form/div[1]/input').send_keys('kulluck@mail.ru')
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/form/div[2]/input').send_keys('hersobachiy')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/form/div[4]/button').click()

time.sleep(10)

while True:
    kurs = driver.find_element_by_xpath('//*[@id="deal_controls"]/div/div[2]/div[2]/div/div/div[2]/button/span[2]').text
    mnenie = driver.find_element_by_xpath('//*[@id="chart"]/div/div[1]/div[3]').text
    mnenie = int(mnenie.replace('%', ''))
    schet = driver.find_element_by_xpath('//*[@id="header"]/div/div[3]/div[1]/button/span').text
    schet = float(schet.split(' ')[0]+schet.split(' ')[1])
    #schet = float(schet)
    
    koridor = np.append(koridor, kurs)
    koridor = np.array(koridor, dtype=float)
    if len(koridor)>600:
        verh = (i - self.viborka[j-trend_len])*1000000
        niz = j - (j-trend_len)
        delen = ((verh/niz)*3600)/60
        raschet = np.append(raschet, delen)

        koridor = np.delete(koridor, 0)
    
    if delen>60 and stavka_time==0 and stavka_vverh==False and stavka_vniz==False:
            driver.find_element_by_xpath('//*[@id="deal_controls"]/div/div[2]/div[2]/div/div/div[1]/button').click()
            schet_stav = driver.find_element_by_xpath('//*[@id="header"]/div/div[3]/div[1]/button/span').text
            schet_stav = float(schet_stav.split(' ')[0]+schet_stav.split(' ')[1])
            stavka_time = 60
            is_stavka = True
            stavka_vverh = True
            
    elif delen<(-60) and stavka_time==0 and stavka_vverh==False and stavka_vniz==False:
            driver.find_element_by_xpath('//*[@id="deal_controls"]/div/div[2]/div[2]/div/div/div[3]/button').click()
            schet_stav = driver.find_element_by_xpath('//*[@id="header"]/div/div[3]/div[1]/button/span').text
            schet_stav = float(schet_stav.split(' ')[0]+schet_stav.split(' ')[1])
            stavka_time = 60
            is_stavka = True
            stavka_vniz = True
            
    if stavka>0:
        stavka-=1
    elif stavka == 0 and is_stavka == True:
        if schet_stav>schet:
            proebs*=2
            klicks = 1*proebs
        else:
            proebs = 1
            klicks = 0
        is_stavka = False

        
    zapis_v_file(kurs, mnenie, 'OlimpGrafik.txt')
    print(str(kurs)+' '+str(sr_zn_kor)+' '+str(sr_zn_kor_min)+' '+str(sr_zn_kor_max))
    print(schet,delen)
    time.sleep(1)
    
