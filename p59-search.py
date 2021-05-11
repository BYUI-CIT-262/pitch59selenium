from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"h")
   except getopt.GetoptError:
      print ('err')
      sys.exit(2)
      
   headless = False
   for opt, arg in opts:
      if opt in ['-h']:
         headless = True

   if headless:
      driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options) 
   else:
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


print('test start')
searchBtn = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[1]')
searchBtn.click()
print('Click search btn')
time.sleep(3)

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(3)
print('Clean search bar')



searchBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input')
searchBar.send_keys('software developer')
time.sleep(2)
print('type software developer')


pitchMe = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/button')
pitchMe.click()
time.sleep(3)


searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
searchBar.send_keys('Software developer')
time.sleep(2)
print('type Software developer')
pitchMe.click()
time.sleep(3)



searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
searchBar.send_keys('Software Developer')
time.sleep(2)
print('type Software Developer')
pitchMe.click()
time.sleep(3)
searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(2)


zipBarClear = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/div/p-autocomplete/span/input').clear()
zipBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/div/p-autocomplete/span/input')
zipBar.send_keys('salt lake city')
time.sleep(2)
print('Clean City/Zip bar and put salt lake city in the bar')

pitchMe.click()
time.sleep(3)

zipBarClear = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/div/div/div/div/div/div[2]/div/p-autocomplete/span/input').clear()
zipBar.send_keys('Salt Lake City, UT')
time.sleep(2)
print('Clean City/Zip bar and put Salt Lake City, UT in the bar')

pitchMe.click()
time.sleep(3)
print('End test')

driver.quit()