import psutil
import smtplib

from email.message import EmailMessage

#Set the content of the email to the file that was read
msgToSend = EmailMessage();
msgToSend.set_content("The Resource Monitor has stopped running.");

#Set the subject, from, and to fields of the email
msgToSend['Subject'] = "Cloud Usage Monitor has Stopped Running";
msgToSend['From'] = "Cloud.Testing2019@gmail.com";
msgToSend['To'] = "Cloud.Testing2019@gmail.com";
processFound = 0;

#Check if the Resource Monitor is running
while(1):
    for proc in psutil.process_iter():
        #If the process is found in the list of processes, print that it is working and exit the loop
        if "theprocess" in proc.name().lower():
            print("working...");
            processFound = 1;
            break;
    #If the process was not found, send the email
    if(processFound == 0):
        server = smtplib.SMTP('smtp.gmail.com', 587);
        server.starttls();
        server.login("Cloud.Testing2019@gmail.com", "Cloud123Testing$");
        server.send_message(msgToSend);
        server.quit();
    #Reset processFound to 0
    processFound = 0;

        


