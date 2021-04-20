from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://public.p59.dev/welcome")

link = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('1111@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)


contact = driver.find_element_by_xpath('//*[@id="search-swiper-pr_id_9"]/swiper/div/div[1]/div[3]/app-search-result-thumbnail/div/div[5]/div[2]')
contact.click()
time.sleep(3)

rightBotton = driver.find_element_by_xpath('//*[@id="search-swiper-pr_id_9"]/swiper/div/div[4]')
rightBotton.click()
time.sleep(2)
rightBotton.click()
time.sleep(2)

profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

logOut = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/div[2]/div')
logOut.click()

time.sleep(2)
driver.back()

time.sleep(5)
driver.quit()
# log in
# //*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]

# Email
# //*[@id="email"]

# password
# //*[@id="password"]

# logIn button
# /html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button