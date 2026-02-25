As a FinOps analyst, you need to prepare and securely share a summary report of your cloud cost optimization for Q2. First, create a text file named <code>/home/user/cloud_cost_report_Q2.txt</code> containing the plaintext line: 
<pre>
Cloud cost savings for Q2: $18,430
</pre>
Next, generate a new GPG key for user "Jane Finops" with email jane.finops@example.com (no passphrase required). Use this key to digitally sign <code>/home/user/cloud_cost_report_Q2.txt</code> in <strong>detached signature</strong> format, resulting in <code>/home/user/cloud_cost_report_Q2.txt.sig</code> in the same directory. Then, encrypt <code>/home/user/cloud_cost_report_Q2.txt</code> using Jane's public key, producing an encrypted file named <code>/home/user/cloud_cost_report_Q2.txt.gpg</code>.

Finally, verify the file signature and output the verification result to <code>/home/user/cloud_cost_report_verification.log</code> in the following format:
<pre>
[DATE TIME] Verification status: [GOOD or BAD] signature for cloud_cost_report_Q2.txt
</pre>
For example:
<pre>
[2024-06-21 15:42:55] Verification status: GOOD signature for cloud_cost_report_Q2.txt
</pre>
Use the <strong>local system time</strong> for the timestamp and ensure the message matches this exact template for automated checking. Only write the verification result to <code>/home/user/cloud_cost_report_verification.log</code>.
