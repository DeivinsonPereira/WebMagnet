import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

# Makes an HTTP request to the Mercado Livre website
url = 'https://lista.mercadolivre.com.br/ofertas'
response = requests.get(url)

# Extracts the desired information from the HTML of the page
soup = BeautifulSoup(response.content, 'html.parser')
products = soup.find_all(class_='andes-card')

# Creates a list to store the collected information
products_list = []

# Extracts the information from each product and adds it to the list
for product in products:
    name = product.find(class_='ui-search-item__title').text.strip()
    price = product.find(class_='andes-money-amount__fraction').text.strip()
    cents = product.find(class_='andes-money-amount__cents').text.strip()
    correct_price = ("R$" + price + "," + cents)
    products_list.append((name, correct_price))
    print(name)
    print(correct_price)

# Creates a DataFrame with the collected information
df = pd.DataFrame(products_list, columns=['Name', 'Correct_price'])

# Connects to the SQLite database and creates the "products" table
conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS products (name TEXT, correct_price TEXT)')

# Inserts the collected information into the "products" table
for index, row in df.iterrows():
    cursor.execute('INSERT INTO products (name, correct_price) VALUES (?, ?)', (row['Name'], row['Correct_price']))

# Saves the changes to the database and closes the connection

conn.commit()
conn.close()