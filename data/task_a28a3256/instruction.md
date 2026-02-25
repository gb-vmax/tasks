As a DevSecOps engineer, you are enforcing a company policy to regularly check authentication logs for entries related to failed user logins. You have a log file located at <code>/home/user/security/audit.log</code>. The policy requires that all lines containing the exact phrases “Failed password” or “authentication failure” (matching case-sensitive, occurring anywhere in the line) must be extracted and summarized into a new report. 

Your task is as follows:

1. Filter the <code>/home/user/security/audit.log</code> file to include **only** lines containing either the exact phrase <code>Failed password</code> or <code>authentication failure</code> (both must be matched case-sensitively as full phrases).
2. Write the filtered lines into a new file named <code>/home/user/security/failed_logins.report</code>.
3. The report must contain **only** the matching lines, in the order they appear in the original log, with no blank lines or extra information.
4. Display the contents of <code>/home/user/security/failed_logins.report</code> in your terminal so that the results can be visually verified.

The correctness of your solution will be checked by automated tests looking for an exact line-by-line match. Ensure your filtering is precise, and do not include lines that do not strictly match one of the two phrases.
