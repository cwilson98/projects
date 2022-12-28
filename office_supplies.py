# import libraries
import re
from bs4 import BeautifulSoup
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Define dictionaries to put items into later
officeDict = {}

# Get main website
url = f"https://eurekaergonomic.com/computer-desks/"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")


# Function to retrieve computer desks
def computerDesks():
    # Get the page number
    try:
        page = int(doc.find(class_="pagination-link").text)

        # Loop through pages until the end
        while page < 6:
            new_url = f"https://eurekaergonomic.com/computer-desks/?page={page}"
            new_page = requests.get(new_url).text
            new_doc = BeautifulSoup(new_page,"html.parser")
            page_content = new_doc.find(class_="page-content")

            # Set a variable equal to the desks
            page_results = page_content.find_all(text=re.compile("Desk|DESK"))

            for item in page_results:
                new_item = item.strip()
                parent = item.parent

                # Set a parameter equal to the link of the desk
                link = parent['href']
                next_parent = item.find_parent(class_="card-body")

                # Set variables equal to both the current and previous price of the desk
                price = next_parent.find(class_="price price--withoutTax price-data-now-value").text

                # Add desk, link and price to dictionary
                officeDict[new_item] = {"price": price, "link": link}

            # Increase page number
            page += 1
    except AttributeError:
        pass

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

        # Set a variable equal to the chairs
        page_results = page_content.find_all(text=re.compile("Chair"))

        for item in page_results:
            new_item = item.strip()
            parent = item.parent

            # Set a variable equal to the link of the chair
            link = parent['href']

            next_parent = item.find_parent(class_="card-body")

            # Set variables equal to both the current and previous price of the chair
            price = next_parent.find(class_="price price--withoutTax price-data-now-value").text

            # Add desk, link and price to dictionary
            officeDict[new_item] = {"price": price, "link": link}

        # Increase page number
        page += 1

def computerAccessories():
    # Get the page number
    page = int(doc.find(class_="pagination-link").text)

    # Loop through pages until the end
    while page < 3:
        new_url = f"https://eurekaergonomic.com/accessories/?page={page}"
        new_page = requests.get(new_url).text
        new_doc = BeautifulSoup(new_page, "html.parser")
        page_content = new_doc.find(class_="page-content")

        # Set a parameter equal to the all accessories on the page
        page_results = page_content.find_all(text=re.compile("Pad|Cart|Cabinet"))

        for item in page_results:
            new_item = item.strip()
            parent = item.parent

            # Set a parameter equal to the link of the accessory
            link = parent['href']

            next_parent = item.find_parent(class_="card-body")

            # Set a variable equal to the price of the accessory
            price = next_parent.find(class_="price price--withoutTax price-data-now-value").text

            # Add desk, link and price to dictionary
            officeDict[new_item] = {"price": price, "link": link}

        # Increase page number
        page += 1

    # Create text file for the items
    with open("office_supplies.txt", "w") as txt:
        for key, value in officeDict.items():
            txt.write('%s : %s\n' % (key, value))



computerDesks()
computerChairs()
computerAccessories()





















