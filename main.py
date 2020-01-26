from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import sqlite3
from helper_functions import info_in_db, format_command_dict, fetch_column_from_db, update_column, reformat_db_info, \
    add_numbering

app = Flask(__name__)

con = sqlite3.connect('user_info.db', check_same_thread=False)  # Database connection.
c = con.cursor()  # Database connection cursor.

available_commands = {'H': 'Available commands', 'A': 'A (item to be added)',
                      'R': 'R (Number of item to be removed)'}  # Command : Usage/Description


@app.route('/', methods=['POST'])
def whatsapp_message():
    phone_number = request.form['From']  # Phone number associated with the message.
    message_body = request.form['Body']  # The body of the message.
    f_let = message_body[0].lower()  # First letter of received msg.
    resp = MessagingResponse()

    if f_let == 'h':  # Command = Help
        msg = format_command_dict(available_commands)  # Message now contains help information.
    elif f_let == 'c':  # Command = Clear
        update_column("Tasks", "Users", phone_number, c, con, '')  # Updates database information. Clears task list.
        msg = "Your tasks list has been cleared."
    else:
        msg_workon = message_body[2:]  # String to be worked on.
        tasks = fetch_column_from_db("Tasks", phone_number, "Users", c)  # Retrieving current tasks of the user.
        tasks = reformat_db_info(tasks)  # Makes into proper list.

        if f_let == 'a':  # Command = Add
            tasks.append(f'{msg_workon}.\n')  # Adding new task to user's current task list.
        elif f_let == 'r':  # Command = Remove
            tasks.pop(int(msg_workon) - 1)  # Removing task from user's current task list. 0 based indexing.

        tasks_for_db = "".join(tasks)  # Tasks in string format to add to the database.
        update_column("Tasks", "Users", phone_number, c, con, tasks_for_db)  # Updates database information.

        if not tasks:
            msg = "No remaining tasks..."
        else:
            msg = "Task list:\n"
            msg += add_numbering(tasks)  # Ready to be sent to the user.

    resp.message(msg)
    return str(resp)


if __name__ == '__main__':
    app.run()
