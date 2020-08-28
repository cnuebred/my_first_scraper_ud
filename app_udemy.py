import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrap.scrap_category import *
from scrap.scrap_courses import *
from time import sleep

web_url = 'https://www.udemy.com'
driver_patch = r'C:\development\library\data_science\drivers\chromedriver.exe'

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=driver_patch,
                          chrome_options=chrome_options)
driver.get(web_url)

goto_category(driver)

courses_loop = True
while courses_loop:
    courses_loop = get_courses_data(driver)
