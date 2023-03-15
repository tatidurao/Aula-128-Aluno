from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    try:
        #obetenha o conteudo da pag html do hiperlink atraves do resquest.get
        page = requests.get(hyperlink)
        #obter o codigo da pagina
        soup = BeautifulSoup(page.content, "html.parser")

        temp_list = []

        
                    
        

    except:
        #para iterar e ir para o próximo link
        time.sleep(1)
        scrape_more_data(hyperlink)

#le o arquivo
planet_df_1 = pd.read_csv("updated_scraped_data.csv")

#acessa os dados do arquivo linha por linha
for index, row in planet_df_1.iterrows():
    
    print(row['hyperlink'])
    #na linha acesse a coluna hyperlink para chamar a função criada acima
    
    print(f"Coleta de dados do hiperlink {index+1} concluída")

print(new_planets_data)

scrapped_data = []
#remover o caracter \n
for row in new_planets_data:
   replaced = []
   for el in row: 
       el = el.replace("\n", "")
       replaced.append(el)
   scrapped_data.append(replaced)

print(scrapped_data)


headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]
new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)
new_planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")
