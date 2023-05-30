from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from bs4 import BeautifulSoup
import pandas as pd


review_list = []

# define a function to scrape the reviews from each page, input is a tuple from start page to end page
def scrape_reviews(page_range: tuple):
    for page_number in range(page_range[0], page_range[1]+1):
        try:
            # Create a new instance of the Chrome driver
            driver = webdriver.Chrome()
            driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P"+str(page_number)+".htm?filter.iso3Language=eng")
            
            # Find all elements with matching XPath
            review_elements = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
            
            # Iterate through each element and extract the text
            for element in review_elements:
                review = element.text
                # append each review to a list
                review_list.append(review)
            #close the driver
            driver.quit()
        except:
            # if a unknown error occurs, try again
            driver = webdriver.Chrome()
            driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P"+str(page_number)+".htm?filter.iso3Language=eng")
            ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
            for element in ids:
                review = element.text
            review_list.append(review)
            driver.quit()
            # continue to the next page
            continue

# convert the list to a dictionary
review_dict = {}
for i in range(len(review_list)):
    review_dict[i+1] = review_list[i]
# convert the dictionary to a csv file
df = pd.DataFrame.from_dict(review_dict, orient='index', columns=['review'])

# create the following columns in the df: overall rates, status(whether the reviewer is a current employee or not),title,date,position,location,pros,cons.
# split the review column into the above columns
df['overall_rates'] = df['review'].str.split('\n', expand=True)[0]
df['status'] = df['review'].str.split('\n', expand=True)[2]
df['title'] = df['review'].str.split('\n', expand=True)[3]
# the date,position,location information is all in a single split row, so we need to split it again
# the date and the position split by a '-', and the position and the location split by a string ' in '
df['date'] = df['review'].str.split('\n', expand=True)[4].str.split('-', expand=True)[0]
df['position'] = df['review'].str.split('\n', expand=True)[4].str.split('-', expand=True)[1].str.split(' in ', expand=True)[0]
df['location'] = df['review'].str.split('\n', expand=True)[4].str.split('-', expand=True)[1].str.split(' in ', expand=True)[1]

df['pros'] = df['review'].str.split('\n', expand=True)[9]
df['cons'] = df['review'].str.split('\n', expand=True)[11]

# if the pros and cons have "-" in front of the text, remove it
df['pros'] = df['pros'].str.replace('-','')
df['cons'] = df['cons'].str.replace('-','')
# fill the NaN values with 'None'
df = df.fillna('None')

# create a new df withou the review column
df_reviews = df.drop(columns=['review'])