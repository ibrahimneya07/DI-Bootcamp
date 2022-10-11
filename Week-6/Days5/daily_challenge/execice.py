'''Using this API,
    create the functionality which will write 10
    random countries to your database.
'''
import requests
import psycopg2
url="https://restcountries.com/v2/alpha/col"
response = requests.get(url)

print(response.json()['name'])
print(response.json()['capital'])
print(response.json()['flag'])
print(response.json()['subregion'])
print(response.json()['population']) 

print()
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'resto'
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
query = "insert into country(name,capital,flag,subregion,population) values()"
