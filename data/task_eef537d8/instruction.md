You are acting as a container specialist managing a set of microservices. There is a log file at /home/user/services/payment-service/payment.log containing logs from the "payment-service" microservice. 

Your task is to analyze this log file as follows:
1. Find and count the number of ERROR entries in the log. Log lines are structured as:  
   [YYYY-MM-DD HH:MM:SS] [LEVEL] [component] Message  
   (For example: [2024-06-13 09:04:04] [ERROR] [transactions] Failed to process payment)
2. Find and count how many unique components have logged an ERROR.
3. Create a summary file at /home/user/services/payment-service/payment-error-summary.txt with the following exact format:

---  
ERROR COUNT: X  
UNIQUE COMPONENTS: Y  
COMPONENTS LIST:  
component1  
component2  
...  
---

Where:
- X is the total ERROR entries found.
- Y is the count of unique components that logged ERRORs.
- COMPONENTS LIST is a newline-separated list of the unique components (in any order).

Only include data related to ERROR log entries (ignore other levels such as INFO or WARNING). Make sure the summary file strictly follows the formatting given above so that automated checks can verify it.
