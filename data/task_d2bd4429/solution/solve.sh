#!/bin/bash
set -e
cd /home/user

(cd /home/user/ml_data/raw_images && python3 -m http.server 8080 &) && sleep 2 && mkdir -p /home/user/ml_data/fetched && curl -fsS http://localhost:8080/cat1.jpg -o /home/user/ml_data/fetched/cat1_copy.jpg && echo -e "Original file: /home/user/ml_data/raw_images/cat1.jpg\nDownloaded file: /home/user/ml_data/fetched/cat1_copy.jpg\nStatus: SUCCESS" > /home/user/ml_data/download_log.txt
(cd /home/user/ml_data/raw_images && python3 -m http.server 8080 &) && sleep 2 && mkdir -p /home/user/ml_data/fetched && wget -qO /home/user/ml_data/fetched/cat1_copy.jpg http://localhost:8080/cat1.jpg && echo -e "Original file: /home/user/ml_data/raw_images/cat1.jpg\nDownloaded file: /home/user/ml_data/fetched/cat1_copy.jpg\nStatus: SUCCESS" > /home/user/ml_data/download_log.txt
mkdir -p /home/user/ml_data/fetched && python3 -c "import urllib.request; urllib.request.urlretrieve('http://localhost:8080/cat1.jpg', '/home/user/ml_data/fetched/cat1_copy.jpg')" && echo -e "Original file: /home/user/ml_data/raw_images/cat1.jpg\nDownloaded file: /home/user/ml_data/fetched/cat1_copy.jpg\nStatus: SUCCESS" > /home/user/ml_data/download_log.txt
cat /home/user/ml_data/download_log.txt
