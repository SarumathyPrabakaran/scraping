from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def scrape(link):
    driver.get(link)
    driver.maximize_window()
    time.sleep(13)
    # for i in range(1,82):
    #     name = driver.find_element("xpath",f'//*[@id="open"]/course-cards/div/div[{i}]/course-card/a/div/div[2]/h4/span/strong').text
        
    #     print(name)

    tags = driver.find_elements(By.TAG_NAME,'strong')
    for tag in tags:
        print(tag.text)

# PATH = "/home/saru/softwares/chromedriver"
# driver = webdriver.Chrome(PATH)



scrape("https://swayam.gov.in/explorer?category=COMP_SCI_ENGG")