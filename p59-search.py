from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://public.p59.dev/welcome")

time.sleep(3)

searchBtn = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[1]')
searchBtn.click()
time.sleep(3)

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(3)

searchBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input')
searchBar.send_keys('software developer')
time.sleep(2)

pitchMe = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/button')
pitchMe.click()
time.sleep(3)


searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
searchBar.send_keys('Software developer')
time.sleep(2)
pitchMe.click()
time.sleep(3)

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
searchBar.send_keys('Software Developer')
time.sleep(2)
pitchMe.click()
time.sleep(3)
searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(2)


zipBarClear = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/div/p-autocomplete/span/input').clear()
zipBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/div/p-autocomplete/span/input')
zipBar.send_keys('salt lake city')
time.sleep(2)
pitchMe.click()
time.sleep(3)
