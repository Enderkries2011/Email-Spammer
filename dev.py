import smtplib
from tqdm import tqdm

#Dev Test
subject_dev = "A subject"
message_dev = "the stuff of the email u see"
num_emails_dev = "999"
receiver_dev = "example_receiver@gmail.com"

sender = "example_sender@gmail.com"
sender_password = "1234 1234 1234 1234" # App Password

text = f"Subject: {subject_dev}\n\n{message_dev}"

server = smtplib.SMTP("smtp.gmail.com", 587) #SMTP Settings
server.starttls()
server.login(sender, sender_password)

for i in tqdm(range(int(num_emails_dev)), unit="emails", desc="Sending emails"):
    server.sendmail(sender, receiver_dev, text)

print("All emails have been sent!")                #The file is called dev.py cause u can change it in here instead of inputs each time
