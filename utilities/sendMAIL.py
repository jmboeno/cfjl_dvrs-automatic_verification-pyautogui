from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from ..contants import EMAIL, HOST, PASSWORD, PORT


def send():
    server = smtplib.SMTP(HOST, PORT)

    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASSWORD)

    corpo = "Processo automatizado de verificação diária de câmeras e DRV's (Ver anexo)"

    email_msg = MIMEMultipart()
    email_msg['From'] = EMAIL
    email_msg['To'] = EMAIL
    email_msg['Subject'] = 'CFTV - Verificação diária'
    email_msg.attach(MIMEText(corpo, 'plain'))

    cam_arquivo = "monitoramento.pdf"
    attachment = open(cam_arquivo, 'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition',
                   f'attachment; filename=monitoramento.pdf')
    attachment.close()
    email_msg.attach(att)

    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())

    server.quit()
