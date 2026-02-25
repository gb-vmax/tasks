I have a directory at /home/user/ml_data/raw_images containing several JPEG files. I want to prepare this data for a training run by creating a local HTTP server using Python's built-in HTTP server module, serving the /home/user/ml_data/raw_images directory on port 8080. Once the server is running, verify its availability by downloading an image named cat1.jpg (which is present in the directory) from the server at http://localhost:8080/cat1.jpg. Save this downloaded file to /home/user/ml_data/fetched/cat1_copy.jpg.

After you complete these steps, please generate a log file at /home/user/ml_data/download_log.txt with the following format, replacing the placeholders as needed:
```
Original file: /home/user/ml_data/raw_images/cat1.jpg
Downloaded file: /home/user/ml_data/fetched/cat1_copy.jpg
Status: SUCCESS
```
Make sure the log file is exactly as shown above. The log will be used for automated verification.
