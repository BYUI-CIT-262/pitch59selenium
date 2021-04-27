from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://public.p59.dev/welcome")


pwd1 = 'Love1111'
pwd0- = 'Love111'


link = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('1111@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pwd)


logIn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)

profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

setting = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/div[1]/div/a/div')
setting.click()
time.sleep(2)

chagePwd = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-settings/div/div/div[1]/div[2]')
chagePwd.click()
time.sleep(2)


currentPwd = driver.find_element_by_xpath('//*[@id="oldpassword"]')
currentPwd.send_keys(pwd)

newPwd = driver.find_element_by_xpath('//*[@id="password"]')
newPwd.send_keys(pwd1)

confirmPwd = driver.find_element_by_xpath('//*[@id="confirmpassword"]')
confirmPwd.send_keys(pwd1)

change = driver.find_element_by_xpath('/html/body/app-root/main/app-change-password/div/div/div/div/div[2]/div/form/button')
change.click()
time.sleep(2)

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('1111@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pwd1)

logIn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)

time.sleep(5)
driver.quit()