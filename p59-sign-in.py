from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome()
# driver.maximize_window()
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


# contact = driver.find_element_by_xpath('//*[@id="search-swiper-pr_id_9"]/swiper/div/div[1]/div[3]/app-search-result-thumbnail/div/div[5]/div[2]')
# time.sleep(3)

# contact.click()
# time.sleep(3)

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

# time.sleep(5)
print("done!!!!")
driver.quit()
# log in
# //*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]

# Email
# //*[@id="email"]

# password
# //*[@id="password"]

# logIn button
# /html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button