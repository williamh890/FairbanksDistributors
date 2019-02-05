import configparser
from flask import Blueprint, request, url_for, redirect
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import mimetypes

order = Blueprint('order', __name__)

@order.route('/order_success')
def order_success():
    return 'order_successful'

@order.route('/place_order', methods=['POST', 'GET'])
def place_order():
    if request.method == 'POST':
        print(request.form)
        write_order_csv(request.form)
        send_order()
    else:
        write_order_csv("testing")
        send_order()
    return redirect(url_for('order.order_success'))

def write_order_csv(order_info):
    with open("order.csv", "w") as order:
        order.write(order_info)

def send_order():
    smtp_config = get_smtp_config()

    email = create_email(smtp_config)

    with smtplib.SMTP_SSL(smtp_config['SERVER']['smtpServerURL'],
                         smtp_config['SERVER']['smtpServerPort']) as server:
        server.login(smtp_config['USER']['smtpUserAddress'],
                smtp_config['USER']['smtpUserPassword'])
        server.send_message(email)

def get_smtp_config():
    smtp_config = configparser.ConfigParser()
    smtp_config.read('app/email_creds.cfg')
    return smtp_config

def create_email(smtp_config):
    email = MIMEMultipart()
    email['Subject'] = 'An order'
    email['From'] = smtp_config['USER']['smtpUserAddress']
    email['To'] = smtp_config['DEST']['destAddress']

    ctype, encoding = mimetypes.guess_type("order.csv")
    if ctype is None or encoding is not None:
        print("henlo")
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)
    attachment = MIMEBase(maintype, subtype)

    with open("order.csv", "rb") as order:
        attachment.set_payload(order.read())

    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename="order.csv")
    email.attach(attachment)

    return email
