You are a release manager preparing deployment configuration files for an upcoming software release. In the directory <code>/home/user/release_configs</code>, you will find two configuration files: <code>app.yaml</code> and <code>database.toml</code>.

Perform the following updates to prepare the files for deployment:

1. In <code>/home/user/release_configs/app.yaml</code>, update the version under the top-level key <code>release</code> to <code>2.1.0</code>. 
2. In the same YAML file, add a new key <code>changelog</code> (at the top level, after <code>release</code>). This key’s value must be a YAML list containing exactly these two bullet points (in this order): <code>Added feature X</code> and <code>Fixed bug Y</code>.
3. In <code>/home/user/release_configs/database.toml</code>, update the field <code>connection.max_active</code> to the integer value <code>40</code>.

<mark>After making these changes, create a plain-text log file at <code>/home/user/release_configs/config_update.log</code> that must contain exactly the following lines, one per update and in this order:</mark>
<ul>
    <li>Updated app.yaml release version to 2.1.0</li>
    <li>Added changelog to app.yaml</li>
    <li>Set database.toml connection.max_active to 40</li>
</ul>
All files should be saved with the described changes.
