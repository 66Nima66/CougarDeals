from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import firebase_admin
from firebase_admin import credentials, firestore
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Firebase Admin  CHANGE TO YOUR SPECIFIC DB!!!!!!!!!!!!!!!!!
cred = credentials.Certificate('/Users/michaelcassidy/Downloads/cougar-phone-deals-firebase-adminsdk-56e88-2edf050505.json')
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

    # Look for the css selector
    price_css_selector = "span.sosumi-link-follows[data-pricing-product='iphone-15']"

    # Wait for Sel. to find the price and the dynamic html to load
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, price_css_selector),
            "$"  # dollar sign is the giveaway for applestore html
        )
    )

    # retrieve and store the price
    price_element = driver.find_element(By.CSS_SELECTOR, price_css_selector)
    price = price_element.text if price_element else 'Price not found'
    print(f'Price: {price}')

    # Generate a document ID based on the model and timestamp
    document_id = f"iPhone15_{int(time.time())}"

    # firebase upload data
    data = {
        'model': 'iPhone 15',
        'price': price,
        'source': 'Apple',
        'timestamp': firestore.SERVER_TIMESTAMP
    }

    # Add a new phone to smartphone collect with unique ID
    db.collection('smartphones').document(document_id).set(data)
    print(f"Data uploaded to Firestore with document ID: {document_id}. Price: {price}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()




