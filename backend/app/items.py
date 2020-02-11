from . import db

from flask import jsonify


class Item:
    def __init__(self, item_name, category_name, ounces, pack_quantity, upc):
        self.item_name = item_name
        self.category_name = category_name
        self.ounces = ounces
        self.pack_quantity = pack_quantity
        self.upc = upc

    @classmethod
    def from_row(cls, row):
        return cls(*row)

    def to_dict(self):
        return {
            'name': self.item_name,
            'case': self.default(self.pack_quantity),
            'oz': self.default(self.ounces),
            'upc': self.default(self.upc)
        }

    def default(self, val, default_val=''):
        return val if val is not None else default_val


def load_chips():
    return load_items('Chips')


def load_freezer_bread():
    return load_items('Freezer Bread')


def load_fresh_bread():
    return load_items('Fresh Bread')


def load_items(item_type):
    with db.connect() as connection:
        try:
            cursor = connection.cursor()
            query = items_query(item_type)
            cursor.execute(query)
            item_rows = cursor.fetchall()

            items = [
                Item.from_row(row) for row in item_rows
            ]

            categories = [item.category_name for item in items]
            items_by_categories = {
                category_name: [] for category_name in categories
            }

            for item in items:
                items_by_categories[item.category_name].append(item.to_dict())

            return jsonify(items_by_categories)

        except Exception as e:
            return jsonify({
                'error': str(e)
            })


def items_query(item_type):
    return f'''
        SELECT item_name,
               category_name,
               ounces,
               pack_quantity,
               upc
          FROM category_types
                 JOIN categories ON category_types.type_id = categories.type_id
                 JOIN items ON categories.category_id = items.category_id
         WHERE type_name = '{item_type}'
           AND is_active = TRUE
         ORDER BY category_name, item_name;
    '''
