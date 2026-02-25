You are acting as a build engineer tasked with managing build artifacts for a software project. There is an INI configuration file located at <code>/home/user/project/artifacts.ini</code>. Each section of this INI file represents a different artifact, and within each section, keys define the artifact’s version and its file path. The INI file has the following structure:

<pre>
[artifact1]
version = 1.0.2
path = /home/user/project/bin/artifact1-1.0.2.tar.gz

[artifact2]
version = 2.5.8
path = /home/user/project/bin/artifact2-2.5.8.tar.gz

[artifact3]
version = 0.9.0
path = /home/user/project/bin/artifact3-0.9.0.tar.gz
</pre>

Your tasks are as follows:

1. Parse the <code>/home/user/project/artifacts.ini</code> file to extract all artifact names, their versions, and their file paths.
2. Check if the artifact files listed in each <code>path</code> field actually exist in the filesystem.
3. Create a log file located at <code>/home/user/project/artifact_verification.log</code>. For each artifact, log one line in the following format:
<pre>
artifact:&lt;artifact_name&gt; version:&lt;version&gt; path:&lt;path&gt; exists:&lt;yes|no&gt;
</pre>
For example, if artifact2’s file does not exist, its line should be:
<pre>
artifact:artifact2 version:2.5.8 path:/home/user/project/bin/artifact2-2.5.8.tar.gz exists:no
</pre>
4. The log file should contain one line per artifact, in the order in which they appear in the INI file.

Do not change the INI file or the artifact files themselves. The log file will be checked by automated systems to ensure the correct formatting and checking logic.
