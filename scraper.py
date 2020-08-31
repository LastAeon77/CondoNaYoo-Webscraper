import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd
from utils.SQL import insertIntoSQL
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Text

engine = create_engine(
    "mysql+mysqlconnector://root:Kaguyabestmanga#1@localhost:3306/condonayoo", echo=True
)
meta = MetaData()
conn = engine.connect()
Vinvestor = Table(
    "condonayoo",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name_th", Text),
    Column("realName_th", Text),
    Column("Owner", Text),
    Column("Area", Text),
    Column("Number_of_Buildings", Text),
    Column("Floors", Text),
    Column("Room", Text),
    Column("Room_size_and_feature", Text),
    Column("Total_Parking", Text),
    Column("Total_Lifts", Text),
    Column("Zone", Text),
    Column("Public_Transports", Text),
    Column("Passing_Transport_Vehicles", Text),
    Column("Address", Text),
    Column("Schedule", Text),
    Column("Year_Construction_Completed", Text),
    Column("Price", Text),
    Column("Price_per_Square_Meter", Text),
    Column("Common_fee_and_funds", Text),
    Column("Nearby_Important_Locations", Text),
    Column("Conveniences", Text),
    Column("Highlights", Text),
)
meta.create_all(engine)
datas = pd.read_csv("./data/MasterDataVinvestor.csv")

things = []
browser = webdriver.Chrome()
browser.get("http://www.google.com")  # open google
search = browser.find_element_by_name("q")
for i in range(20):
    time.sleep(1)
    search.send_keys(datas.iloc[i]["name_th"] + " Condonayoo")
    search.send_keys(Keys.RETURN)
    results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
    results[0].click()
    try:
        if browser.current_url[:26] == "https://www.condonayoo.com":
            # site = requests.get('https://www.condonayoo.com/state-tower-condominium/').text
            soup = BeautifulSoup(browser.page_source, "lxml")
            table = soup.findAll("ul")
            newString = table[1].get_text()
            df = pd.read_html(browser.current_url)
            df = df[0]
            df.iloc[18][1] = newString
            things.append(df)
            ins = insertIntoSQL(Vinvestor, datas.iloc[i]["name_th"], df)
            conn.execute(ins)
    except ValueError as e:
        print(e)
    except IndexError as f:
        print("THere's not enough indexes for system")
    browser.get("http://www.google.com")
    search = browser.find_element_by_name("q")
browser.quit()