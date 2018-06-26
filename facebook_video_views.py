#Importing all the required packages.
import time
from bs4 import BeautifulSoup
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *
import time
from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from contextlib import closing
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests
import re
from bs4 import BeautifulSoup
import retrying
import pandas as pd
import xlsxwriter
from datetime import datetime


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#We are using chrome chrome options as we have to disable the the notification from the browser as it appears when you open a new link, which results in breaking of the code.
chrome_options = Options()
#Disabling the chrome notification.
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path='/Users/prateekgaurav/Downloads/chromedriver', chrome_options=chrome_options)

wait = WebDriverWait( driver, 10 )

#Defining the required variables.
names =[]
video_links = []
dates = []
views =[]

# Mention all the lists of the url's to be scraped.
urls = ['https://www.facebook.com/pg/RenaultIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/HyundaiIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/datsunindia/videos/?ref=page_internal',
'https://www.facebook.com/pg/TataMotorsGroup/videos/?ref=page_internal',
'https://www.facebook.com/pg/ToyotaIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/HondaCarIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/nissanindia/videos/?ref=page_internal',
'https://www.facebook.com/pg/Volkswagenindia/videos/?ref=page_internal',
'https://www.facebook.com/pg/FordIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/SkodaIndia/videos/?ref=page_internal',
'https://www.facebook.com/pg/MSArenaOfficial/videos/?ref=page_internal']



driver.get('https://www.facebook.com')

try:
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    #Your emmail id and password for the facebook account goes here.
    username.send_keys("*******")
    password.send_keys("*******")
    #Clicks on the Submit button after typing in the login credentials.
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()
    time.sleep(5)
except:
    pass

#For loop to loop through the list urls.
for url in urls:
    count = 0
    print("url" + url)
    try :
        driver.get(url)
    except:
        print("error fetching the url")
        continue
    time.sleep(5)

    page = driver.page_source

    soup_expatistan = BeautifulSoup(page, "html.parser")

    SCROLL_PAUSE_TIME = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    tmp = []
    tmp1=[]
    tmp2=[]
    tmp3=[]
    while count <=100 :

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        print("new_height" + str(new_height))
        if new_height == last_height:
            break
        last_height = new_height

        # print(str(driver))
        # link_loop = browser.page_source

    page_html = BeautifulSoup(driver.page_source, "html.parser")
    #print("page_html = {0}".format(page_html))
    mv_containers = page_html.find_all("div", class_="_u3y")
    #print("containers - {0}".format(mv_containers))

    for container in mv_containers:
        try:
            name = container.find('div', class_ = '_3v4h _48gm _50f3 _50f7')
            name = name.text
            #print(name)
            tmp.append(name)

        except:
            tmp.append("No Data")
            #print("No Names")

        try:
            video_link = container.find('a', href=True)
            video_link = video_link['href']
            video_link = "https://www.facebook.com"+str(video_link)
            #print(video_link)
            tmp1.append(video_link)

            #inputTag = soup.findAll(attrs={"name" : "stainfo"})
            #output = inputTag['value']
        except:
            tmp1.append("No Data")
            #print("No video_links")

        try:
            view = container.find('span', class_ = 'fcg')
            view = view.text.split(' ')[0]
            if (view[-1:] == 'K'):
                view = view[:-1]
                view = float(view)*1000
            elif (view[-1:] == 'M'):
                view = view[:-1]
                view = float(view)*1000000
            else:
                view = float(view)

            tmp2.append(view)

        except:
            tmp2.append("No Data")

        try:
            date = container.find('div', class_ = 'fsm fwn fcg')
            date = date.text
            #date = datetime.strptime('Jun 1 2005', '%b %d %Y')
            #date_month = datetime.month
            #print("date_month = "+date_month)
            tmp3.append(date.split('·')[1])
            #tmp3.append(date)

        except:
            tmp3.append("No Data")


        count = count + 1
    names += tmp
    video_links += tmp1
    views += tmp2
    dates += tmp3



driver.quit()


data_store = pd.DataFrame({ 'Video Name': names,
                            'Views': views,
                            'Video_Links': video_links,
                            'Upload Date': dates
                              })

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('facebook_videos.xlsx', engine='xlsxwriter')

# # Convert the dataframe to an XlsxWriter Excel object.
data_store.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
