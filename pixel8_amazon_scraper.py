import re
import time
import firebase_admin
from firebase_admin import credentials, firestore
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Firebase Admin
cred = credentials.Certificate('/Users/michaelcassidy/Downloads/cougar-phone-deals-firebase-adminsdk-56e88-2edf050505.json')  
firebase_admin.initialize_app(cred)

# Firestore database client
db = firestore.client()

# Setup Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the Amazon product page
# Replace as needed if amazon changes the landing page
url = 'https://www.amazon.com/Google-Pixel-Unlocked-Smartphone-Advanced/dp/B0CGTD5KVT?th=1'

try:
    driver.get(url)

    # Adjust the selectors based on Amazon's page structure
    price_whole_selector = "span.a-price-whole"
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, price_whole_selector)))
    
    price_whole_element = driver.find_element(By.CSS_SELECTOR, price_whole_selector)
    full_price = price_whole_element.text.strip()

    # Remove currency symbol and commas if present
    full_price = re.sub(r'[^\d.]', '', full_price)

    print(f"Price on Amazon: {full_price}")

    # Generate a document ID based on the model and timestamp
    document_id = f"Google Pixel 8_{int(time.time())}"

    # Firestore upload data
    data = {
        'model': 'Google Pixel 8',  
        'price': full_price,
        'source': 'Amazon',
        'timestamp': firestore.SERVER_TIMESTAMP
    }

    # Add a new document to the smartphones collection with the specified document ID
    db.collection('smartphones').document(document_id).set(data)
    print(f"Data uploaded to Firestore with document ID: {document_id}. Price: {full_price}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()