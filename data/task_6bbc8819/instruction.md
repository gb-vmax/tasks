You are assisting an automation specialist with preparing precise configuration files for a multi-stage deployment workflow. You must perform the following steps sequentially:

1. In the directory <code>/home/user/workflows</code>, ensure there are two configuration files: 
<ul>
  <li><code>deploy.yaml</code></li>
  <li><code>settings.toml</code></li>
</ul>

2. Open <code>/home/user/workflows/deploy.yaml</code> and:
<ul>
    <li>Add a new workflow called <code>staging_deploy</code> under a top-level key called <code>workflows</code> (creating it if it doesn’t exist).</li>
    <li>Under <code>staging_deploy</code>, define the following structure <b>exactly</b>:
      <pre>
workflows:
  staging_deploy:
    description: "Deploy to staging environment"
    steps:
      - name: build
        command: "./scripts/build.sh"
      - name: test
        command: "./scripts/test.sh"
      - name: deploy
        command: "./scripts/deploy.sh"
      </pre>
    </li>
</ul>

3. Open <code>/home/user/workflows/settings.toml</code> and:
    <ul>
      <li>Create (or modify) a <code>[staging]</code> table with the following values:
        <ul>
          <li><code>url</code> = "<code>https://staging.example.com</code>"</li>
          <li><code>api_key</code> = "<code>STAGING123ABC</code>"</li>
          <li><code>timeout</code> = <code>60</code></li>
        </ul>
      </li>
    </ul>

4. Once you have completed the above steps, create a log file at <code>/home/user/workflows/config_edit.log</code> containing, line by line:
    <ul>
      <li>A timestamped line for when you edited/deployed the YAML file, in the format: <code>[YYYY-MM-DD HH:MM:SS] Edited deploy.yaml</code></li>
      <li>A timestamped line for when you edited/deployed the TOML file, in the format: <code>[YYYY-MM-DD HH:MM:SS] Edited settings.toml</code></li>
    </ul>
    Use the 24-hour time format and the system's current date/time for the timestamps.

The automated test will check both the precise structure and contents of <code>deploy.yaml</code> and <code>settings.toml</code>, as well as the format of <code>config_edit.log</code>. Ensure that the indentation and value quoting (where required) matches the specification above.
