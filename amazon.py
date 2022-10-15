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

PATH = "/home/user/Downloads/chromedriver"

driver = webdriver.Chrome(executable_path=PATH)

links=[]

def get_links():
    df = pd.read_csv('links.csv')
    links = df.iloc[:,0].tolist()

    return links 









def startpy():
    links = get_links()

    for link in links:
        pass





if __name__ == "__main__":
    startpy()