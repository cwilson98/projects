# import libraries
import re
import pandas as pd

from bs4 import BeautifulSoup
import requests

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from password import password

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pendulum

# Define dataframe to put items into later
office_list = []

# Function to retrieve computer desks
def computerDesks():

    # Grab the page content from eureka ergonomics for desks
    url = "https://eurekaergonomic.com/collections/computer-desks"
    page = requests.get(url)
    doc = BeautifulSoup(page.content,"html.parser")

    # Find the desk content within the class
    content = doc.find(class_="collection__products collection-items--4 collection-items--mobile--one-whole")
    desks = content.find_all(text=re.compile('Desk|DESK'))

    # Loop through each desk and its information
    for item in desks:
        parent = item.parent
        if parent.name != 'a':
            continue

        # Retrieve the link of each desk
        desk_link = "https://eurekaergonomic.com/" + parent['href']

        # Since not all elements are part of the same class, I use regex to find all that start with a specific pattern
        product_pattern = re.compile(r"^product-grid-item grid__item one-quarter mobile--one-whole")
        product_tab = item.find_parent(attrs={'class': product_pattern})

        # Find all prices with the specified class
        current_price = product_tab.find(attrs={'class': "product-grid-item__price__new"})
        regular_price = product_tab.find(attrs={'class': "product-grid-item__price price"}).text.lstrip("From ")
        if current_price:
            office_list.append([item, 'Desk', current_price.text, desk_link])
        else:
            office_list.append([item, 'Desk', regular_price, desk_link])
    # print(office_list)

#  Function to retrieve computer desks
def computerChairs():

# Grab the page content from eureka ergonomics for chairs
    url = "https://eurekaergonomic.com/collections/desk-chairs"
    page = requests.get(url)
    doc = BeautifulSoup(page.content,"html.parser")

    # Find the chairs within the class
    content = doc.find(class_="collection__products collection-items--4 collection-items--mobile--one-whole")
    chairs = content.find_all(text=re.compile('Chair'))


# Loop through each chair and its information
    for item in chairs:
        parent = item.parent
        if parent.name != 'a':
            continue

        # Retrieve the link of each chair
        chair_link = "https://eurekaergonomic.com/" + parent['href']

        # Since not all elements are part of the same class, I use regex to find all that start with a specific pattern
        product_pattern = re.compile(r"^product-grid-item grid__item one-quarter mobile--one-whole")
        product_tab = item.find_parent(attrs={'class': product_pattern})

        # Find all prices with the specified class
        current_price = product_tab.find(attrs={'class': "product-grid-item__price__new"})
        regular_price = product_tab.find(attrs={'class': "product-grid-item__price price"}).text.lstrip("From ")
        if current_price:
            office_list.append([item, 'Chair', current_price.text, chair_link])
        else:
            office_list.append([item, 'Chair', regular_price, chair_link])

def computerStorage():

    url = "https://eurekaergonomic.com/collections/storages"
    page = requests.get(url)
    doc = BeautifulSoup(page.content,"html.parser")
    #
    # Find the chairs within the class
    content = doc.find(class_="collection__products collection-items--4 collection-items--mobile--one-whole")
    storage_units = content.find_all(text=re.compile('Cabinet|Cart|shelf|Shelf|Shelves|stand'))
    # print(storage_units)
#
# Loop through each storage unit and its information
    for item in storage_units:
        parent = item.parent
        if parent.name != 'a':
            continue

        # Retrieve the link of each unit
        storage_link = "https://eurekaergonomic.com/" + parent['href']
        # print(storage_link)
#
#       # Since not all elements are part of the same class, I use regex to find all that start with a specific pattern
        product_pattern = re.compile(r"^product-grid-item grid__item one-quarter mobile--one-whole")
        product_tab = item.find_parent(attrs={'class': product_pattern})
#
#       # Find all prices with the specified class
        current_price = product_tab.find(attrs={'class': "product-grid-item__price__new"})
        regular_price = product_tab.find(attrs={'class': "product-grid-item__price price"}).text.lstrip("From ")
        if current_price:
            office_list.append([item, 'Storage', current_price.text, storage_link])
        else:
            office_list.append([item, 'Storage', regular_price, storage_link])
    # print(office_list)

    # Create dataframe, add all items to it and export it as a csv
    office = pd.DataFrame(office_list, columns=['Name', 'Type', 'Price', 'Link'])
    officeItems = office.to_csv(r'C:\Users\Chris\PycharmProjects\Projects\DE_Projects\homeOffice\office.csv',header=True,index=False)
    return officeItems
#
#
# Function that sends email to specified email address
def sendEmail():
    # Create message object
    message = MIMEMultipart()

    # identify the sender, receiver, and message contents
    message["from"] = "Christopher Wilson"
    message["to"] = "cwilson83@live.com"
    message["subject"] = "Web Scraping Project Results"
    message.attach(MIMEText("Here is a csv file containing the products from Eureka Ergonomics and a txt file documenting the process"))
    with open(r'C:\Users\Chris\PycharmProjects\Projects\DE_Projects\homeOffice\office.txt','r') as file1:
        message.attach(MIMEText(file1.read()))
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
#
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

storageScraper = PythonOperator(
    task_id='Scrape_Accessories',
    python_callable=computerStorage,
    dag=dag
)

emailMe = PythonOperator(
    task_id='Email',
    python_callable=sendEmail,
    dag=dag
)

deskScraper >> chairScraper >> storageScraper >> emailMe
computerLog("SCRAPING DESKS!")
computerDesks()
computerLog("FINISHED SCRAPING DESKS!")
computerLog("SCRAPING CHAIRS!")
computerChairs()
computerLog("FINISHED SCRAPING DESKS!")
computerLog("SCRAPING ACCESSORIES!")
computerStorage()
computerLog("FINISHED SCRAPING ACCESSORIES!")
computerLog("SENDING EMAIL!")
sendEmail()
computerLog("EMAIL SENT!")
