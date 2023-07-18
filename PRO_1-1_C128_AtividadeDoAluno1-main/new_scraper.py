from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
#browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
#browser.get(START_URL)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(START_URL)
time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):


    

#le o arquivo
planet_df_1 = pd.read_csv("updated_scraped_data.csv")

#acessa os dados do arquivo linha por linha


scrapped_data = []
#remover o caracter \n



headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]
new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)
new_planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")
