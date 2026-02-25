You are performing a quick security scan and want to check whether a target repository at <code>/home/user/target-repo</code> contains any Git submodules, as these can sometimes introduce vulnerabilities if not maintained properly. 

Your task is to list all Git submodules configured in the repository. 

The output should be written to a file named <code>/home/user/target-repo/submodules_list.txt</code>, with each line containing the path and URL of each submodule as recorded in the repository’s <code>.gitmodules</code> file. The required format for each submodule is:

<pre>
path: &lt;submodule_path&gt;, url: &lt;submodule_url&gt;
</pre>

If there are no submodules configured, the file should exist and contain exactly:

<pre>
No submodules found.
</pre>

Ensure the output format is precise and matches the above specification, as an automated test will use this to verify the results.
