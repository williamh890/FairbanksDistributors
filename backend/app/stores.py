import json

import psycopg2
from flask import jsonify


class Store:
    def __init__(self, id, name, chain_id):
        self.id = id
        self.name = name
        self.chain_id = chain_id

    @classmethod
    def from_row(cls, row):
        id, name, chain_id = row
        return cls(id, name, chain_id)

    def to_dict(self):
        return {
            'storeName': self.name,
            'rsr': []
        }


def load_chips():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM stores')
        stores = cursor.fetchall()

        store_dicts = [
            Store.from_row(row).to_dict() for row in stores
        ]

        return jsonify(store_dicts)

    except Exception as e:
        return jsonify({
            'error': str(e)
        })


def load_bread():
    pass


def connect():
    config = db_config()

    return psycopg2.connect(
        user=config['user'],
        password=config['pass'],
        host=config['host'],
        port=config['port'],
        database=config['database']
        )


def db_config():
    with open('db-config.json', 'r') as f:
        return json.load(f)
