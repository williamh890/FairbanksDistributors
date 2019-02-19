import csv
import configparser
from flask import Blueprint, jsonify, request, url_for, redirect
import json
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import mimetypes

order = Blueprint('order', __name__)

@order.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response

def order_success():
    return jsonify({"status":"order successful"})

@order.route('/place_order', methods=['POST', 'GET'])
def place_order():
    if request.method == 'POST':
        data = json.loads(request.form[''])
        write_order_csv(data)
        send_order()
    else:
        write_order_csv({"store":"safeway", "order":{"item":{"upc":"test", "amount":0}}})
        send_order()
    return order_success()

def write_order_csv(order_info):
    with open("/tmp/order.csv", "w") as order_file:
        order_writer = csv.writer(order_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        order_writer.writerow(['store'])
        order_writer.writerow([order_info['store']])

        order_writer.writerow(['upc', 'amount'])
        order = order_info["order"]
        for k,v in order.items():
            order_writer.writerow([v['upc'], v['amount']])

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

def create_order_attachment():
    ctype, encoding = mimetypes.guess_type("order.csv")
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)
    attachment = MIMEBase(maintype, subtype)

    with open("/tmp/order.csv", "rb") as order:
        attachment.set_payload(order.read())

    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment",
                          filename="order.csv")

    return attachment

def create_email(smtp_config):
    email = MIMEMultipart()
    email['Subject'] = 'An order'
    email['From'] = smtp_config['USER']['smtpUserAddress']
    email['To'] = smtp_config['DEST']['destAddress']

    email.attach(create_order_attachment())

    return email
