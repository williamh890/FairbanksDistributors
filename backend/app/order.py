import configparser
from flask import Blueprint, request, url_for, redirect
import smtplib
from email.mime.text import MIMEText

order = Blueprint('order', __name__)

@order.route('/order_success')
def order_success():
    return 'order_successful'

@order.route('/place_order', methods=['POST', 'GET'])
def place_order():
    if request.method == 'POST':
        print(request.form)
        send_order(request.form)
    else:
        send_order("testing")
    return redirect(url_for('order.order_success'))


def send_order(order_info):
    smtp_config = get_smtp_config()

    email = create_email(order_info, smtp_config)

    with smtplib.SMTP_SSL(smtp_config['SERVER']['smtpServerURL'],
                         smtp_config['SERVER']['smtpServerPort']) as server:
        server.login(smtp_config['USER']['smtpUserAddress'],
                smtp_config['USER']['smtpUserPassword'])
        server.send_message(email)

def get_smtp_config():
    smtp_config = configparser.ConfigParser()
    smtp_config.read('app/email_creds.cfg')
    return smtp_config

def create_email(order_info, smtp_config):
    email = MIMEText(order_info)
    email['Subject'] = 'An order'
    email['From'] = smtp_config['USER']['smtpUserAddress']
    email['To'] = smtp_config['DEST']['destAddress']

    return email
