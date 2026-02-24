You are working as a developer on a Python project located at <code>/home/user/my_python_project</code>. Inside this project directory, you have two configuration files: <code>settings.yaml</code> and <code>config.toml</code>. 

Your task is to update and organize these configuration files according to the following instructions:

1. In the <code>/home/user/my_python_project/settings.yaml</code> file, under a top-level section called <code>database</code>, add the following keys and values:
   <ul>
      <li><code>host: localhost</code></li>
      <li><code>port: 5432</code></li>
      <li><code>user: admin</code></li>
      <li><code>password: secret123</code></li>
   </ul>
   The YAML file must have the <code>database</code> key as the root-level key, containing the other keys (host, port, user, password) as indented properties inside it. Use YAML syntax with 2 spaces per indentation level.

2. In the <code>/home/user/my_python_project/config.toml</code> file, create a section named <code>[project]</code> (if not present) and add the following key-value pairs under it:
   <ul>
      <li><code>name = "my_python_project"</code></li>
      <li><code>version = "1.0.0"</code></li>
   </ul>
   The TOML file should follow standard TOML format, with the <code>[project]</code> section header in square brackets, and each key-value pair on its own line directly underneath.

3. To verify your changes, create a log file at <code>/home/user/my_python_project/config_update.log</code> listing the current contents of both configuration files. The format of the log must be:
   <ul>
      <li>The first line: <code>=== settings.yaml ===</code></li>
      <li>Then, the full contents of <code>settings.yaml</code></li>
      <li>Next line: <code>=== config.toml ===</code></li>
      <li>Then, the full contents of <code>config.toml</code></li>
   </ul>

Example (with exact formatting):

<pre>
=== settings.yaml ===
database:
  host: localhost
  port: 5432
  user: admin
  password: secret123
=== config.toml ===
[project]
name = "my_python_project"
version = "1.0.0"
</pre>
Make sure that both configuration files are updated exactly as described and that the log file matches the output format given.
