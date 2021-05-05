from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt
from selenium.webdriver import ActionChains

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"h")
   except getopt.GetoptError:
      print ('err')
      sys.exit(2)
      
   driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)
   for opt, arg in opts:
      if opt in ['-h']:
         return driver

   driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
   return driver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = main(sys.argv[1:])
driver.get("https://public.p59.dev/welcome")


link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()
print('start test')
print('click login')

time.sleep(5)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('1111@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('log in')

profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

favorite = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/ul/li[2]/a/span')
favorite.click()
time.sleep(2)
print('On favorite page and try to create a new pocket')

addPocket = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/div[1]/div[2]/div[2]/div')
addPocket.click()
time.sleep(1)

pocketName = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/p-dialog[1]/div/div/div[2]/div/input')
pocketName.send_keys('test')

color = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/p-dialog[1]/div/div/div[2]/div/div/div[5]/div')
color.click()

create = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/p-dialog[1]/div/div/div[2]/div/button')
create.click()
print('Create a test pocket')
time.sleep(5)

# backToMainPage = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[1]/img')
# backToMainPage.click()
# time.sleep(2)
# print("go back to main page")

# saveToFavorite = driver.find_element_by_xpath('//*[@id="search-swiper-pr_id_18"]/swiper/div/div[1]/div[1]/app-search-result-thumbnail/div/div[6]/div[1]/span')
# saveToFavorite.click()
# time.sleep(1)

# saveToTestPocket = driver.find_element_by_xpath('//*[@id="pr_id_43"]/app-pitchcard-modals-wrapper/p-dialog[4]/div/div/div[2]/div/app-pitchcard-folder-thumbnail[3]/div/div[1]/div[2]/span[2]')
# saveToTestPocket.click()
# time.sleep(1)
# print("Add a pitch Card to test pocket")


# profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
# profi.click()
# time.sleep(2)

# favorite = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/ul/li[2]/a/span')
# favorite.click()
# time.sleep(2)
# print("Back to favorite page")

# lookInToTest = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/div[1]/div[3]/div[2]/div[3]')
# lookInToTest.click()
# time.sleep(2)

# backToFavorite = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/div[1]/div[1]/span/i')
# backToFavorite.click()
# time.sleep(4)
# print('Back to favorite page')

testPocket = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/div[1]/div[3]/div[2]/div[3]/app-pocket-thumbnail/div/div[2]')
testPocket.click()
time.sleep(2)

deletePocket = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/div[1]/div[2]/div[2]/div[3]')
deletePocket.click()
time.sleep(2)

delete = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-my-pockets/p-dialog[2]/div/div/div[2]/div/div[1]')
delete.click()
time.sleep(2)
print('delete test pocket')


print("test end")
driver.quit()