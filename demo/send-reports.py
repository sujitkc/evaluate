#!/usr/bin/python3

import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass

class Email:
  def __init__(self, sender, subject, body, attachment, password, receiver, smtpServer):
    self.sender     = sender
    self.password   = password
    self.receiver   = receiver
    self.subject    = subject
    self.body       = body
    self.attachment = attachment
    self.smtpServer = smtpServer

  def send(self):
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = self.sender

    # storing the receivers email address
    msg['To'] = self.receiver

    # storing the subject
    msg['Subject'] = self.subject # "Assignment 3 Automated evaluation report"

    # attach the body with the msg instance
    msg.attach(MIMEText(self.body, 'plain'))

    # open the file to be sent
#    filename = roll_number + ".tar.gz"
    attachment = open(self.attachment, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % self.attachment)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.outlook.office365.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
#    password = getpass.getpass("Enter your password: ")
    s.login(self.sender, self.password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(self.sender, self.receiver, text)

    # terminating the session
    s.quit()

class Mailer:
  def __init__(self, data):
    self.sender     = 'sujitkc@iiitb.ac.in'
    self.subject    = "Assignment 5 evaluated solutions"
    self.data       = data
    self.smtpServer = 'smtp.outlook.office365.com:587'
    self.password   = getpass.getpass()

    # string to store the body of the mail
    with open("mail-body.txt", "r") as content_file:
      self.body = content_file.read()

  def send_mails(self):
    for (roll_number, receiver) in self.data:
      print("Sending report to " + roll_number + " ...")
      try:
        email    = Email(  sender     = self.sender, \
                         password   = self.password, \
                         receiver   = receiver, \
                         subject    = self.subject, \
                         body       = self.body, \
                         attachment = "evaluated-package/" + roll_number + ".tar.gz", \
                         smtpServer = self.smtpServer )
        email.send()
        print("Sending report to " + roll_number + " ... done.")
      except FileNotFoundError as e:
        print("Failed due to " + str(e))

def read_csv(filename):
  reader = csv.reader(open(filename, 'r'))
  rows = list(reader)
  rows.pop(0)
  return [(row[0], row[2]) for row in rows]

if __name__ == "__main__":
  data = read_csv("../../class.csv")

  mailer = Mailer(data)
 # mailer = Mailer([("Sujit", "sujitkc@gmail.com")])
  mailer.send_mails()
