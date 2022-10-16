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

# from symbol import pass_stmt

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


links=[]
info ={}
count =0
unavail= 0
total_links_list =[]


def get_links():
    df = pd.read_csv('links.csv')
    links = df.iloc[:,0].tolist()

    return links 

def get_scraped_links():
    
    f = open('amazon.json',)
    data = json.load(f)
    
    for i in data['products']:
        total_links_list.append(i['link'])

     

def scrape(link):
    print(link)
    driver.get(link)
    driver.maximize_window()
    # time.sleep(3)
    title = driver.find_element('xpath','//*[@id="productTitle"]').text
    print(title)
   
    img_url = driver.find_element("xpath",'//*[@id="landingImage"]').get_attribute('src')
    print(img_url)
    try:
        ratings = driver.find_element('xpath','//*[@id="acrCustomerReviewLink"]')
        ratings_no = ratings.text
        ratings_link = ratings.get_attribute('href')
    except:
        global unavail
        unavail +=1 
        print(f"unavailable: {unavail}")
        return
        


    try:
        desc = driver.find_element('xpath','//*[@id="productDescription"]/p/span').text
    except:
        try:
            desc= driver.find_element('xpath','//*[@id="visual-rich-product-description"]/div/div[1]/div/div/div/div[2]/span').text
        except:
            desc = title
    
    driver.get(ratings_link)
    

   
    review_titles = []
    # english = driver.find_element('xpath','//*[@id="cr-translate--450546797"]/a[2]').click()
    try:
        see_all_reviews = driver.find_element('xpath','//*[@id="reviews-medley-footer"]/div[2]/a').click()
    except:
        try:
            see_all_reviews = driver.find_element('xpath','//*[@id="cr-pagination-footer-0"]/a').click()
        except:
            global unavail
            unavail +=1 
            print(f"unavailable: {unavail}")


    for j in range(2):
        
        rlink     = driver.find_elements('xpath','//*[@data-hook="review-body"]')
            # reviews_link.append(rlink)
        for i in rlink:
            review_titles.append(i.text)
        
        try:
             next_page = driver.find_element('xpath','//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').click()
        except:
            try:
                next= driver.find_element('xpath','//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a').get_attribute('href')
                driver.get(next)
            except:
                pass

        time.sleep(2)

    info['link'] = link
    info['title']= title
    info['img'] = img_url
    info['ratings'] = ratings_no
    info['description'] = desc
    info['reviews'] = review_titles
    

    global count 
    count = count+1
    print(count)

    with open('amazon.json') as f:
        data = json.load(f)

    with open('amazon.json',"w") as of:    
        try:
                
            data ["products"].append(info)
        except:
            data = {
                    "products" : [info]
                }
        json.dump(data,of)



def startpy():
    links = get_links()
    # print(links[0:10])
    get_scraped_links()
    for link in links[101:150]:
        if link in total_links_list:
            print("already scraped: "+link)
            continue
        scrape(str(link.strip()))





if __name__ == "__main__":
    startpy()