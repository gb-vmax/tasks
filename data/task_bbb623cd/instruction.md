You are an assistant to a database administrator who is optimizing query performance. In the directory <code>/home/user/db_query_optim</code>, there is a set of SQL query template files:

<ul>
  <li><code>/home/user/db_query_optim/query_prod.sql</code></li>
  <li><code>/home/user/db_query_optim/query_test.sql</code></li>
  <li><code>/home/user/db_query_optim/query_dev.sql</code></li>
</ul>

Right now, applications running in different environments use a symlinked file called <code>active_query.sql</code> in the same directory to refer to one of these templates. For optimization, you need to perform the following steps:

<ol>
  <li>Create a subdirectory <code>/home/user/db_query_optim/old_links</code> if it does not exist.</li>
  <li>If there is already a symlink named <code>active_query.sql</code> in <code>/home/user/db_query_optim</code>, move it into <code>/home/user/db_query_optim/old_links</code>. Do NOT move it if it is not a symlink.</li>
  <li>Create three new symlinks in <code>/home/user/db_query_optim</code> named:</li>
  <ul>
    <li><code>active_query_prod.sql</code> &rarr; pointing to <code>/home/user/db_query_optim/query_prod.sql</code></li>
    <li><code>active_query_test.sql</code> &rarr; pointing to <code>/home/user/db_query_optim/query_test.sql</code></li>
    <li><code>active_query_dev.sql</code> &rarr; pointing to <code>/home/user/db_query_optim/query_dev.sql</code></li>
  </ul>
  <li>Create a plain text report <code>/home/user/db_query_optim/symlink_report.txt</code> listing each of these new symlinks on a separate line in the following format (do not include any lines except these):</li>
</ol>

<pre>
[symlink name] -> [path it points to]
</pre>

For example, the line for the production symlink should read exactly as:
<pre>
active_query_prod.sql -> /home/user/db_query_optim/query_prod.sql
</pre>

Repeat this for all three new symlinks in the specified order: prod, test, dev.

After completing the task, the <code>/home/user/db_query_optim/symlink_report.txt</code> file should contain exactly three lines, one for each symlink, in the precise format above. Ensure that each symlink points to the absolute path. Ensure all paths, file names, and output formats strictly follow this specification.
