# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
# from dotenv import load_dotenv
# load_dotenv('credentials.env')

db_host = os.environ['MYSQL_HOST']
# db_host = 'localhost' # CAUTION! Localhost because we run this script inside the DB container!
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
cursor.execute("drop table if exists TestUsers;")

# Create a TestUsers table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE TestUsers (
      id          integer  AUTO_INCREMENT PRIMARY KEY,
      first_name  VARCHAR(30) NOT NULL,
      last_name   VARCHAR(30) NOT NULL,
      email       VARCHAR(50) NOT NULL,
      age         int,
      created_at  TIMESTAMP
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert Records
query = "insert into TestUsers (first_name, last_name, email, age, created_at) values (%s, %s, %s, %s, %s)"
values = [
  ('Bill','Gates','bill@gates.com', '65', '2020-02-11 12:00:00'),
  ('Elon','Musk','elon@mask.com', '49', '2020-02-11 12:00:00'),
  ('Mark','Zuckerberg','mark@facebook.com', '36', '2020-02-11 12:00:00')
]
cursor.executemany(query, values)
db.commit()

# Selecting Records
cursor.execute("select * from TestUsers;")
print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]
db.close()
