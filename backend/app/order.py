import json
from datetime import datetime
import configparser
import smtplib

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import mimetypes
from flask import jsonify, request

from .write_order_xlsx import write_xlsx


def place():
    filename = f"{str(datetime.now())}_order.xlsx" \
        .replace(' ', '_')

    if request.method == 'POST':
        try:
            data = json.loads(request.form['order'])
            write_xlsx(f"/tmp/{filename}", data)
            send_order(filename, data['store'])
        except Exception as e:
            return order_failure(str(e))
    else:
        write_xlsx(f"/tmp/{filename}", {"date": "2002-02-02", "store": "safeway",
                                        "items": [{"name": "chip", "upc": "test", "amount": 0}]})
        send_order(filename, "safeway")
    return order_success()


def send_order(filename, store_name):
    smtp_config = get_smtp_config()

    email = create_email(smtp_config, filename, store_name)

    with smtplib.SMTP_SSL(smtp_config['SERVER']['smtpServerURL'],
                          smtp_config['SERVER']['smtpServerPort']) as server:
        server.login(smtp_config['USER']['smtpUserAddress'],
                     smtp_config['USER']['smtpUserPassword'])
        server.send_message(email)


def get_smtp_config():
    smtp_config = configparser.ConfigParser()
    smtp_config.read('app/email_creds.cfg')
    return smtp_config


def create_order_attachment(filename):
    ctype, encoding = mimetypes.guess_type(filename)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)
    attachment = MIMEBase(maintype, subtype)

    with open(f"/tmp/{filename}", "rb") as order:
        attachment.set_payload(order.read())

    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment",
                          filename=f"{str(datetime.now())}_order.xlsx")

    return attachment


def create_email(smtp_config, filename, store_name):
    email = MIMEMultipart()
    email['Subject'] = store_name
    email['From'] = smtp_config['USER']['smtpUserAddress']
    email['To'] = smtp_config['DEST']['destAddress']

    email.attach(create_order_attachment(filename))

    return email


def order_success():
    return jsonify({"status": "order successful"})


def order_failure(message):
    return jsonify({"status": "order failed",
                    "message": message})
