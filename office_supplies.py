# import libraries
import re
from bs4 import BeautifulSoup
import requests

# Define dictionaries to put items into later
deskDict = {}
chairDict = {}

# Get main website
url = f"https://eurekaergonomic.com/computer-desks/"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")


# Function to retrieve computer desks
def computerDesks():
    # Get the page number
    page = int(doc.find(class_="pagination-link").text)
    
    # Loop through pages until the end
    while page < 6:
        new_url = f"https://eurekaergonomic.com/computer-desks/?page={page}"
        new_page = requests.get(new_url).text
        new_doc = BeautifulSoup(new_page,"html.parser")
        page_content = new_doc.find(class_="page-content")
        
        # Set a parameter equal to the desks
        page_results = page_content.find_all(text=re.compile("Desk|DESK"))
        
        for item in page_results:
            new_item = item.strip()
            parent = item.parent
            
            # Set a parameter equal to the link of the desk
            link = parent['href']
            next_parent = item.find_parent(class_="card-body")
            
            # Set a parameter equal to the link of the desk
            price = next_parent.find(class_="price price--withoutTax price-data-now-value").text
            
            # Add desk, link and price to dictionary
            deskDict[new_item] = {"price": price, "link": link}
            
        # Increase page number
        page += 1
    
    # Create text file for desks
    with open("desks.txt", "w") as txt:
        for key, value in deskDict.items():
            txt.write('%s : %s\n' % (key,value))

# Function to retrieve computer desks
def computerChairs():
    
    # Get the page number
    page = int(doc.find(class_="pagination-link").text)

    # Loop through pages until the end
    while page < 3:
        new_url = f"https://eurekaergonomic.com/chairs/?page={page}"
        new_page = requests.get(new_url).text
        new_doc = BeautifulSoup(new_page, "html.parser")
        page_content = new_doc.find(class_="page-content")

        # Set a parameter equal to the chairs
        page_results = page_content.find_all(text=re.compile("Chair"))
        
        for item in page_results:
            new_item = item.strip()
            parent = item.parent

            # Set a parameter equal to the link of the chair
            link = parent['href']
            
            next_parent = item.find_parent(class_="card-body")

            # Set a parameter equal to the price of the chair
            price = next_parent.find(class_="price price--withoutTax price-data-now-value").text

            # Add desk, link and price to dictionary
            chairDict[new_item] = {"price": price, "link": link}
        
        # Increase page number
        page += 1

    # Create text file for chairs
    with open("chairs.txt", "w") as txt:
        for key, value in chairDict.items():
            txt.write('%s : %s\n' % (key, value))

computerChairs()
computerDesks()











