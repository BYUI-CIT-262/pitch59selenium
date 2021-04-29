from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

""" CREATE A USER """

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://public.p59.dev/welcome")

link = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[2]')
link.click()

firstName = driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys("test")

lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys('test')

email = driver.find_element_by_xpath('//*[@id="emailId"]')
email.send_keys('1111@gmail.com')

number = driver.find_element_by_xpath('//*[@id="contactNumber"]/input')
number.send_keys('9999997485')

zipCode = driver.find_element_by_xpath('//*[@id="zipCode"]')
zipCode.send_keys('83440')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

cPassword = driver.find_element_by_xpath('//*[@id="repassword"]')
cPassword.send_keys('Love1111')

signUp = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-up/div/div/div/div[2]/div/form/div[9]/button')
signUp.click()

time.sleep(5)

firstV = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[1]')
firstV.send_keys('1')

secondV = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[2]')
secondV.send_keys('1')

thirdV = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[3]')
thirdV.send_keys('1')

fourth = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[4]')
fourth.send_keys('1')

button = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[2]/button')
button.click()

time.sleep(5)
driver.quit()

""" BREAK IN """


""" DELETE A USER (find code on postman) """

