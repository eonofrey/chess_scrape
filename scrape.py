#yadda yadda yadda 
import pandas as pd 
import requests 
import re
from bs4 import BeautifulSoup, SoupStrainer
import selenium 
from selenium import webdriver
import time
import getpass

# Input Password
password = getpass.getpass()

# Make it so chrome will allow automated software
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")

# Find driver, add argument for the options we just created 
driver = webdriver.Chrome('/Users/Eric/Downloads/chromedriver_4',chrome_options=chrome_options)

# Grab site
driver.get('https://www.chess.com/games/archive')

# Sign in 
driver.find_element_by_xpath('//*[@id="username"]').send_keys("eonofrey@gmail.com")
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="login"]').click()

time.sleep(1)

links = []
for page_num in list(range(1,12)):
    link = """https://www.chess.com/games/archive?gameOwner=my_game&gameTypes%5B0%5D
    =lightning&gameTypes%5B1%5D=bullet&gameTypes%5B2%5D=blitz&gameTypes%5B3%5D
    =standard&gameTypes%5B4%5D=liveChess960&gameTypes%5B5%5D=
    bughouse&gameTypes%5B6%5D=threecheck&gameTypes%5B7%5D=crazyhouse&gameTypes%5B8%5D
    =kingofthehill&gameTypes%5B9%5D=rapid&gameType=live&page=""" + str(page_num)


    driver.get(link)

    # Pass over to BS4
    bsObj = BeautifulSoup(driver.page_source, 'lxml')


    # Grab all the games
    for link in bsObj.findAll('a', attrs={'href': re.compile("https://www.chess.com/live/game")}):
        links.append(link.get('href'))

    #print(BeautifulSoup(driver.page_source, 'lxml').prettify)


time.sleep(5)
driver.close()

# Remove Duplicates
def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

links = remove(links)

# Print Links
for i in links:
    print(i)
