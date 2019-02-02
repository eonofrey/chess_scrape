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

#################### Analyze and Plot ####################
sns.set_style("white")
sns.set_context('talk')

plt.plot(chess_data_total['my_elo'][40:])

plt.xlabel('Number of Games', fontsize=18)
plt.ylabel('ELO', fontsize=16)

plt.show()
