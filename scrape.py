# Imports
import pandas as pd 
import requests 
import re
from bs4 import BeautifulSoup, SoupStrainer
import selenium 
from selenium import webdriver
import time
import getpass

#################### Define Functions ####################
def pull_results(link = None):
    # Grab link 
    driver.get(link)
    
    # Pass over to BS4
    bsObj = BeautifulSoup(driver.page_source, 'lxml')

    results = []
    # Grab all the games
    for result in bsObj.findAll('i', attrs={'class': re.compile("icon-square")}):
        results.append(result.get('tip'))

    return results

def pull_moves(link = None):  
    # Grab link
    driver.get(link)

    # Pass over to BS4
    bsObj = BeautifulSoup(driver.page_source, 'lxml')

    moves = []
    # Grab all the games
    for move in bsObj.findAll('a', attrs={'class': "clickable-link text-middle moves"}):
        moves.append(move.getText())
    
    # Empty container
    clean_moves = []
    
    # Clean 
    for move in moves:
        clean_moves.append(move.strip())
    
    return clean_moves

# Remove Duplicates
def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


def pull_links(link = None):
    # Grab link
    driver.get(link)
    
    # Empty container
    links = []
    
    # Pass over to BS4
    bsObj = BeautifulSoup(driver.page_source, 'lxml')

    # Grab all the games
    for link in bsObj.findAll('a', attrs={'href': re.compile("https://www.chess.com/live/game")}):
        links.append(link.get('href'))
    
    # Dedup
    links = remove(links)
    
    return links

def pull_dates(link = None):
    # Grab link
    driver.get(link)

    # Pass over to BS4
    bsObj = BeautifulSoup(driver.page_source, 'lxml')
    
    # Empty container
    dates = []
    
    # Grab all the games
    for date in bsObj.findAll('a', attrs={'class': "clickable-link archive-date"}):
        dates.append(date.getText())
    
    # Empty container
    clean_dates = []
    
    # Strip away the rest
    for date in dates:
        clean_dates.append(date.strip())
    
    return clean_dates

#################### Sign In to chess.com ####################
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

#################### Start the Scrape ####################
# Make the containers
results_container = []
moves_container = []
links_container = []
dates_container = []

for page_num in list(range(1,12)):
    # Make the Link
    link = """https://www.chess.com/games/archive?gameOwner=my_game&gameTypes%5B0%5D
    =lightning&gameTypes%5B1%5D=bullet&gameTypes%5B2%5D=blitz&gameTypes%5B3%5D
    =standard&gameTypes%5B4%5D=liveChess960&gameTypes%5B5%5D=
    bughouse&gameTypes%5B6%5D=threecheck&gameTypes%5B7%5D=crazyhouse&gameTypes%5B8%5D
    =kingofthehill&gameTypes%5B9%5D=rapid&gameType=live&page=""" + str(page_num)
    
    results_container = results_container + pull_results(link)
    moves_container = moves_container + pull_moves(link)
    links_container = links_container + pull_links(link)
    dates_container = dates_container + pull_dates(link)
    
time.sleep(3)
driver.close() 
