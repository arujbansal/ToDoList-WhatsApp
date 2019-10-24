from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3
from helper_functions import info_in_db

app = Flask(__name__)

con = sqlite3.connect('user_info.db', check_same_thread=False)  # Database connection.
c = con.cursor()  # Database connection cursor.


@app.route('/', methods=['POST'])
def whatsapp_message():
    phone_number = request.form['From']  # Phone number associated with message.
    message_body = request.form['Body']  # The body of the message.
    resp = MessagingResponse()

    db_users_table = info_in_db(c, "Users")  # Gets all the information present in the Users table

    return 'Hello World'


if __name__ == '__main__':
    app.run()
