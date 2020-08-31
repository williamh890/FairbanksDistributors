import imaplib
import smtplib
from smtplib import SMTP
import logging
import email
from email.contentmanager import ContentManager
from email.message import EmailMessage
from datetime import datetime
from pathlib import Path
import configparser
import os
import time


def get_imap_config():
    config = configparser.ConfigParser()
    config.read('credentials.cfg')
    return config


def get_server():
    config = get_imap_config()
    server = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, login_message = server.login(config['CREDS']['email'],
                                      config['CREDS']['pass'])
    if typ.lower() != 'ok':
        raise Exception("Exception")

    return server


##def extract_and_write_attachment(msg):
##    attachment = msg.get_payload()[0]
##    if attachment.get_content_type() == 'application/octet-stream':
##        open('order.xlsx', 'wb').write(attachment.get_payload(decode=True))
##        os.startfile(".\{}".format('order.xlsx'), "print")


def scrape_inbox():
    server = get_server()
    server.select('inbox')
    emails = server.search(None, '(FROM "fdist.smtp@gmail.com" SUBJECT "Test")')
    ids = emails[1][0]
    ids = list((ids.decode()).split(' '))
    if ids == ['']:
        return

    content_manager = ContentManager()

    for id in ids:
        typ, data = server.fetch(id, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        if msg.is_multipart():
            config = get_imap_config()
            s = smtplib.SMTP('smtp.gmail.com',587)
##            s.ehlo()
            s.login(config['CREDS']['email']
                        config['CREDS']['pass'])
            s.starttls()
            s.sendmail('orders.fbxdist@gmail.com','9073785223@txt.att.net', 'Subject: Scrape Error\n Email scrape hanging')
            {}
            s.quit()
##            extract_and_write_attachment(msg)
        #server.store(id, '+X-GM-LABELS', '\\Trash')


def make_log_dir(log_dir):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)


def log_error(error, log_dir):
    log_file = f"{log_dir}\\{datetime.now().strftime('%x_%H')}.log"
    log_file = log_file.replace('/', '-')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fileh = logging.FileHandler(log_file, 'a')
    formatter = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s')
    fileh.setFormatter(formatter)
    logger.handlers = [fileh]
    logger.exception(error)


if __name__ == "__main__":
    log_dir = ".\\logs"
    make_log_dir(log_dir)
    while(True):
        try:
            scrape_inbox()
        except Exception as e:
            log_error(e, log_dir)
        time.sleep(15)
    # variable = input("Press something")
