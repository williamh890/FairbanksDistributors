import json
from datetime import datetime
import configparser
import smtplib

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import mimetypes

from .write_order_xlsx import write_xlsx


def place(order_data):
    filename = f"{str(datetime.now())}_order.xlsx" \
        .replace(' ', '_')

    try:
        order_id = add_order_to_db(order_data)
        send_order(filename, order_data)
    except Exception as e:
        return order_failure(str(e))
    else:
        return order_success()


def send_order(filename, order_data):
    write_xlsx(f"/tmp/{filename}", data)

    send_order_email(filename, order_data['store'])


def add_order_to_db(order_data):
    print(f'ORDER DATA: {order_data}')


def send_order_email(filename, store_name):
    smtp_config = get_smtp_config()

    email = create_email(smtp_config, filename, store_name)
    smtp_server = smtp_config['SERVER']['smtpServerURL']
    smtp_port = smtp_config['SERVER']['smtpServerPort']

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(
            smtp_config['USER']['smtpUserAddress'],
            smtp_config['USER']['smtpUserPassword']
        )
        server.send_message(email)


def get_smtp_config():
    smtp_config = configparser.ConfigParser()
    smtp_config.read('app/email_creds.cfg')

    return smtp_config


def create_email(smtp_config, filename, store_name):
    email = MIMEMultipart()
    email['Subject'] = store_name
    email['From'] = smtp_config['USER']['smtpUserAddress']
    email['To'] = smtp_config['DEST']['destAddress']

    email.attach(create_order_attachment(filename))

    return email


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


def order_success():
    return {
        "status": "order successful"
    }


def order_failure(message):
    return {
        "status": "order failed",
        "message": message
    }
