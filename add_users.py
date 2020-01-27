import sqlite3
from helper_functions import insert_column

con = sqlite3.connect('user_info.db', check_same_thread=False)  # Database connection.
c = con.cursor()  # Database connection cursor.

num = int(input("How many users do you want to add?: "))  # Number of users to be added to the database.
print("Please enter the phone number in this format:")
print("+(countrycode)(number)")
print("Eg. +91981038384 for a number in India")
for user in range(num):
    print("\n")
    name = input(f'Enter User No. {user + 1}s username: ')
    number = input(f'Enter User No. {user + 1}s number: ')
    insert_column("Users", name, number, c, con)

con.close()
