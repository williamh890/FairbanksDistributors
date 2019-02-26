import json
import chip_form
import boto3


def lambda_handler(event=None, context=None):
    BUCKET_NAME = 'fd-order-app-storage'  # replace with your bucket name
    KEY = 'chipForm.xls'  # replace with your object key

    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).download_file(KEY, '/tmp/chipForm.xls')

    chip_form.make_json(chip_form.get_data())


if __name__ == '__main__':
    lambda_handler()