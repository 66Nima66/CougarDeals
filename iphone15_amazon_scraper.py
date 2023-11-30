import re
import firebase_admin
from firebase_admin import credentials, firestore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# REPLACE WITH YOUR JSON FILE \/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\
cred = credentials.Certificate('/Users/michaelcassidy/Downloads/cougar-phone-deals-firebase-adminsdk-56e88-2edf050505.json')  
firebase_admin.initialize_app(cred)

# Firestore database client
db = firestore.client()

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to the Amazon product page
    # iphone 15 url to amazon
    driver.get("https://www.amazon.com/iphone-15/s?k=iphone+15")

    # Wait for the price element to be visible on the page
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "a-price"))
    )

    # Retrieve the whole number part of the price
    price_whole_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
    price_whole = price_whole_element.text.strip().replace(',', '').replace('.', '')

    # Retrieve the decimal part of the price
    price_fraction_element = driver.find_element(By.CLASS_NAME, "a-price-fraction")
    price_fraction = price_fraction_element.text.strip()

    # Combine the whole number and the decimal part to get the full price
    full_price = f"{price_whole}.{price_fraction}"

    # Print price to terminal for verification
    print(f"Price on Amazon: {full_price}")

    # Firestore upload data
    data = {
        'model': 'iPhone 15', 
        'price': full_price,
        'source': 'Amazon',
        'timestamp': firestore.SERVER_TIMESTAMP  # Adds a server-side timestamp
    }

    # Add a new document to the smartphones collection
    db.collection('smartphones').add(data)
    print(f"Data uploaded to Firestore. Price: {full_price}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
