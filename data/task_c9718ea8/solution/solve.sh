#!/bin/bash
set -e
cd /home/user

iconv -f UTF-8 -t ISO-8859-1 /home/user/sample_config.txt -o /home/user/sample_config_iso8859-1.txt
echo -e "Original Encoding: UTF-8\nConverted Encoding: ISO-8859-1" > /home/user/encoding_conversion_log.txt
