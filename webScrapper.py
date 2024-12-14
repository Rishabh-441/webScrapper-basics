from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
from tqdm import tqdm
import time

# Configure Chrome to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Enable headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU for headless compatibility
chrome_options.add_argument('--window-size=1920,1080')  # Set default window size for rendering

# Initialize the Chrome WebDriver with the options
driver = webdriver.Chrome(options=chrome_options)
# Open Amazon
driver.get('https://www.amazon.in/s?k=mobiles&crid=370P9AP6N85PI&sprefix=laptops%2Caps%2C214&ref=nb_sb_noss_2')
html_data = BeautifulSoup(driver.page_source, 'html.parser')
no_of_pages = int(html_data.find('span', {'class' : 's-pagination-item s-pagination-disabled'}).text)
print(no_of_pages)

titles = []
images = []
ratings = []
prices = []

for page in tqdm(range(no_of_pages)):
    driver.get('https://www.amazon.in/s?k=mobiles&crid=370P9AP6N85PI&sprefix=laptops%2Caps%2C214&ref=nb_sb_noss_2&page='+str(page+1))
    time.sleep(2)
    html_data = BeautifulSoup(driver.page_source, 'html.parser')
    products = html_data.find_all('div', {'data-component-type': 's-search-result'})
    for product in products:
        title = product.find('h2', {'class': 'a-size-medium a-spacing-none a-color-base a-text-normal'})
        image_url = product.find('img')
        rating = product.find('span', {'class': 'a-icon-alt'})
        price = product.find('span', {'class': 'a-price-whole'})
        titles.append(title.text)
        images.append(image_url['src'])
        if rating is None:
            ratings.append("No rating")
        else:
            ratings.append(rating.text)

        if price is None:
            prices.append('NA')
        else:
            prices.append(int(price.text.replace(',','').strip('.')))

data = pd.DataFrame({'titles':titles, 'image_url':images, 'ratings':ratings, 'prices':prices})
print(data)
data.to_csv('Laptop Products.csv')
# Pause the script to keep the browser open
input("Press Enter to close the browser...")
driver.quit()
