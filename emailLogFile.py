import smtplib;

import email.message;

#Read the log file
fileToRead = open("logfile.txt");

#Set the content of the email to the file that was read
msgToSend = email.message.EmailMessage();
msgToSend.set_content(fileToRead.read());

#Set the subject, from, and to fields of the email
msgToSend['Subject'] = "Cloud Usage Monitor Log File";
msgToSend['From'] = "cbodak@uwo.ca";
msgToSend['To'] = "cbodak@uwo.ca";

#Set the server to send from and send the email
server = smtplib.SMTP('localhost');
server.send_message(msgToSend);
server.quit();