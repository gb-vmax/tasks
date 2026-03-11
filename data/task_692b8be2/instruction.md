I'm an infrastructure engineer and I need help processing a server provisioning template. We have a template file at `/home/user/provisioning/server.conf.tmpl` that contains placeholder variables in the format `{{VARIABLE_NAME}}`. I need to substitute all the placeholders with real values and write the final config to `/home/user/provisioning/server.conf`.

Here are the substitutions I need made:

| Placeholder | Value |
|---|---|
| `{{HOSTNAME}}` | `prod-web-04` |
| `{{IP_ADDRESS}}` | `10.0.1.44` |
| `{{MAX_CONNECTIONS}}` | `512` |
| `{{TIMEOUT_SECONDS}}` | `30` |
| `{{ENVIRONMENT}}` | `production` |

The template file already exists at `/home/user/provisioning/server.conf.tmpl`. Please generate the final `/home/user/provisioning/server.conf` by replacing every placeholder with its corresponding value. The output file should have no remaining `{{...}}` placeholders — all five must be substituted.

Do not modify the original template file; it should remain unchanged at `/home/user/provisioning/server.conf.tmpl`.
