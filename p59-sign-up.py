from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://public.p59.dev/welcome")
# print(driver.title)

link = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[2]')
link.click()

firstName = driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys("test")

lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys('test')

email = driver.find_element_by_xpath('//*[@id="emailId"]')
email.send_keys('111@gmail.com')

number = driver.find_element_by_xpath('//*[@id="contactNumber"]/input')
number.send_keys('9999997484')

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

# emailR = driver.find_element_by_xpath('//*[@id="refemailId"]')
# emailR.send_keys('1111')

time.sleep(5)
driver.quit()

# ----------------------------------Form input-------------------------------------
# Fist Name
# //*[@id="firstName"]
# Last Name
# //*[@id="lastName"]
# Email Address
# //*[@id="emailId"]
# Mobile Number 999 999 7484
# //*[@id="contactNumber"]/input
# Zip Code
# //*[@id="zipCode"]
# Password
# //*[@id="password"]
# Confirm Password
# //*[@id="repassword"]
# Email Referer
# //*[@id="refemailId"]
# Sign up
# /html/body/app-root/main/app-new-sign-up/div/div/div/div[2]/div/form/div[9]/button

#--------------------------------------Verify Form----------------------------------
# First Input
# /html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[1]
# Second Input
# /html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[2]
# Third Input
# /html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[3]
# fourth Input
# /html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[4]
# Verify
# /html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[2]/button