# Imports
import pandas as pd 
import requests 
import re
from bs4 import BeautifulSoup, SoupStrainer
import selenium 
from selenium import webdriver
import time
import getpass
import matplotlib.pyplot as plt
import seaborn as sns


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
