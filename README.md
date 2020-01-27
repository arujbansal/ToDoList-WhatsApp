# ToDoList-WhatsApp
Hey there! This repository contains the code for a WhatsApp bot. This bot will basically let you add tasks to a list and remove them. It formats them in a clear readable manner. The code has been divided into functions and moved into a seperate file (helper functions). All the code is clearly documented.

# Tweaking The Code
This project uses the Twilio API to send and receive WhatsApp messages. Since the basic function of sending WhatsApp messages is the same, you can use the basic project structure to add your own functionality. Eg. An AI chatbot can be implemented.

# Using The Bot
1. Download the code and install the required packages (can be found in requirements.txt).
2. Run the create database file if it does not already exist.
3. Run the add users file to add users to the database.
4. Install ngrok (https://ngrok.com/product). Follow the instructions given on their website to set it up.
5. Create an account on Twilio (https://www.twilio.com/).
6. Follow the instructions given under Sandbox Participants (https://www.twilio.com/console/sms/whatsapp/sandbox).
7. Run the ngrok server on port 5000 or whatever port the flask server is running on (instructions can be found on the ngrok website.)
8. Add the ngrok URL to the WhatsApp sandbox area (configure the webhook at https://www.twilio.com/console/sms/whatsapp/sandbox).
9. Start sending messages!
