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

#################### Clean & Structure ####################
chess_data = pd.DataFrame(
    {'Date': dates_container,
     'Result': results_container,
     'Moves': moves_container,
     'Link': links_container 
    })

#################### Grabbing Individual Game Stats ####################
def grab_extras(link = None):
    driver.get(link)

    # Pass over to BS4
    bsObj = BeautifulSoup(driver.page_source, 'lxml')

    # Get top player stats
    top_player = bsObj.findAll('div', attrs={'id': "topPlayer"})
    top_elo = top_player[0].find('span', {'class':'user-rating'}).getText()
    top_country = top_player[0].findAll('span', {'class', re.compile('country')})[0].get('tip')
    top_name = top_player[0].find('a', {'class':'username'}).getText().strip()     

    # Get bottom player stats
    bottom_player = bsObj.findAll('div', attrs={'id': "bottomPlayer"})
    bottom_elo = bottom_player[0].find('span', {'class':'user-rating'}).getText()
    bottom_name = bottom_player[0].find('a', {'class':'username'}).getText().strip()   
    bottom_country = bottom_player[0].findAll('span', {'class', re.compile('country')})[0].get('tip')

    # Get game stats
    game_info = bsObj.findAll('li', attrs={'class': "game-info-item"})
    game_result = game_info[0].getText()
    game_time = game_info[1].getText().strip()
    
    # Clean
    bottom_elo = bottom_elo.replace("(", "")
    bottom_elo = bottom_elo.replace(")", "")
    top_elo = top_elo.replace("(", "")
    top_elo = top_elo.replace(")", "")
    
    # Logic 
    if top_name == 'eono619':
        return [int(top_elo), top_name, top_country, int(bottom_elo), bottom_name, bottom_country, game_result, game_time]
    else:
        return [int(bottom_elo), bottom_name, bottom_country, int(top_elo), top_name, top_country, game_result, game_time]
    

# Make container and Loop
row_list = []
for row in chess_data['Link']:
    row_list.append(grab_extras(row))

# Close the driver    
driver.close()

# Convert to a dataframe   
col_list = ['my_elo', 'my_user', 'my_country', 'opponent_elo', 'opponent_user', 'opponent_country', 'game_result', 'game_time']
game_stats = pd.DataFrame(row_list, columns=col_list)

# Combine all data
chess_data_total = pd.concat([chess_data, game_stats], axis=1)
chess_data_total.head()

# Covert types and re-index 
chess_data_total["Moves"] = pd.to_numeric(chess_data_total["Moves"])
#chess_data_total["Date"] = pd.to_datetime([chess_data_total["Date"]])#, format="%m/%d/%Y")

chess_data_total.dtypes

# Reverse and reset index
chess_data_total = chess_data_total.iloc[::-1]
chess_data_total.reset_index(drop=True, inplace=True)

# Save down a copy 
chess_data_total.to_csv()

