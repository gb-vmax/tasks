#!/bin/bash
set -e
cd /home/user

grep '\[ERROR\]' /home/user/services/payment-service/payment.log | awk -F'] ' '{print $3}' | awk -F'[][]' '{print $2}' | sort | uniq > /tmp/payment_error_components.txt && ERROR_COUNT=$(grep -c '\[ERROR\]' /home/user/services/payment-service/payment.log) && UNIQUE_COUNT=$(wc -l < /tmp/payment_error_components.txt) && { echo "---"; echo "ERROR COUNT: $ERROR_COUNT"; echo "UNIQUE COMPONENTS: $UNIQUE_COUNT"; echo "COMPONENTS LIST:"; cat /tmp/payment_error_components.txt; echo "---"; } > /home/user/services/payment-service/payment-error-summary.txt
cat /home/user/services/payment-service/payment-error-summary.txt
