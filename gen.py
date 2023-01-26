import random
import smtplib
from email.mime.text import MIMEText

participants = [
    {'name': 'Alice', 'country': 'USA', 'email': 'alice@example.com', 'preferences': 'I like books and candles', 'address': '123 street'},
    {'name': 'Bob', 'country': 'Ukraine', 'email': 'bob@example.com', 'preferences': 'I like gadgets and music', 'address': '123 street'},
    {'name': 'Charlie', 'country': 'Mexico', 'email': 'charlie@example.com', 'preferences': 'I like sports and art', 'address': '123 street'},
    {'name': 'David', 'country': 'USA', 'email': 'david@example.com', 'preferences': 'I like outdoor activities and sweets', 'address': '123 street'},
    {'name': 'Eve', 'country': 'Ukraine', 'email': 'evek@example.com', 'preferences': 'I like cooking and gardening', 'address': '123 street'},
]



# Create a copy of the list of participants so we can remove them as they are matched
available_participants = participants.copy()

# Create an empty dictionary to store the matches
matches = {}

# Iterate through the participants
for participant in participants:
    # If there are no more participants from the same country, choose a random participant from the available list
    if len([p for p in available_participants if p["country"] != participant["country"]]) == 0:
        match = random.choice(available_participants)
    else:
        # Otherwise, choose a random participant from a different country
        match = random.choice([p for p in available_participants if p["country"] != participant["country"]])
    # Add the match to the dictionary
    matches[participant["name"]] = match["name"]
    # Remove the match from the available participants list
    available_participants.remove(match)

# Print the matches
for sender, receiver in matches.items():
    print(f"{sender} will send a gift to {receiver}.")
  
print("\n")
for sender, receiver in matches.items():
    print(sender)

# Connect to the email server maybe can delete
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login("admin@example.com", "password")

for sender, receiver in matches.items():
    sender_info = next(p for p in participants if p["name"] == sender)
    receiver_info = next(p for p in participants if p["name"] == receiver)
    subject = "Secret Santa project"
    message = f"""Hi, {sender}\n
    Happy to announce that you are secret santa for {receiver}!\n

    IMPORTANT INFO:\n
    Please don't contact with your reciever about secret santa as it's planned as surprise. If you have any questions or problem with address, contact me, I'll reach to your reciever with your question:
    admin@example.com

    Some info about him:
    {receiver_info["preferences"]}

    Post address:
    {receiver_info["address"]}\n

    Regards,\nSecret Santa.
    """
    msg = MIMEText(message)
    msg['Subject'] = "Secret Spinaker Santa project"
    msg['From'] = "Secret Santa <admin@example.com>"
    msg['To'] = "admin@example.com"
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login("admin@example.com", "password")
    server.send_message(msg)
    server.quit()