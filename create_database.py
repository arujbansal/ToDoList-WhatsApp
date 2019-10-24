import sqlite3

conn = sqlite3.connect('user_info.db')  # Creates a new database
c = conn.cursor()

# Creating Users table
c.execute('''CREATE TABLE Users (ID INTEGER PRIMARY KEY AUTOINCREMENT, Username TEXT NOT NULL, Phone TEXT NOT NULL)''')
