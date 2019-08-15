from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('div', class_="content_title").text
    print(title)
    p = soup.find('div', class_="article_teaser_body").text
    print(p)

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find('li', class_="slide").find('div', class_="img").find('img', class_="thumb")
    image = image['src']
    featured_image_url = f'https://www.jpl.nasa.gov{image}'
    featured_image_url

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweet = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    tweet

    import pandas as pd
    url = 'https://space-facts.com/mars/'
    table = pd.read_html(url)
    df = table[0]
    html_table = df.to_html()
    html_table.replace('\n', '')

    cerberus = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'

    browser.visit(cerberus)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    cerberus_img = soup.find('img')['src']
    cerberus_img

    schiaparelli = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'

    browser.visit(schiaparelli)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    schiaparelli_img = soup.find('img')['src']
    schiaparelli_img

    syrtis_major = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'

    browser.visit(syrtis_major)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    syrtis_major_img = soup.find('img')['src']
    syrtis_major_img

    valles_marineris = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    browser.visit(valles_marineris)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    valles_marineris_img = soup.find('img')['src']
    valles_marineris_img

    mars_dict= {
        "title": title, 
        "p": p,
        "featured_image_url": featured_image_url,
        "tweet": tweet,
        "html_table": html_table,
        "cerberus_img": cerberus_img,
        "schiaparelli_img": schiaparelli_img,
        "syrtis_major_img": syrtis_major_img,
        "valles_marineris_img": valles_marineris_img,
        "html_table": html_table

    }

    browser.quit()
    return mars_dict

    # import pymongo

    # conn = 'mongodb://localhost:27017'
    # client = pymongo.MongoClient(conn)

    # db = client.mars_stuff
    # collection = db.mars_info
    # collection.drop()

    # db.collection.insert(mars_dict)