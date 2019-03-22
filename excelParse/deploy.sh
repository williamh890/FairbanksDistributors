BUILD_DIR=build
OUTPUT_ZIP=lambda.zip

mkdir $BUILD_DIR -p
rm $BUILD_DIR/* -r

pip install -r requirements.txt -t $BUILD_DIR
cp chip_form.py lambda_function.py $BUILD_DIR
cd $BUILD_DIR || exit

zip $OUTPUT_ZIP * -r

aws lambda update-function-code \
  --function-name update-order-form \
  --zip-file fileb://$OUTPUT_ZIP
