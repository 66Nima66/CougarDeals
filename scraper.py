# Dynamic Web Scraper for Apple.com
# For educational purposes only and not for monetary gain.
# Lawyers....for real its a dumb school project. Leave us alone please.
#
# Other scrapers are in production for more online retailers.
#
# Usage: 
# Enter the path to your Firebase json 
# pip install selenium webdriver_manager
# updated Chrome (browser will automatically open briefly)
#
# Running:
# python3 scraper.py 
#
# 


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import firebase_admin
from firebase_admin import credentials, firestore
from webdriver_manager.chrome import ChromeDriverManager

# CHANGE TO YOUR FIREBASE CREDS \/   \/   \/   \/   \/   \/ 
cred = credentials.Certificate('/Users/name/folder/.json')
firebase_admin.initialize_app(cred)

# Firestore database client
db = firestore.client()

# Setup Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://www.apple.com/iphone-15/'

try:
    # Open the webpage
    driver.get(url)

    # Wait for the jscript to populate the price data
    # CSS selector to get the right data scraped 
    price_css_selector = "span.sosumi-link-follows[data-pricing-product='iphone-15']"

    # Run until entire page is opened 
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, price_css_selector),
            "$"  # Look for the price indicator 
        )
    )

    # Element's text and print to terminal for verification 
    price_element = driver.find_element(By.CSS_SELECTOR, price_css_selector)
    price = price_element.text if price_element else 'Price not found'
    print(f'Price: {price}')

    # data for Firebase DB
    data = {
        'model': 'iPhone 15',
        'price': price,  # The scraped price
        'source': 'Apple',
        'timestamp': firestore.SERVER_TIMESTAMP  # Adds a server-side timestamp
    }

    # Add a new document to the smartphones collection
    db.collection('smartphones').add(data)
    print(f"Data uploaded to Firestore. Price: {price}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # browser close
    driver.quit()
