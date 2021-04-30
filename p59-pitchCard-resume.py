from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://public.p59.dev/welcome")
# video_recorder = VideoRecorder(driver)
# video_recorder.start()

link = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('1111@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('Log in')

createPitchCard = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[2]')
createPitchCard.click()
time.sleep(2)

resume = driver.find_element_by_xpath('//*[@id="resume"]/div[2]/app-search-result-thumbnail')
resume.click()
time.sleep(2)

nextBtn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-cards-packges/div/div/div/div[3]/div/button')
nextBtn.click()
time.sleep(2)
print('create reseme')

free = driver.find_element_by_xpath('/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-billing-cycle/div/div[1]/div[2]/div[1]/div/div[2]')
free.click()
time.sleep(2)

freeTwo = driver.find_element_by_xpath('/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-visual-video/div/div[1]/div[2]/div[1]/div/div[2]')
freeTwo.click()
time.sleep(2)
print('to the referal page')

referBtn = driver.find_element_by_xpath('/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-billing-summary/div/div/div[2]/div[2]/ul/li[1]/span[2]/img')
referBtn.click()
time.sleep(2)

# referMail = driver.find_element_by_xpath('/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-billing-summary/div/div/div[2]/div[2]/ul/li[1]/span[2]/input')
# referMail.send_keys('IneedEmail@gmail.com')



# time.sleep(5)
# video_recorder.stop()
print('test end')
driver.quit()