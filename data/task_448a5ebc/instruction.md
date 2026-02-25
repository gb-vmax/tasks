You are acting as a release manager preparing for an application deployment. Your task is to ensure secure and correct use of environment variables using a dotenv file.

1. Create a new file called <b>/home/user/deploy/.env.production</b> with the following exact key-value pairs (each on a separate line with no quotes, spaces, or extra newlines):

<pre>
APP_ENV=production
DB_HOST=db.prod.company.com
DB_USER=release_manager
DB_PASS=Sup3rS3cret!
</pre>

2. Then, load these values into your current shell session so that they are available as environment variables.
3. After sourcing, write a verification log file at <b>/home/user/deploy/env_check.log</b>. This log must have the following precise format, one line for each variable:
<pre>
APP_ENV=[value]
DB_HOST=[value]
DB_USER=[value]
DB_PASS=[value]
</pre>
(The values should be the exact values loaded into the environment variables for the current shell at the time you write the log.)

Make sure <b>/home/user/deploy/env_check.log</b> exists and contains only those four lines in the specified order, with no extra output or blank lines. This will be used to verify that the environment was configured correctly.
