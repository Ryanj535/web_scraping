import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser

#Browser
def init_browser():
    executable_path = {'executable_path': 'C:/Program Files/chromedriver_win32/chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)
    html4 = browser.html
    soup4 = bs(html4, 'html.parser')

    titles = soup4.find_all("h3")
    for title in titles:
        browser.click_link_by_partial_text("Hemisphere")

    results4 = soup4.find_all("div", class_="description")
    mars_dict={}
    hemisphere_image_urls=[]
    for result in results4:
        link = result.find('a')
        img_href = link['href']
        title_img = link.find('h3').text
        url6 = "https://astrogeology.usgs.gov" + img_href
        browser.visit(url6)
        html5 = browser.html
        soup5 = bs(html5, 'html.parser')
        pic = soup5.find("a", target="_blank")
        pic_href = pic['href']
        hemisphere_image_urls.append({"title":title_img,"img_url":pic_href})
    print(hemisphere_image_urls)
scrape()
