You are a system administrator maintaining several servers. In the directory <code>/home/user/server_configs/</code>, there is an INI file named <code>prod_server.ini</code> that contains configuration details for a production server. 

Your task is to parse the INI file and extract all the key-value pairs under the section <code>[Database]</code>. Then, print each key-value pair in the following output format, using a single Linux command (for example, using <code>grep</code>, <code>awk</code>, <code>sed</code> or similar utilities):

<pre>
key1=value1
key2=value2
key3=value3
</pre>

where each <code>key=value</code> line must correspond exactly to the key and value found under <code>[Database]</code> in <code>/home/user/server_configs/prod_server.ini</code>, and appear in the same order as they are in the INI file. There should be no extra spaces around =, no blank lines, and no additional output.

Make sure the output does not include the section header itself (like <code>[Database]</code>) or lines from any other sections.
