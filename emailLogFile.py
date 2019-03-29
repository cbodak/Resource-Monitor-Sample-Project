import smtplib

from email.message import EmailMessage

#Read the log file
fileToRead = open("logfile.txt")

#Set the content of the email to the file that was read
msgToSend = EmailMessage()
msgToSend.set_content(fileToRead.read())

#Set the subject, from, and to fields of the email
msgToSend['Subject'] = "Cloud Usage Monitor Log File"
msgToSend['From'] = "Cloud.Testing2019@gmail.com"
msgToSend['To'] = "Cloud.Testing2019@gmail.com"

#Set the server to send from and send the email
server = smtplib.SMTP('smtp.gmail.com', 587);
server.starttls();
server.login("Cloud.Testing2019@gmail.com", "Cloud123Testing$");
server.send_message(msgToSend)
server.quit()