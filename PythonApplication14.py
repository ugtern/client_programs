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

def zapis_v_file(kurs, our_file):
    f = open(our_file, 'a')
    now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    f.write(now+': '+str(kurs)+'\n')
    f.close()


driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get("https://olymptrade.com/")
koridor = np.array([])
stavka = 0
proebs = 1
klicks = 0
our_koeff = [0, 0.00025, 0.00030, 0.00040, 0.00045, 0.00050, 0.00055, 0.00060, 0.00065, 0.00070, 0.00075, 0.00080, 0.00090, 0.00090, 0.00095, 0.00100, 0.00105]

is_stavka = False

time.sleep(5)
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[1]/header/div/div[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/form/div[1]/input').send_keys('kulluck@mail.ru')
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/form/div[2]/input').send_keys('hersobachiy')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="page-container"]/section[1]/div/div[2]/div[1]/div[1]/div/div[2]/div/form/div[4]/button').click()

time.sleep(10)

while True:
    kurs = driver.find_element_by_xpath('//*[@id="opcion"]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/button/div').text
    
    koridor = np.append(koridor, kurs)
    koridor = np.array(koridor, dtype=float)

    if len(koridor)>120:
        koridor = np.delete(koridor, 0)

        if stavka == 0:

#           print(str(kurs)+' '+str(np.mean(koridor)))

            sr_zn_kor = float(kurs) - float(np.mean(koridor))

#           print(sr_zn_kor)

            for i in range(1, len(our_koeff)):

                if is_stavka == False:

                    length_proizv = i

                    proizv = float(kurs) - float(koridor[(len(koridor)-1)-length_proizv])
    
#                   proizv[i]>our_koeff[i] and sr_zn_kor>our_koeff[i] #на понижение
#                   proizv[i]<-our_koeff[i] and sr_zn_kor<-our_koeff[i] #на повышение

                    if proizv>our_koeff[i] and sr_zn_kor>our_koeff[i]:
                            driver.find_element_by_xpath('//*[@id="opcion"]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/button').click()
                            print(proizv)
                            stavka = 40
                            is_stavka = True
            
                    elif proizv<(-our_koeff[i]) and sr_zn_kor<(-our_koeff[i]):
                            driver.find_element_by_xpath('//*[@id="opcion"]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/button').click()
                            print(proizv)
                            stavka = 40
                            is_stavka = True

            
    if stavka>0:
        stavka-=1
    elif stavka == 0 and is_stavka == True:
        
        is_stavka = False

        
    zapis_v_file(kurs, 'OlimpGrafik.txt')
    print(str(kurs))
    time.sleep(1)