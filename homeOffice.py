import re

from bs4 import BeautifulSoup
import requests

def computerDesks():
    # Define a dictionary to put the values in later
    itemDict = {}

    # Access multiple pages
    pageNum = 0
    try:
        for page in range(1, 5):
            pageNum += 1

            # Step 1: Get website
            url = f"https://eurekaergonomic.com/computer-desks/?sort=featured&page={pageNum}"
            req = requests.get(url).text
            doc = BeautifulSoup(req, "html.parser")

            # Search for relevant content on the page
            page_content = doc.find(class_="page-content")
            page_results = page_content.find_all(text=re.compile("Desk|DESK"))

            # Get the link from the values
            for item in page_results:
                parent = item.parent
                if parent.name != "a":
                    continue

                # if the parent name is an <a> tag then use the link variable to copy it down
                link = parent['href']
                # Search the product for the text using its class and then find the price
                next_parent = item.find_parent(class_="card epic-product-card")
                price = next_parent.find(class_="price price--withoutTax price-data-now-value").text
                # For each product, display the price and link to it
                itemDict[item] = {"Price": price, "Link": link}


    except AttributeError:
        print("FINISHED SCRAPING DESKS!!!")
    print("FINISHED SCRAPING DESKS!!!")

    # Save values to a txt file
    with open("desks.txt", "w") as txt:
        for key, value in itemDict.items():
            txt.write('%s : %s\n' % (key,value))

def computerChairs():
    # Define a dictionary to put the values in later
    itemDict = {}

    # Access multiple pages
    pageNum = 0
    try:
        for page in range(1, 5):
            pageNum += 1
            url = f"https://eurekaergonomic.com/chairs/?sort=featured&page={pageNum}"
            req = requests.get(url).text
            doc = BeautifulSoup(req, "html.parser")

            # Search for relevant content on the page
            page_content = doc.find(class_="page-content")
            page_results = page_content.find_all(text=re.compile("Chair|CHAIR"))

            # Get the link from the values
            for item in page_results:
                parent = item.parent
                if parent.name != "a":
                    continue

                # if the parent name is an <a> tag then use the link variable to copy it down
                link = parent['href']

                next_parent = item.find_parent(class_="card epic-product-card")
                price = next_parent.find(class_="price price--withoutTax price-data-now-value").text
                itemDict[item] = {"Price": price, "Link": link}

            # Return the results
    except AttributeError:
        print("FINISHED SCRAPING CHAIRS!!!")

    # Save values to a txt file
    with open("chairs.txt", "w") as txt:
        for key, value in itemDict.items():
            txt.write('%s : %s\n' % (key, value))


def computerAccessories():
    # Define a dictionary to put the values in later
    itemDict = {}

    # Access multiple pages
    pageNum = 0
    try:
        for page in range(1, 5):
            pageNum += 1

            # Step 1: Get website
            url = f"https://eurekaergonomic.com/accessories/?sort=featured&page={pageNum}"
            req = requests.get(url).text
            doc = BeautifulSoup(req, "html.parser")
 
            # Search for relevant content on the page
            page_content = doc.find(class_="page-content")
            page_results = page_content.find_all(text=re.compile("Desk|DESK"))

            # Get the link from the values
            for item in page_results:
                parent = item.parent
                if parent.name != "a":
                    continue

                # if the parent name is an <a> tag then use the link variable to copy it down
                link = parent['href']
                # Search the product for the text using its class and then find the price
                next_parent = item.find_parent(class_="card epic-product-card")
                price = next_parent.find(class_="price price--withoutTax price-data-now-value").text
                # For each product, display the price and link to it
                itemDict[item] = {"Price": price, "Link": link}


    except AttributeError:
        print("FINISHED SCRAPING ACCESSORIES!!!")

    # Save values to a txt file
    with open("accessories.txt", "w") as txt:
        for key, value in itemDict.items():
            txt.write('%s : %s\n' % (key, value))

computerDesks()
computerChairs()