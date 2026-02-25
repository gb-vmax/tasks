As the backup administrator, you have a user login history file located at <code>/home/user/backup/logins.log</code>. Each line in this file contains a user ID (a single string with no spaces, e.g., <code>alice</code>, <code>bob</code>, <code>carol</code>), indicating that this user logged in at a recorded time (timestamps are not present, only user IDs per line).

Your task is to perform the following steps to create a summary report of login frequencies for archival purposes:

1. Count how many times each unique user ID appears in the <code>/home/user/backup/logins.log</code> file (i.e., how many times each user logged in).
2. Sort the user IDs by frequency, in descending order (the user with the most logins should come first).
3. For users with equal frequencies, sort them alphabetically.
4. Write the summarized results into a new file at <code>/home/user/backup/login_frequencies.txt</code>.

The output format in <code>login_frequencies.txt</code> must satisfy these constraints for the automated test:

- Each line contains the frequency (number of logins), a single space, then the user ID.
- For example, if user "alice" logged in 4 times and "bob" 2 times, the lines should be:
<pre>
4 alice
2 bob
</pre>
- All user entries in the file must be unique, with no blank lines.
- The file should contain as many lines as there are distinct user IDs in the input file.
- The first line must correspond to the most frequent user (with ties broken alphabetically).
- The input file should not be modified; only <code>login_frequencies.txt</code> must be created or overwritten as output.

Please complete this end-to-end task in the terminal.
