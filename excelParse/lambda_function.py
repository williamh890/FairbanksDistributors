import json
import pathlib as pl

import boto3

import chip_form


def lambda_handler(event=None, context=None):
    print(json.dumps(event))

    BUCKET_NAME = 'fd-order-app-storage'
    KEY = 'chipForm.xls'

    tmp = pl.Path('/') / 'tmp'
    order_xls_path = str(tmp / KEY)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)

    bucket.download_file('forms/{}'.format(KEY), order_xls_path)

    order_form_data = chip_form.get_data(order_xls_path)

    chip_data = chip_form.get_chips_by_category(order_form_data)

    json_key = 'chips.json'
    json_path = tmp / json_key

    with json_path.open('w') as f:
        json.dump(chip_data, f, indent=2)

    with json_path.open('rb') as f:
        bucket.put_object(Key=json_key, Body=f)


if __name__ == '__main__':
    lambda_handler()
