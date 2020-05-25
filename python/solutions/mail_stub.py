from email.mime.text import MIMEText
import smtplib

class EmailClient:
    def __init__(self, server_addr):
        self._server = server_addr

    def send(self, frm, to, subject, text):
        # TODO: send an email
        pass
