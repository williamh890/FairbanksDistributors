import imaplib
import email
from email.contentmanager import ContentManager
import configparser
import os

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

def extract_and_write_attachment(msg):
    attachment = msg.get_payload()[0]
    if attachment.get_content_type() == 'application/octet-stream':
        open('order.xlsx', 'wb').write(attachment.get_payload(decode=True))
        os.startfile(".\{}".format('order.xlsx'), "print")

def scrape_inbox():
    server = get_server()
    server.select('inbox')
    emails = server.search(None, 'FROM', '"fdist.smtp@gmail.com"')
    ids = emails[1][0]
    ids = list((ids.decode()).split(' '))
    if ids == ['']: return

    content_manager = ContentManager()

    for id in ids:
        typ, data = server.fetch(id, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        if msg.is_multipart():
            extract_and_write_attachment(msg)
        server.store(id, '+X-GM-LABELS', '\\Trash')


if __name__ == "__main__":
    try:
        scrape_inbox()
    except Exception as e:
        print(e)
    # variable = input("Press something")
