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

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
# Open the desired URL of the first web page
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P1.htm?filter.iso3Language=eng")
# Find all the elements with the specified XPath
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
# Iterate through each element and extract the text
for element in ids:
    review = element.text
#put the text into a dictionary, each review is a value, and key starts from 1
review_dict = {}
for i in range(len(ids)):
    review_dict[i+1] = ids[i].text   
driver.quit()

# the same process for the second page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P2.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+11] = ids[i].text
driver.quit()

# the same process for the third page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P3.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+21] = ids[i].text
driver.quit()

# the same process for the fourth page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P4.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+31] = ids[i].text
driver.quit()

# the same process for the fifth page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P5.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+41] = ids[i].text
driver.quit()

# the same process for the sixth page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P6.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+51] = ids[i].text
driver.quit()

# the same process for the seventh page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P7.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+61] = ids[i].text
driver.quit()

# the same process for the eighth page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P8.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+71] = ids[i].text
driver.quit()

# the same process for the ninth page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P9.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+81] = ids[i].text
driver.quit()

# the same process for the tenth page
driver = webdriver.Chrome()
driver.get("https://www.glassdoor.co.uk/Reviews/Zara-Reviews-E17544_P10.htm?filter.iso3Language=eng")
ids = driver.find_elements(By.XPATH, '//*[starts-with(@id, "empReview_")]')
for element in ids:
    review = element.text
for i in range(len(ids)):
    review_dict[i+91] = ids[i].text
driver.quit()

print(review_dict)

# convert the dictionary into a dataframe
df = pd.DataFrame.from_dict(review_dict, orient='index', columns=['Review'])
# save the dataframe into a csv file
df.to_csv('F:/Meta/Web/Zara_reviews.csv', index=False, encoding='utf-8-sig')