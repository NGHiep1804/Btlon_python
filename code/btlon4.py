import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time
url='https://www.footballtransfers.com/us/transfers/confirmed/2023-2024/uk-premier-league'
chuyen_nhuong=[]
def duyet(url):
    time.sleep(10)
    service = Service(ChromeDriverManager().install())
    driver1 = webdriver.Chrome(service=service)
    driver1.get(url)
    try:
        
        soup=bs(r.content,'html.parser')
        ta=soup.find('table',class_='table table-striped table-hover leaguetable mvp-table transfer-table mb-0 player-table-loading')
        tbody=ta.find('tbody')
        trs=tbody.find_all('tr')
        for tr in trs:
            tds=tr.find_all('td')
            cauthu=[]
            name_span=tds[0].find('div')
            name_div=name_span.find_all('div')
            name=name_div[1].text
            club_divs=tds[1].find('div',class_='transfer-club-container')
            club_div=club_divs.find_all('div')
            club_from=club_div[0].find('a')
            club_from_div=club_from.find('div')
            club_from_text=club_from_div.text
            club_to=club_div[2].find('a')
            club_to_div=club_to.find('div')
            club_to_text=club_to_div.text
            date=tds[2].text
            gia_span=tds[3].find('span')
            gia=gia_span.text
            cauthu.append(name)
            cauthu.append(club_from_text)
            cauthu.append(club_to_text)
            cauthu.append(date)
            cauthu.append(gia)  
            chuyen_nhuong.append(cauthu)
    except:
        print("done")
duyet(url)
print(1)
# url+='/'
# for i in range(2,19):
#     link=url+str(i)
#     duyet(link)
#     print(i)
header=['name','club_from','club_to','date','gia']
dataFrame=pd.DataFrame(chuyen_nhuong,columns=header)
dataFrame.to_csv('chuyen_nhuong.csv')