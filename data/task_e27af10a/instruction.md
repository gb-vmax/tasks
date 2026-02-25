As a configuration manager, you need to track user modifications to a configuration file. You have a file located at <code>/home/user/config/settings.cfg</code> containing multiple lines, each of the format <code>key=value</code>. Your task is to extract all keys whose values have been changed from the default value "unchanged", and save these keys to a file at <code>/home/user/config/modified_keys.txt</code>. 

The <code>settings.cfg</code> file might look like this:
<pre>
user=alice
timeout=unchanged
theme=dark
autosave=unchanged
language=en
</pre>

You should extract the following keys: <code>user</code>, <code>theme</code>, and <code>language</code> (since their values are not <code>unchanged</code>), and write them each on a new line in the output file <code>/home/user/config/modified_keys.txt</code>. The output format must be exactly one key per line, with no additional spaces or blank lines.

Please ensure the output file is overwritten if it already exists, and contains only the keys (without values or extra text).
