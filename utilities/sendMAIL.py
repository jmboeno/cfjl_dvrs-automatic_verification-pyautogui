from datetime import datetime
from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from config.constants import EMAIL_SENDER, HOST, PASSWORD, PORT


def send(emails_receivers):

    cam_arquivo = "CHECK_DVRS_"+datetime.today().strftime('%Y-%m-%d')+".pdf"
    attachment = open(cam_arquivo, 'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition',
                   f'attachment; filename=CHECK_DVRS_'+datetime.today().strftime('%Y-%m-%d')+'.pdf')
    attachment.close()

    email_msg = MIMEMultipart()
    body = "Processo automatizado de verificação diária de câmeras e DRV's (Ver anexo)"
    email_msg.attach(MIMEText(body, 'plain'))
    email_msg.attach(att)

    for email in emails_receivers:
        print("Enviando email para: ", email)
        email_msg['From'] = EMAIL_SENDER
        email_msg['To'] = email
        email_msg['Subject'] = 'CFTV - Verificação diária'

        try:
            server = smtplib.SMTP(HOST, PORT)
            server.ehlo()
            server.starttls()
            server.login(EMAIL_SENDER, PASSWORD)
            server.sendmail(EMAIL_SENDER, email,
                            email_msg.as_string())
            server.quit()
            print('Email enviado!')
        except smtplib.SMTPException:
            print("Error: Ocorreu um erro ao enviar o email")
