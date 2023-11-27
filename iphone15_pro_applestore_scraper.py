from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import firebase_admin
from firebase_admin import credentials, firestore
from webdriver_manager.chrome import ChromeDriverManager
import time

# CHANGE JSON PATH TO YOUR OWN
cred = credentials.Certificate('/Users/michaelcassidy/Downloads/cougar-phone-deals-firebase-adminsdk-56e88-2edf050505.json')
firebase_admin.initialize_app(cred)

# Firestore database client
db = firestore.client()

# Setup Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://www.apple.com/iphone-15-pro/'

try:
    # Open the webpage
    driver.get(url)

    # Wait for the JavaScript to populate the price data
    price_css_selector = "span.sosumi-link-follows[data-pricing-product='iphone-15-pro']"

    # Wait for the price element to have its content populated
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, price_css_selector),
            "$"  # This is the text we're expecting to be present
        )
    )

    # Now retrieve the element's text
    price_element = driver.find_element(By.CSS_SELECTOR, price_css_selector)
    price = price_element.text if price_element else 'Price not found'
    print(f'Price: {price}')

    # Generate a document ID based on the model and timestamp
    document_id = f"iPhone15 PRO_{int(time.time())}"

    # Prepare data for upload
    data = {
        'model': 'iPhone 15 PRO',
        'price': price,
        'source': 'www.apple.com/iphone-15-pro',
        'timestamp': firestore.SERVER_TIMESTAMP
    }

    # Add a new document to the smartphones collection with the specified document ID
    db.collection('smartphones').document(document_id).set(data)
    print(f"Data uploaded to Firestore with document ID: {document_id}. Price: {price}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()