You are developing a Python utility script that uses configuration files to manage environment variables for deployment. There are two configuration files in your home directory: <code>/home/user/deploy_settings.yaml</code> and <code>/home/user/deploy_settings.toml</code>.

Both files contain identical contents and specify a list under the key or section for environment variables. Due to recent changes, the value for <code>APP_ENVIRONMENT</code> must be set to <code>production</code> instead of <code>development</code>.

Here is the YAML file structure:

<pre>
env_variables:
  - name: APP_ENVIRONMENT
    value: development
  - name: DB_HOST
    value: db.example.local
</pre>

And the TOML file structure:

<pre>
[[env_variables]]
name = "APP_ENVIRONMENT"
value = "development"

[[env_variables]]
name = "DB_HOST"
value = "db.example.local"
</pre>

Please modify both <code>/home/user/deploy_settings.yaml</code> and <code>/home/user/deploy_settings.toml</code> to change the value for <code>APP_ENVIRONMENT</code> from <code>development</code> to <code>production</code>.

After making your changes, output a verification log named <code>/home/user/config_update.log</code> containing exactly the following format (including exact wording and spacing):

<pre>
YAML APP_ENVIRONMENT: production
TOML APP_ENVIRONMENT: production
</pre>

Make sure that only the <code>APP_ENVIRONMENT</code> environment variable changes, and that the rest of each file remains unaltered.
