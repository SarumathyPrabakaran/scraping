from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
import time 
import pandas as pd
# import os
# from dotenv import load_dotenv
import json
from selenium.webdriver.chrome.options import Options
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


PATH = "C:\\Users\\Admin\\Downloads\\chromedriver"

driver = webdriver.Chrome(executable_path=PATH, options= options)

links=[]
info ={}
count =0
def get_links():
    df = pd.read_csv('C:\\Users\\Admin\\Documents\\tact\\scraping\\links.csv')
    links = df.iloc[:,0].tolist()

    return links 

def scrape(link):
    print(link)
    driver.get(link)
    driver.maximize_window()
    # time.sleep(3)
    title = driver.find_element('','//*[@id="productTitle"]').text
    print(title)
    ratings = driver.find_element('xpath','//*[@id="acrCustomerReviewText"]')
    ratings_no = ratings.text
    ratings_link = ratings.get_attribute('href')
    desc = driver.find_element('xpath','//*[@id="productDescription"]/p/span').text

    driver.get(ratings_link)
    

    # reviews_link = []
    review_titles = []
    english = driver.find_element('xpath','//*[@id="cr-translate--450546797"]/a[2]').click()
    see_all_reviews = driver.find_element('xpath','//*[@id="reviews-medley-footer"]/div[2]/a').click()

    for j in range(2):
        for i in range(1,11):
            rlink     = driver.find_element('xpath','//*[@data-hook="review-body"]')
            # reviews_link.append(rlink)
            review_titles.append(rlink.text)
        
        next_page = driver.find_element('xpath','//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
        time.sleep(2)

    info['link'] = link
    info['title']= title
    info['ratings'] = ratings_no
    info['description'] = desc
    info['reviews'] = review_titles

    global count 
    count = count+1
    print(count)

    with open("amazon.json","r") as f1:

        old_data = json.load(f1)
        # print(type(old_data))
        old_data.update(info)


    # print(old_data)
    with open("amazon.json","w") as f2:
        json.dump(old_data,f2)
        print("done!\\n")



def startpy():
    links = get_links()
    # print(links[0:10])

    for link in links[0:2]:
        scrape(link)





if __name__ == "__main__":
    startpy()