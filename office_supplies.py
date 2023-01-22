# import libraries
import re
import pandas as pd
import pendulum

from bs4 import BeautifulSoup
import requests

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from password import password

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define list to put items into later
officeList = []

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

                # Add desk, link and price to list
                officeList.append([new_item,price,link,"desk"])

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

            # Add chair, link and price to list
            officeList.append([new_item,price,link,"chair"])

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

            # Add accessories, link and price to list
            officeList.append([new_item,price,link,"accessory"])

        # Increase page number
        page += 1

    # Create dataframe, add all items to it and export it as a csv
    office = pd.DataFrame(officeList, columns=['Name', 'Price', 'Link', 'Type'])
    officeItems = office.to_csv(r'C:\Users\Chris\PycharmProjects\Projects\DE_Projects\homeOffice\office.csv',header=True,index=False)
    return officeItems


# Function that sends email to specified email address
def sendEmail():
    # Create message object
    message = MIMEMultipart()

    # identify the sender, receiver, and message contents
    message["from"] = "Christopher Wilson"
    message["to"] = "cwilson83@live.com"
    message["subject"] = "Web Scraping Project Results"
    message.attach(MIMEText("Here is a text file containing the products from Eureka Ergonomics"))
    with open(r'C:\Users\Chris\PycharmProjects\Projects\DE_Projects\homeOffice\office.csv','rb') as file:
        message.attach(MIMEApplication(file.read(),Name='office.csv'))

    # Establish connection to gmail
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("swaggaman73@gmail.com", password)
        smtp.send_message(message)

    # Close connection
    smtp.close()

# Function that logs each step of the project
def computerLog(message):
    timestamp_format = '%H:%M:%S on %h/%d/%Y'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("office.txt", "a") as file:
        file.write(message + " at " + timestamp + '\n')

default_args = {
    'owner': 'Christopher Wilson',
    'start_date': pendulum.today('UTC').add(days=2),
    'email': ['cwilson83@live.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='Eureka-ETL',
    default_args=default_args,
    description='A python data pipeline that scrapes https://eurekaergonomic.com/computer-desks/ for chairs, desks, and accessories',
    schedule=timedelta(days=1),
)

deskScraper = PythonOperator(
        task_id='Scrape_Desks',
        python_callable=computerDesks,
        dag=dag
    )

chairScraper = PythonOperator(
    task_id='Scrape_Chairs',
    python_callable=computerChairs,
    dag=dag
)

accessoryScraper = PythonOperator(
    task_id='Scrape_Accessories',
    python_callable=computerAccessories,
    dag=dag
)

emailMe = PythonOperator(
    task_id='Email',
    python_callable=sendEmail,
    dag=dag
)

deskScraper >> chairScraper >> accessoryScraper >> emailMe
computerLog("SCRAPING DESKS!")
computerDesks()
computerLog("FINISHED SCRAPING DESKS!")
computerLog("SCRAPING CHAIRS!")
computerChairs()
computerLog("FINISHED SCRAPING DESKS!")
computerLog("SCRAPING ACCESSORIES!")
computerAccessories()
csvfile = computerAccessories()
computerLog("FINISHED SCRAPING ACCESSORIES!")
computerLog("SENDING EMAIL!")
sendEmail()
computerLog("EMAIL SENT!")



















