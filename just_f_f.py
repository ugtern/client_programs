from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\chromedriver.exe')

for i in range(49,100):
    a='https://hls-hw.xvideos-cdn.com/videos/hls/85/44/0b/85440b586cb37f9f2f491d87e5153b26/hls-480p'+str(i)+'.ts?e=1544032580&l=0&h=d2094cf262aaf37ac312c2e46d6a5de3'
    driver.get(a)
