import smtplib
from tqdm import tqdm

sender = "exmple_sender@gmail.com" #Email
sender_password = "1234 1234 1234 1234" # App Password

subject = input("Subject: ") # Email Subject
message = input("Message: ") # Email Message "The text that u read"

num_emails = int(input("Enter the number of emails to send: ")) # Amount of spammmmm

receiver = input("Receiver Email:") # Receiver Email

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587) # SMTP Settings
server.starttls()
server.login(sender, sender_password)

for i in tqdm(range(num_emails), unit="emails", desc="Sending emails"):
    server.sendmail(sender, receiver, text)

print("All emails have been sent!")
