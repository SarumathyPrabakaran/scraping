from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
import os
from dotenv import load_dotenv
import json
from selenium.webdriver.chrome.options import Options
import const
import culog
import requests
import os.path
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

load_dotenv()

PATH=os.environ.get("DRIVER_PATH")
EMAIL=os.environ.get("EMAIL")
PASSWORD=os.environ.get("PASSWORD")
BATCH=os.environ.get("BATCH")

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome( executable_path=PATH)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    os.mkdir("images")
except:
    pass



def links_csv():
    total_links = []
    # df=pd.read_csv('C:\\Users\\Admin\\Documents\\tact\\housilon-data-collector\\batch-1.csv')
    df=pd.read_csv('batch-1.csv')
    links = df.iloc[:,0].tolist()
    for link in links:
        if link not in total_links:
            total_links.append(link)
    return total_links



def image():
    time.sleep(3)
    links  = links_csv()
    for link in links:
        image_links = []
        print(link)
        # driver.get("https://housesigma.com/web/en/house/56k97wqE6WnYKRjD/417-DOON-SOUTH-Drive-Kitchener-N2P2T6-40211515")
        driver.get(link)
        time.sleep(5)
        while True:
            try:
                next = driver.find_element('xpath','//*[@class="swiper-button-next"]')
                time.sleep(2)
                next.click()
            except:
                break
            
        # div_tag = driver.find_element('By.CLASS_NAME',"swiper-wrapper")
        # img_tag = div_tag.find_elements('By.tag_name',"img")
        for i in range(1,14):
            img_tag = driver.find_element('xpath',f'//*[@id="{i}"]/div/img')
        for img in img_tag:
            url = img.get_attribute('src')
            # print(url)
            image_links.append(url)

        for image_link in image_links:
            print(image_link)
            name = image_link.split('/')[-1].split('?')[0]
            # print(name)
            with open(f"images/{name}",'wb') as f:  
                image = requests.get(image_link)
                f.write(image.content)    
                print("writing: ",name)
        
    # driver.quit()


def login():
    signin = driver.find_element('xpath','//a[@class="global-link user_login"]')
    signin.click()

    time.sleep(2)

    email = driver.find_element('xpath','//*[@id="pane-email"]/form/div[1]/div/div/input')
    email.send_keys(EMAIL)

    pwd = driver.find_element('xpath','//*[@id="pane-email"]/form/div[2]/div/div/input')
    pwd.send_keys(PASSWORD)

    button = driver.find_element('xpath','//*[@class="el-button signin el-button--primary"]')
    button.click()

def startpy():
    driver.get('https://housesigma.com/web/en/')
    driver.maximize_window()

    time.sleep(2)

    login()

    image()



if __name__ == '__main__':
    startpy()