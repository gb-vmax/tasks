You are a mobile build engineer maintaining pipelines. Please follow these steps:

1. In your home directory (/home/user), initialize a new git repository named <b>pipeline-utils</b> inside /home/user/pipeline-utils, if it does not already exist.
2. In the repository, create a file named <b>build_status.txt</b> containing exactly the following two lines (with a single newline between the lines):

<pre>
Pipeline: Android Release
Status: Success
</pre>

3. Add and commit this file with the commit message <b>Initial build status</b>.
4. Tag this commit with the tag <b>build-v1.0</b>.

After you have completed these steps, create a verification log file named <b>/home/user/pipeline-verification.log</b>. This file must contain exactly the following data in this order:
<ul>
<li>The git commit hash of the most recent commit (first line)</li>
<li>The commit message (second line)</li>
<li>The build_status.txt content (third and fourth lines exactly as specified above)</li>
<li>The name of the tag that points at the most recent commit (fifth line)</li>
</ul>
Each data item should be on its own line, and no extra lines or spaces should be present.
