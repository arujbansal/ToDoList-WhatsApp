from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3
from helper_functions import info_in_db, format_command_dict, fetch_column_from_db

app = Flask(__name__)

con = sqlite3.connect('user_info.db', check_same_thread=False)  # Database connection.
c = con.cursor()  # Database connection cursor.

available_commands = {'H': 'Available commands', 'A': 'A (item to be added)'}  # Command : Usage/Description


@app.route('/', methods=['POST'])
def whatsapp_message():
    phone_number = request.form['From']  # Phone number associated with the message.
    message_body = request.form['Body']  # The body of the message.
    resp = MessagingResponse()

    db_users_table = info_in_db(c, "Users")  # Gets all the information present in the Users table
    msg = ""

    if message_body.lower() == 'h':
        msg = format_command_dict(available_commands)  # Message now contains help information.

    if message_body.lower() == 'a':
        to_add = message_body[2:]  # String to add to the database (task entered by the user).
        tasks = fetch_column_from_db("Tasks", phone_number, "Users", c)  # Retrieving current tasks of the user.
        tasks.append(f'{to_add}.\n')  # Adding new task to user's current task list.

    resp.message(msg)
    return str(resp)


if __name__ == '__main__':
    app.run()
