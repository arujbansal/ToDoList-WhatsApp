import sqlite3

#######################################################
# Run this file if the database does not already exist.
#######################################################

conn = sqlite3.connect('user_info.db')  # Creates a new database.
c = conn.cursor()

# Creating the Users table.
c.execute(
    'CREATE TABLE Users(ID INTEGER PRIMARY KEY AUTOINCREMENT, Username TEXT NOT NULL, Phone TEXT NOT NULL, Tasks TEXT)')
conn.commit()  # Saving the Users table.
conn.close()  # Close database connection.
