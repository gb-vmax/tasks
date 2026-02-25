You are a monitoring specialist tasked with setting up custom alert triggers and outputs for a local service. 

1. Create a new directory at /home/user/alerts/.
2. Inside this directory, write an alerts configuration file named service_alerts.conf with exactly the following parameters:
    - THRESHOLD=85
    - NOTIFY_EMAIL=on
    - LOGFILE=/home/user/alerts/alert.log
    - ENABLED=true

   Each parameter should be on its own line, using only uppercase letters for the keys, and NO extra spaces around = signs.
   
3. Next, create an empty log file at /home/user/alerts/alert.log with permissions set so that only the owner (user) can read and write to it.
   
4. Finally, simulate triggering an alert by writing exactly this line into /home/user/alerts/alert.log:
   [2024-06-11 12:00:00] ALERT: THRESHOLD exceeded (value: 92)

Format details to be checked:
- The /home/user/alerts/service_alerts.conf file must have only the four parameters above, each on its own line, in the given order.
- The /home/user/alerts/alert.log file must contain ONLY the single line shown, matching the timestamp and wording exactly.
- Permissions on /home/user/alerts/alert.log must be set to -rw------- (owner read/write only).

Use your Linux terminal to complete the steps. Ask for a verification log if you wish to confirm your setup.
