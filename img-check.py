from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
import time 
import pandas as pd
# import os
# from dotenv import load_dotenv
import json
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# import session_util
options = Options()
# options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")


PATH = "C:\\coUsers\\Admin\\Downloads\\chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def startpy():
    # links = get_links()
    # print(links[0:10])

    # for link in links[0:2]:
    link="https://www.amazon.com/dp/B000052YHR"
    # scrape(str(link.strip()))
    driver.get(link)
    img_tag = driver.find_element("xpath",'//*[@id="landingImage"]').get_attribute('src')
    print(img_tag)





if __name__ == "__main__":
    startpy()








