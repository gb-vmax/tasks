You are assisting an infrastructure engineer who needs to automate the process of synchronizing configuration files to a remote server as part of provisioning. Your task is to prepare for future automation by simulating the remote synchronization step locally.

Start by creating a directory at <b>/home/user/source_configs</b> and place a single file named <b>nginx.conf</b> in it. The <b>nginx.conf</b> file should contain exactly this text (including newlines and indentation):

<pre>
user www-data;
worker_processes auto;
pid /run/nginx.pid;
</pre>

Next, create another directory called <b>/home/user/remote_server/configs</b>.

Synchronize (copy) the entire contents of <b>/home/user/source_configs</b> into <b>/home/user/remote_server/configs/</b> in a way that exactly matches what rsync would do, i.e., only the <b>nginx.conf</b> file should appear in the target directory, and its contents must be identical.

As verification, generate a synchronization log at <b>/home/user/sync.log</b> listing each file that was copied, one per line, using the format:

<pre>
COPIED: /path/to/copied/file
</pre>

For this task, the log must contain only the line:

<pre>
COPIED: /home/user/remote_server/configs/nginx.conf
</pre>

Do not include any additional output or log lines. Once this is complete, inform the user that the synchronization is finished and that the log has been generated.
