# Import Dependecies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests
import time
# Initialize browser

def init_browser():
    # Replace the path with your actual path to the chromedriver

    # Windows Users
    # executable_path = {'executable_path': '/Users/cantu/Desktop/Mission-to-Mars'}
    # return Browser('chrome', **executable_path, headless=False)
    exec_path = {'executable_path': 'C:/chromedriver/chromedriver.exe'}
    return Browser('chrome', headless=True, **exec_path)


# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS


def scrape_mars_news():
    try:

        # Initialize browser
        browser = init_browser()

        #browser.is_element_present_by_css("div.content_title", wait_time=1)

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_paragraph = soup.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_paragraph

        return mars_info

    finally:
        browser.quit()


# Featured images


def scrape_mars_image():

    try:

        # Initialize browser
        browser = init_browser()

        # Visit Mars Space Images through splinter module
        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        # Visit Mars Space Images through splinter module
        browser.visit(image_url_featured)

        # HTML Object
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html_image, 'html.parser')

        # Retrieve background-image url from style tag
        featured_image_url = soup.find('article')['style'].replace(
            'background-image: url(', '').replace(');', '')[1:-1]

        # Website Url
        main_url = 'https://www.jpl.nasa.gov'

        # Concatenate website url with scrapped route
        featured_image_url = main_url + featured_image_url

        # Display full link to featured image
        featured_image_url

        # Dictionary entry from FEATURED IMAGE
        mars_info['featured_image_url'] = featured_image_url

        return mars_info
    finally:

        browser.quit()

# Mars Weather


def scrape_mars_weather():

    try:

        # Initialize browser
        browser = init_browser()

        #browser.is_element_present_by_css("div", wait_time=1)

        # Visit Mars Weather Twitter through splinter module
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)

        # HTML Object
        html_weather = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html_weather, 'html.parser')

        # Find all elements that contain tweets
        tweets = soup.find("ol", class_="stream-items")
# Find the src for the sloth image
        mars_weather = tweets.find('p', class_="tweet-text").text

        # Dictionary entry from WEATHER TWEET
        mars_info['mars_weather'] = mars_weather

        return mars_info
    finally:
        browser.quit()


# Mars Facts
def scrape_mars_facts():
    try:
    # Visit Mars facts url
     facts_url = 'http://space-facts.com/mars/'

# Use Panda's `read_html` to parse the url
     mars_facts = pd.read_html(facts_url)

# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
     mars_df = mars_facts[0]

# Assign the columns `['Description', 'Value']`
     mars_df.columns = ['Description', 'Value']

# Set the index to the `Description` column without row indexing
     mars_df.set_index('Description', inplace=True)

# Save html code to folder Assets
     data = mars_df.to_html()

# Dictionary entry from MARS FACTS
     mars_info['mars_facts'] = data
     return mars_info
    finally:
        browser.quit()

# def scrape_mars_hemisphere():

#     try:

#         browser = init_browser()
#         hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
#         browser.visit(hemispheres_url)
#         html = browser.html
#         soup = bs(html, "html.parser")
#         mars_hemisphere = []

#         products = soup.find("div", class_="result-list")
#         hemispheres = products.find_all("div", class_="item")
#         for hemisphere in hemispheres:
#             title = hemisphere.find("h3").text
#             title = title.replace("Enhanced", "")
#             end_link = hemisphere.find("a")["href"]
#             image_link = "https://astrogeology.usgs.gov/" + end_link
#             browser.visit(image_link)
#             html = browser.html
#             soup = bs(html, "html.parser")
#             downloads = soup.find("div", class_="downloads")
#             image_url = downloads.find("a")["href"]
#             mars_hemispheres.append({"title": title, "img_url": image_url})
#               return mars_hemisphere
#     finally:
#             browser.quit()

# print(scrape_mars_news())
# print(scrape_mars_image())
# print(scrape_mars_weather())
# print(scrape_mars_facts())
# print(scrape_mars_hemisphere())
def return_scrape():
    scrape_mars_news()
    scrape_mars_image()
    scrape_mars_weather()
    scrape_mars_facts()
    # scrape_mars_hemispheres()
    return mars_info
# In[ ]:
