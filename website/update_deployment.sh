#!/bin/bash
MATURITY=$1

update_deployment() {
    S3_BUCKET=$1
    CDN_ID=$2

    npm run build
    cd dist

    echo "Updating s3 bucket ${S3_BUCKET}"
    aws s3 sync . "s3://${S3_BUCKET}"

    echo "Invalidating index.html for cloudfront distro ${CDN_ID}"
    aws cloudfront create-invalidation \
        --distribution-id $CDN_ID \
        --paths /index.html /favicon.ico
}

if [ "$MATURITY" = "" ]; then
    echo "./update-deployment.sh dev|prod"
elif [ "$MATURITY" = "dev" ]; then
   update_deployment \
       "fdak-orders.com-dev" \
       "E2UTKX4LYDPNZT"
elif [ "$MATURITY" = "prod" ]; then
   update_deployment \
       "fdak-orders.com" \
       "E39BCHG6PX5TX7"
else
    echo "Unrecognized maturity '${MATURITY}'."
fi
