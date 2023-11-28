import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# YOUR JSON PATH NOT MINE
cred = credentials.Certificate('/Users/michaelcassidy/Downloads/cougar-phone-deals-firebase-adminsdk-56e88-2edf050505.json')
firebase_admin.initialize_app(cred)

# firebase connect
db = firestore.client()

def get_lowest_price(model_name):
    # find the models in smartphone collect
    smartphones_ref = db.collection('smartphones')
    query = smartphones_ref.where('model', '==', model_name)
    documents = query.stream()

    # get lowest price and non amazon price
    lowest_price = None
    lowest_price_source = None
    manufacturer_price = None
    for document in documents:
        data = document.to_dict()
        price = float(data.get('price', '0').replace('$', ''))
        source = data.get('source', '').lower()

        # CHANGE THIS ACCORDING TO WHAT MODEL YOU ARE SEARCHING
        # CONSIDER MAKING THIS A VARIABLE FOR EASE OF USE
        if 'manufacturer' in source or 'samsung' in source:
            manufacturer_price = price

        # lowest price logic
        if lowest_price is None or price < lowest_price:
            lowest_price = price
            lowest_price_source = data.get('source')

    # same price logic
    if manufacturer_price is None:
        manufacturer_price = lowest_price

    return lowest_price, lowest_price_source, manufacturer_price

# REPLACE WITH EXACT PHONE NAME ACCORDING TO FIRESTORE
model_to_search = "Google Pixel 8"
lowest_price, source, manufacturer_price = get_lowest_price(model_to_search)

# Save price and unique doc iD
if lowest_price is not None:
    best_price_ref = db.collection('best_price')
    document_id = model_to_search.replace(" ", "_")  # Example: 'Galaxy_S23+'
    
    # Make the upload with data
    document_data = {
        'model': model_to_search,
        'price': lowest_price,
        'source': source,
        'manufacturer_price': manufacturer_price  
    }
    
    # Set the document with the custom ID
    best_price_ref.document(document_id).set(document_data)
    
    print(f"The lowest price for {model_to_search} is {lowest_price} from {source}. Manufacturer's price is {manufacturer_price}.")
else:
    print(f"No prices found for {model_to_search}")
